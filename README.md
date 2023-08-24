# Look Who's Talking: Active Speaker Detection in the Wild

### Paper
- [Latest version (2021-08-17)](https://arxiv.org/abs/2108.07640)
  - Statistics and reference performances of the dataset are changed, as the annotation are updated. 
- [INTERSPEECH proceeding (2021-06-15)](https://www.isca-speech.org/archive/pdfs/interspeech_2021/kim21k_interspeech.pdf)

### Dependencies
```
pip install -r requirements.txt
```

In addition to the Python dependencies, `ffmpeg` must be installed on the system.

### Instructions
1. Download the videos to `$DATA_DIR/original` usign [yt-dlp](https://github.com/yt-dlp/yt-dlp).

```
yt-dlp --verbose -f best/best -o {download_path} https://www.youtube.com/watch?v={vid}
```

2. Run the following to convert the videos and visualise the annotation.

```
python3 run_convert.py --data_dir $DATA_DIR
python3 run_visualize.py --data_dir $DATA_DIR
```

### FAQ
- About the meaning of 'eval' in jsons

-> "label" is the annotation of each frame, and has 1 (active) or 0 (non-active). On the other hand, "eval" indicates whether each frame is evaluated or not. The start and end frames of each track are excluded from evaluation, beacause it is nearly impossible to get accurate timestamps of boundary frames.

- About the unavailable youtube videos

-> YouTube videos might be removed by the uploader. In that case, conventionally, evaluate the model performance without them. (I would like to share the dataset, but due to the copyright issue, I cannot.)

- About box coordinates

-> In json, elements of bbox list represent [x1, y1, x2, y2], where (x1, y1) is the top-left coordinate and (x2, y2) is the bottom-right coordinate. The coordinates are normalized with respect to the video frame size, where (0.0, 0.0) corresponds to the top-left, and (1.0, 1.0) corresponds to bottom-right.

-> You can find some negative coordinates in json. The reason is that some of the faces are on the edges of the video frame, and we draw bboxes over the video frame with zero-padded edges.

<img width="150" alt="image" src="https://github.com/clovaai/lookwhostalking/assets/20121380/ce46e756-b3f9-4af3-88e1-9d7a96eac1a4">

### Citation
Please cite the following if you make use of the code.

```
@inproceedings{kim2021you,
  title={Look Who's Talking: Active Speaker Detection in the Wild},
  author={Kim, You Jin and Heo, Hee-Soo and Choe, Soyeon and Chung, Soo-Whan and Kwon, Yoohwan and Lee, Bong-Jin and Kwon, Youngki and Chung, Joon Son},
  booktitle={Interspeech},
  year={2021}
}
```

### License

```
Copyright (c) 2021-present NAVER Corp.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
