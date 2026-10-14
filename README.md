
# StemLab — Music Source Separation

A dark-themed Streamlit application for separating vocals and
instrumental components from audio using the Demucs deep learning model.

## Features

- Upload supported audio files
- Separate vocals, drums, bass, and other instruments
- Listen to individual audio stems
- Download separated WAV files
- Interactive Streamlit interface with a dark theme

## Tech Stack

- Python
- Streamlit
- Demucs
- PyTorch

## Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   pip install -r requirements.txt

4. Run the application:

   streamlit run app.py

## Note

Audio separation may take several minutes depending on audio length,
hardware, and the selected model. Model weights may be downloaded
on the first run.
