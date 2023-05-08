# Audio Replacement Script

This Python script replaces the audio in a video file (MP4) with a provided audio file (MP3 or WAV).

## Installation

1. Install Python 3.x if you haven't already: https://www.python.org/downloads/

2. Install MoviePy and FFmpeg by running the following command in the command prompt:

 
 ```
 pip install moviepy
 ```
 

## Usage

1. Place the video and audio files with the same base name in the same folder. The script will process all video files in the folder and replace their audio with the corresponding audio files. The output files will be saved in the same folder with the same base name and `_ad.mp4` appended.

2. Run the script from the command line as follows:

 ```
python replace_audio.py C:\path\to\your\folder
 ```
 
 Replace `C:\path\to\your\folder` with the folder path containing the video and audio files.

## Help

For help, run the script with the `-h` argument:

 ```
python replace_audio.py -h
 ```


## Additional Information

- If both a WAV and MP3 file are present for a video, the script will use the WAV file.
- If there is an MP4 file with no matching audio file, a message will be displayed.
- If there is an audio file with no matching video file, a message will be displayed.
