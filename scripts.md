# Audio Processing Scripts

## Step 1: Extract Audio from Video

```bash
ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 48000 -ac 1 audio.wav 
```

## Step 2: Apply RNNoise Model

```bash
ffmpeg -i audio.wav -af arnndn=m=/Users/georgizahariev/Desktop/2025-2026/eDynamix/edynamix-video-noise-cleaner/rnnoise-models/conjoined-burgers-2018-08-28/cb.rnnn cleaned_audio.wav
```

*Note: Still not perfect - requires additional post-processing*

## Step 3: Custom Post-Processing with Equalization

```bash
ffmpeg -i cleaned_audio.wav -af "equalizer=f=1000:width_type=h:width=200:g=8,equalizer=f=3000:width_type=h:width=300:g=6,equalizer=f=100:width_type=h:width=100:g=3,equalizer=f=50:width_type=h:width=100:g=-10,equalizer=f=12000:width_type=h:width=2000:g=-5" final_audio.wav
```

## Step 4: Apply Dynamic Range Compression

```bash
ffmpeg -i cleaned_audio.wav -af "acompressor=threshold=-25dB:ratio=3:attack=5:release=100" compressed.wav
```

## Step 5: Combine Equalization and Compression

```bash
ffmpeg -i cleaned_audio.wav -af "acompressor=threshold=-25dB:ratio=3:attack=5:release=100, equalizer=f=1000:width_type=h:width=200:g=8, equalizer=f=3000:width_type=h:width=300:g=6" final_audio.wav
```

## Step 6: AI Solution with Demucs

```bash
pip install demucs
demucs audio.wav
```





