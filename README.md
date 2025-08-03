# video-noise-cleaner

Silence the noise. Enhance speech clarity in your videos.

## Noise Reduction Pipeline for Video Audio (Speech Enhancement)

This project focuses on building a cost-effective, offline pipeline for background noise reduction in video audio using open-source tools. Below is the journey and technical steps followed to clean and enhance speech clarity from noisy recordings.

---

### Step 1: Extract Audio from Video

We first extract the audio stream from the video file using **FFmpeg**, converting it to mono WAV at 48kHz (which RNNoise expects):

```bash
ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 48000 -ac 1 audio.wav
```

---

### Step 2: Noise Reduction Using RNNoise (arnndn filter in FFmpeg)

Apply RNNoise using FFmpeg's `arnndn` filter with a pretrained `.rnnn` model:

```bash
ffmpeg -i audio.wav -af arnndn=m=/Users/georgizahariev/Desktop/2025-2026/eDynamix/edynamix-video-noise-cleaner/rnnoise-models/conjoined-burgers-2018-08-28/cb.rnnn cleaned_audio.wav
```

This significantly reduces background noise while preserving speech. Still not perfect – muffled voice or low speech presence may occur.

---

### Step 3: Post-Processing to Enhance Speech

#### A. Equalization (EQ)

Boost mid-range speech frequencies and cut irrelevant bands:

```bash
ffmpeg -i cleaned_audio.wav -af "equalizer=f=1000:width_type=h:width=200:g=8, \
equalizer=f=3000:width_type=h:width=300:g=6, \
equalizer=f=100:width_type=h:width=100:g=3, \
equalizer=f=50:width_type=h:width=100:g=-10, \
equalizer=f=12000:width_type=h:width=2000:g=-5" final_audio.wav
```

- Boosts voice clarity
- Reduces low-end rumble and high-end hiss

#### B. Dynamic Range Compression

Make quiet voices louder and balance volume spikes:

```bash
ffmpeg -i cleaned_audio.wav -af "acompressor=threshold=-25dB:ratio=3:attack=5:release=100" compressed.wav
```

#### C. Combine EQ + Compression

For best results, combine both filters in a single command:

```bash
ffmpeg -i cleaned_audio.wav -af "acompressor=threshold=-25dB:ratio=3:attack=5:release=100, \
equalizer=f=1000:width_type=h:width=200:g=8, \
equalizer=f=3000:width_type=h:width=300:g=6" final_audio.wav
```

---

### Step 4: AI Solution (Final Step)

**Demucs** stands out as the optimal solution for this project. It's an open-source deep learning model developed by **Facebook AI Research (FAIR)** for source separation — meaning it separates audio into components like vocals, instruments, background noise, etc.

```bash
pip install demucs

demucs audio.wav 
#Full file path might be needed
```

**Results**: Near-professional quality audio separation. This represents the current endpoint of our processing pipeline, delivering excellent speech enhancement through AI-powered source separation.

---

## Files in This Repo

| File                    | Description                                |
| ----------------------- | ------------------------------------------ |
| `audio.wav`           | Extracted original audio                   |
| `cleaned_audio.wav`   | Output after RNNoise filtering             |
| `compressed.wav`      | Audio after dynamic compression            |
| `final_audio.wav`     | Audio with both EQ and compression applied |
| `separated/htdemucs/` | Demucs-separated audio components          |

---

## Tools Used

- [FFmpeg](https://ffmpeg.org/)
- [RNNoise](https://github.com/xiph/rnnoise)
- [Demucs](https://github.com/facebookresearch/demucs)
- `.rnnn` models (e.g., `cb.rnnn`)
- Equalization & dynamic compression filters
- Shell scripting and local processing

---

## ✅ Final Output

You now have:

- 🎯 Clean speech separation using Demucs
- 🔇 Background noise effectively removed
- 🎧 Professional-grade audio enhancement
- 📁 Separated audio components in `separated/htdemucs/` directory

The Demucs approach provides the best balance of quality and simplicity for automated speech enhancement.

---

## Project Information

This project and research is part of the **eDynamix** project. Any further development was kept private.
