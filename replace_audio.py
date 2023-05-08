import sys
import os
from moviepy.editor import *


def display_help():
    print("Usage: python replace_audio.py [-h] folder_path")
    print("\nReplace the audio in a video file (mp4) with a provided audio file (wav or mp3).")
    print("Arguments:")
    print("  folder_path  Path to the folder containing video and audio files.")
    print("  -h           Show this help message and exit.")


def replace_audio(folder_path):
    audio_extensions = ['.mp3', '.wav']
    video_extensions = ['.mp4']
    processed_audio_files = set()

    for file in os.listdir(folder_path):
        if any(file.endswith(ext) for ext in video_extensions):
            video_file = os.path.join(folder_path, file)
            basename = os.path.splitext(file)[0]

            audio_file = None
            for ext in audio_extensions:
                if os.path.exists(os.path.join(folder_path, f'{basename}{ext}')):
                    audio_file = os.path.join(folder_path, f'{basename}{ext}')
                    processed_audio_files.add(audio_file)
                    break

            if audio_file is None:
                print(f'No matching audio file found for {file}')
                continue

            video = VideoFileClip(video_file)
            audio = AudioFileClip(audio_file)

            video_with_new_audio = video.set_audio(audio)
            video_with_new_audio.write_videofile(os.path.join(folder_path, f'{basename}_ad.mp4'))

    for file in os.listdir(folder_path):
        if any(file.endswith(ext) for ext in audio_extensions) and os.path.join(folder_path, file) not in processed_audio_files:
            print(f'No matching video file found for {file}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Please provide the folder path as an argument.")
        display_help()
        sys.exit(1)

    if sys.argv[1] == '-h':
        display_help()
        sys.exit(0)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid folder path.")
        sys.exit(1)

    replace_audio(folder_path)
