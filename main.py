import argparse

from download_tiktok_url import download_tiktok_url
from urls_finder import getUrlsFromUserName

parser = argparse.ArgumentParser(description='Download all tiktok videos from a user OR Download a single video from a tiktok url')
parser.add_argument('-u','--user',
                    help='user to download videos from', default=None)
parser.add_argument('-v','--videoUrl',
                    help='url of the video to download', default=None)
parser.add_argument('-o','--output',
                    help='name convention of the ouput, for example : `-o video` will name the videos `video_1.mp4, video_2.mp4, ...',
                    default='video')
parser.add_argument('--destination', '-d',
                    default='.',
                    help='destination folder to download videos to')

args = parser.parse_args()

USER = args.user
DESTINATION_FOLDER = args.destination
OUTPUT_NAME = args.output
VIDEO_URL = args.videoUrl

# 1 - Retrieve the list of urls from the user page
if USER and VIDEO_URL:
    raise Exception("You can't use -u and -v at the same time")
if USER is not None:
    urls = getUrlsFromUserName(USER, DESTINATION_FOLDER)
elif VIDEO_URL is not None:
    urls = [VIDEO_URL]
else:
    raise Exception("You must specify either a user or a video url")


# 2 - Download the videos from the list of urls and store them in the destination folder

for i in range(len(urls)):
    download_tiktok_url(urls[i], i, DESTINATION_FOLDER, OUTPUT_NAME)