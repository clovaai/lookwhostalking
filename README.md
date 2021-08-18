# Look Who's Talking: Active Speaker Detection in the Wild

### Dependencies
```
pip install -r requirements.txt
```

In addition to the Python dependencies, `ffmpeg` must be installed on the system.

### Instructions

First, download the videos to `$DATA_DIR/original`. 

Run the following to convert the videos and visualise the labels.

```
python3 run_convert.py --data_dir $DATA_DIR
python3 run_visualize.py --data_dir $DATA_DIR
```

### Citation

Please cite the following if you make use of the code.

```
@inproceedings{kim2021you,
  title={Look Who's Talking: Active Speaker Detection in the Wild},
  author={Kim, You Jin and Heo, Hee-Soo Heo and Choe, Soyeon and Chung, Soo-Whan and Kwon, Yoohwan and Lee, Bong-Jin and Kwon, Youngki and Chung, Joon Son},
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
