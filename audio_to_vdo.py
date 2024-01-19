from moviepy.editor import *

# getting the vdo
video  = VideoFileClip("video.mp4")

# extracting the audio
video.audio.write_audiofile("video.mp3")
