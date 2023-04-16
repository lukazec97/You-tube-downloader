

from pytube import Playlist
import os
from pydub import AudioSegment
from moviepy.editor import *
# Replace the playlist URL with the URL of the playlist you want to download
playlist_url = "https://www.youtube.com/playlist?list=PLXnQbBsB_NnJuevcSpBO1_0wibuceFxE9"
# playlist_url = "https://youtube.com/playlist?list=PLXnQbBsB_NnKJYCR6EX9dT2cOjVMX7z3R"
ffmeg_path = "C:/Users/lukaz/Desktop/py/ffmpeg/bin/ffmpeg.exe"

playlist = Playlist(playlist_url)
# Print the playlist title
print("Playlist Title:", playlist.title)

# Download each video in the playlist and extract its audio in mp4 format
for video in playlist.videos:
    try:
        os.makedirs("./mp3", exist_ok=True)
        print("Downloading audio:", video.title)
        # audio_streams = video.streams.filter(only_audio=True, file_extension='mp4')
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

# # Convert each mp4 audio file to MP3 using pydub
# for filename in os.listdir("./temp2"):
#     video_path = video_stream.default_filename
#     audio_path = video_path.split(".")[0] + ".mp3"
#     video_clip = AudioFileClip(video_path)
#     video_clip.write_audiofile(audio_path)
#     video_clip.close()




# from pytube import Playlist
# import ffmpeg
# import os
# # Replace the playlist URL with the URL of the playlist you want to download
# playlist_url = "https://www.youtube.com/playlist?list=PLXnQbBsB_NnJuevcSpBO1_0wibuceFxE9"

# # Create a Playlist object
# playlist = Playlist(playlist_url)

# # Print the playlist title
# print("Playlist Title:", playlist.title)

# # Download each audio in the playlist
# for video in playlist.videos:
#     print("Downloading audio:")
#     audio_streams = video.streams.filter(only_audio=True, file_extension='mp4')
#     audio_streams.first().download(output_path="./temp", filename_prefix="audio_")
#     print("Audio download complete:", video.title)

# # Convert the MP4 files to MP3 using a third-party library like ffmpeg
# # (you can install ffmpeg using "pip install ffmpeg-python")


# # Create a directory to store the MP3 files
# os.makedirs("./mp3", exist_ok=True)

# # Convert each audio file in the "temp" directory to MP3
# for filename in os.listdir("./temp"):
#     if filename.endswith(".mp4"):
#         mp4_filename = f"./temp/{filename}"
#         audio_filename = f"./mp3/{filename.replace('.mp4', '.mp3')}"
#         stream = ffmpeg.input(mp4_filename)
#         stream = ffmpeg.output(stream, audio_filename, format='mp3')
#         ffmpeg.run(stream)

# # Remove the "temp" directory
# os.system("rm -rf ./temp")




# from pytube import Playlist

# # Replace the playlist URL with the URL of the playlist you want to download
# playlist_url = "https://www.youtube.com/playlist?list=PLXnQbBsB_NnJuevcSpBO1_0wibuceFxE9"

# # Create a Playlist object
# playlist = Playlist(playlist_url)

# # Print the playlist title
# print("Playlist Title:", playlist.title)

# # Download each video in the playlist
# for video in playlist.videos:
#     print("Downloading:", video.title)
#     video.streams.get_highest_resolution().download()
#     print("Download complete:", video.title)
