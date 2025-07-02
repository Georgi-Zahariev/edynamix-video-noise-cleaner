import noisereduce as nr
import librosa
import soundfile as sf
import sys
import os

def reduce_noise(input_wav, output_wav):
    print(f"Loading audio: {input_wav}")
    y, sr = librosa.load(input_wav, sr=None)

    print("Reducing noise...")
    reduced = nr.reduce_noise(y=y, sr=sr)

    print(f"Saving cleaned audio to: {output_wav}")
    sf.write(output_wav, reduced, sr)
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python noise_reduce.py input.wav output.wav")
        sys.exit(1)

    input_wav = sys.argv[1]
    output_wav = sys.argv[2]

    if not os.path.exists(input_wav):
        print(f"Error: {input_wav} does not exist.")
        sys.exit(1)

    reduce_noise(input_wav, output_wav)
