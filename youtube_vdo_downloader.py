import sys
from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()
        print("Download Successful")
    except:
        print("Error")

try:   
    link = sys.argv[1]
    download(link)
except:
    print("Usage:- python youtube_vdo_downloader.py [your_link]")


