import sys
from moviepy.editor import *

try:
    # getting the vdo
    video  = VideoFileClip(sys.argv[1])
    
    # extracting the audio
    video.audio.write_audiofile('audio.mp3')
except:
    print('Usage:- python audio_to_vdo.py [vdo_file]')
