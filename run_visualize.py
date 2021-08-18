## assumes label at 5fps and video at 25fps

import glob, pdb, json, os, subprocess, cv2, shutil, argparse

def vis_labels(args,file):

    with open(file) as f:
        data = json.load(f)

    ref = os.path.splitext(os.path.basename(file))[0] # YouTube reference

    vid = os.path.join(args.avi_dir,ref,'video.avi') # saved video AVI
    aud = os.path.join(args.avi_dir,ref,'audio.wav') # saved audio PCM
    frm_dir = os.path.join(args.tmp_dir,'{}_frames'.format(ref)) # temporary extracted frames
    tmp_avi = os.path.join(args.tmp_dir,'{}.avi'.format(ref)) # temporary video file
    out_mp4 = os.path.join(args.out_dir,'{}.mp4'.format(ref)) # mp4 file to save

    # skip if output already exists
    if os.path.exists(out_mp4):
        print('File already exists. Delete the original file to re-run the visualisation.')
        return

    # skip if input files do not exist
    if not (os.path.exists(vid) and os.path.exists(aud)):
        print('Skipping {} due to missing video or audio file'.format(ref))
        return


    # make directory for frame extraction
    os.makedirs(frm_dir,exist_ok=True)
    command = ("ffmpeg -y -i %s -qscale:v 2 -threads 1 -f image2 %s" % (vid,os.path.join(frm_dir,'%06d.jpg'))) 
    output = subprocess.call(command, shell=True, stdout=None)

    assert output == 0

    # get the list of frames
    flist = glob.glob(os.path.join(frm_dir,'*.jpg'))
    flist.sort()

    # make an empty list of face instances
    faces = [[] for i in range(1000000)]

    for datum in data:

        for fidx, frame in enumerate(data[datum]) :

            # current frame number at 25fps
            cfr = int(frame['time']*args.frame_rate)

            info = {'track': datum, 'bbox': frame['bbox'] ,'label': frame['label'], 'eval':frame['eval']}

            for ii in range(-2,3):
                if cfr+ii >= 0:
                    faces[cfr+ii].append(info)

    # get height and width of image
    first_image = cv2.imread(flist[0])
    fw = first_image.shape[1]
    fh = first_image.shape[0]

    # initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vOut = cv2.VideoWriter(tmp_avi, fourcc, args.frame_rate, (fw,fh))

    # for every frame
    for fidx, fname in enumerate(flist):

        # read image
        image = cv2.imread(fname)

        for face in faces[fidx]:

            # get bbox coordinates
            x1 = int(face['bbox'][0]*fw)
            x2 = int(face['bbox'][2]*fw)
            y1 = int(face['bbox'][1]*fh)
            y2 = int(face['bbox'][3]*fh)

            # color of bbox
            clr = float(face['label'])*255

            # print bbox on image
            cv2.rectangle(image,(x1,y1,x2-x1,y2-y1),(0,clr,255-clr),2)

            # double box if eval is positive
            if face['eval'] == 1:
                cv2.rectangle(image,(x1-6,y1-6,x2-x1+12,y2-y1+12),(0,clr,255-clr),2)

            # write track number
            cv2.putText(image,face['track'],(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

        # write to video
        vOut.write(image)

        if fidx % 100 == 0:
            print('Saved frame {:d} of {:d}, {}'.format(fidx,len(flist),ref))

    vOut.release()

    # combine saved video with original audio
    command = ("ffmpeg -y -i %s -i %s -c:v libx264 -c:a aac -strict -2 %s" % (tmp_avi,aud,out_mp4)) #-async 1 
    output = subprocess.call(command, shell=True, stdout=None)

    assert output == 0

    # remove temporary files
    shutil.rmtree(frm_dir) 
    os.remove(tmp_avi)



# ========== ========== ========== ==========
# # PARSE ARGS AND RUN SCRIPTS
# ========== ========== ========== ==========

parser = argparse.ArgumentParser(description = "VisFaceTracks");
parser.add_argument('--data_dir',       type=str, default='exps', help='Output direcotry');
parser.add_argument('--json_dir', help="dataset json files", type=str, default='json')
parser.add_argument('--frame_rate',     type=int, default=25,   help='Frame rate');
args = parser.parse_args();

files = glob.glob('{}/*.json'.format(args.json_dir))

setattr(args,'avi_dir',os.path.join(args.data_dir,'pyavi'))
setattr(args,'out_dir',os.path.join(args.data_dir,'viz_asd'))
setattr(args,'tmp_dir',os.path.join(args.data_dir,'tmp'))

os.makedirs(args.out_dir,exist_ok=True)

for file in files:
    vis_labels(args, file)


