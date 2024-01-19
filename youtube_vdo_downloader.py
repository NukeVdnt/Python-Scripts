from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()
        print("Download Successful")
    except:
        print("Error")
    


link = input("Enter the URL: ")

download(link)
