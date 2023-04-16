

from pytube import Playlist
import os
from pydub import AudioSegment
from moviepy.editor import *
playlist_url = "https://www.youtube.com/playlist?list=PLXnQbBsB_NnJuevcSpBO1_0wibuceFxE9"

playlist = Playlist(playlist_url)
print("Playlist Title:", playlist.title)

# Download each video in the playlist and extract its audio in mp4 format
for video in playlist.videos:
    try:
        os.makedirs("./mp3", exist_ok=True)
        print("Downloading audio:", video.title)
        video_stream = video.streams.filter(only_audio=True).first()
        video_file = video_stream.download(output_path="mp3")

        # convert the downloaded video to MP3 using moviepy
        video_clip = AudioFileClip(video_file)
        audio_file = video_file.split(".")[0] + ".mp3"
        video_clip.write_audiofile(audio_file)
        video_clip.close()
        print("Audio download complete:", video.title)
    except Exception as e:
        print("Error downloading audio:", e)

