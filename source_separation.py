
import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Supported audio extensions
SUPPORTED_EXTENSIONS = (
    ".wav",
    ".mp3",
    ".flac",
    ".ogg",
    ".m4a"
)

audio_files = [
    f for f in os.listdir(INPUT_DIR)
    if f.lower().endswith(SUPPORTED_EXTENSIONS)
]

if not audio_files:
    print("❌ No supported audio file found in input folder")
    sys.exit(1)

if len(audio_files) > 1:
    print("❌ Multiple audio files found. Keep only one.")
    sys.exit(1)

input_audio = audio_files[0]
INPUT_AUDIO = os.path.join(INPUT_DIR, input_audio)

print("🎧 Using input file:", INPUT_AUDIO)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Run Demucs using the current Python environment
command = [
    sys.executable,
    "-m",
    "demucs.separate",
    "--two-stems=vocals",
    INPUT_AUDIO,
    "-o",
    OUTPUT_DIR
]

print("🚀 Starting vocal separation...")

subprocess.run(command, check=True)

print("✅ Vocal separation completed!")
print("📁 Output folder:", OUTPUT_DIR)