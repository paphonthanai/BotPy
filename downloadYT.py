from pytube import YouTube;

SAVE_PATH = "Desktop:/"

link = "https://www.youtube.com/watch?v=w8I0_phB6Jw"

yt = YouTube(link)

mp4_files = yt.streams.filter(file_extension="mp4")

mp4_720_files = mp4_files.get_by_resolution("720p")

mp4_720_files.download(SAVE_PATH)

