# TikTok Video Downloader

## Working in November 2022

### How to use

1. Install Python 3.8 or higher
2. Install Chrome v^107
2. Install the requirements: `pip install -r requirements.txt --user`
3. Run the script: `python tiktok.py ...args`

## example:

### Download all videos from a user
```
python tiktok.py -u "alexandredevauxtiktok"
```

### Download a specific video
```
python tiktok.py -v "https://www.tiktok.com/@alexandredevauxtiktok/video/7010000000000000000"
```

## Options

```
  -h, --help            show this help message and exit
  
  -u, --user            user to download videos from
  
  -v, --videoUrl        url of the video to download
  
  -o, --output          name convention of the ouput, for example : `-o video` will name the videos `video_1.mp4, video_2.mp4, ..., default is `video`
  
  --destination, -d     destination folder, default is '.' (current folder)
```