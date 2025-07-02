Extracting audio from video

ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 48000 -ac 1 audio.wav 

