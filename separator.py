import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# find any .wav file in input folder
wav_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".wav")]

if not wav_files:
    print("❌ No .wav file found in input folder")
    sys.exit(1)

if len(wav_files) > 1:
    print("❌ Multiple .wav files found. Keep only one.")
    sys.exit(1)

input_wav = wav_files[0]
INPUT_AUDIO = os.path.join(INPUT_DIR, input_wav)

print("🎧 Using input file:", INPUT_AUDIO)

os.makedirs(OUTPUT_DIR, exist_ok=True)

command = [
    "demucs",
    "--two-stems=vocals",
    INPUT_AUDIO,
    "-o",
    OUTPUT_DIR
]

subprocess.run(command, check=True)
