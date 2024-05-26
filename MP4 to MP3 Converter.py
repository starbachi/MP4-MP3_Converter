from moviepy.editor import AudioFileClip
import os
import glob


def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    audio = AudioFileClip(mp4_file_path)
    audio.write_audiofile(mp3_file_path)

# Get all mp4 files in the current directory
mp4_files = glob.glob("*.mp4")

# Convert each mp4 file to mp3
for mp4_file in mp4_files:
    mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
    convert_mp4_to_mp3(mp4_file, mp3_file)
