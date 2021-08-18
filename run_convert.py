#!/usr/bin/python

import sys, time, os, pdb, argparse, subprocess, glob, cv2, itertools

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


def convert_video(args, videofile, ref):

    vid_out = os.path.join(args.avi_dir,ref,'video.avi')
    aud_out = os.path.join(args.avi_dir,ref,'audio.wav')

    # Check if the conversion is already done
    if os.path.exists(aud_out) and not args.overwrite:
        print('Already done %s'%ref)
        return

    # Make new directory to save the files
    os.makedirs(os.path.join(args.avi_dir,ref),exist_ok=True)

    # Convert audio and video
    if get_length(videofile) >= args.max_seconds:
      command = ("ffmpeg -y -i %s -async 1 -qscale:v 2 -r %d -t %.1f %s" % (videofile, args.frame_rate, args.max_seconds, vid_out))
    else:
      command = ("ffmpeg -y -i %s -async 1 -qscale:v 2 -r %d %s" % (videofile, args.frame_rate, vid_out)) #-async 1  -deinterlace
    output = subprocess.call(command, shell=True, stdout=None)

    assert output == 0

    command = ("ffmpeg -y -i %s -ac 1 -vn -acodec pcm_s16le -ar 16000 %s" % (vid_out, aud_out)) 
    output = subprocess.call(command, shell=True, stdout=None)

    assert output == 0



# ========== ========== ========== ==========
# # PARSE ARGS AND RUN SCRIPTS
# ========== ========== ========== ==========

parser = argparse.ArgumentParser(description = "ConvertVideo");
parser.add_argument('--data_dir',       type=str, default='exps', help='Output direcotry');
parser.add_argument('--frame_rate',     type=int, default=25,   help='Frame rate');
parser.add_argument('--max_seconds',    type=float, default=1200, help='Maximum length of input video in seconds, if longer, we cut to this length');
parser.add_argument('--overwrite',      dest='overwrite', action='store_true', help='Re-run pipeline even if already run')
args = parser.parse_args();

setattr(args,'avi_dir',os.path.join(args.data_dir,'pyavi'))
setattr(args,'original_dir',os.path.join(args.data_dir,'original'))

exts = ['.mkv', '.mp4', '.webm']

files = [glob.glob('{}/*{}'.format(args.original_dir,ext)) for ext in exts]
files = sum(files,[])

for file in files:
    ref = os.path.splitext(os.path.basename(file))[0]
    convert_video(args,file,ref)
