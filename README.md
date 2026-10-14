# 🎧 Audio Source Separation Using Demucs

A Python-based music source separation application that uses the **Demucs deep learning model** to separate vocals and instrumental components from mixed audio recordings. The project provides a user-friendly interface built with Streamlit for uploading audio, processing tracks, listening to separated stems, and downloading the results.

**Live Demo:** [Audio Source Separation Web App](https://audio-source-separation-aiwwhxossvbqfzemhrggks.streamlit.app/)

## ✨ Features

- 🎵 Upload audio files for source separation.
- 🎤 Extract vocals from mixed music recordings.
- 🥁 Separate drums, bass, and other instrumental components.
- ▶️ Listen to the original audio and separated tracks.
- 📥 Download individual audio stems in WAV format.
- 🌙 Dark-themed, interactive Streamlit interface.
- 🧠 AI-powered audio separation using Demucs.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Deep Learning:** Demucs, PyTorch
- **Web Interface:** Streamlit
- **Audio Processing:** Demucs audio processing pipeline
- **Version Control:** Git and GitHub

## 📁 Project Structure

```text
audio-source-separation/
├── app.py
├── separator.py
├── source_separation.py
├── demucs_visualizer.html
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── input/
└── output/
```

*Note: The `input/` and `output/` folders are intended for local audio files and generated results. They may be excluded from GitHub.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/abiramiratan/audio-source-separation.git
cd audio-source-separation
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Ensure that `requirements.txt` includes Streamlit and Demucs, along with the project's other required dependencies.

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 🚀 How to Use

1. Launch the Streamlit application.
2. Upload a supported audio file.
3. Select the Demucs separation model.
4. Start the separation process.
5. Wait for the model to process the audio.
6. Listen to the available separated tracks.
7. Download the stems you need.

## 🎼 Output

The standard four-stem Demucs model can produce the following outputs:

| Stem | Description |
|---|---|
| Vocals | Singing and vocal components |
| Drums | Percussion and drum components |
| Bass | Bass instruments |
| Other | Remaining instrumental components |

The available stems depend on the selected model.

## 💻 Hardware and Performance

Audio processing time depends on the length of the input recording, available RAM, processor, GPU support, and selected model. The first run may take longer because the required pretrained model weights may need to be downloaded.

## 🔮 Future Enhancements

- Real-time processing status and progress feedback.
- Audio waveform visualization.
- Side-by-side original and separated audio playback.
- Support for additional separation models.
- Deployment as a publicly accessible web application.

## 👩‍💻 Author

**Abirami R**

- GitHub: [@abiramiratan](https://github.com/abiramiratan)
- Project Repository: [Audio Source Separation](https://github.com/abiramiratan/audio-source-separation)

## 📄 Disclaimer

This project uses the existing Demucs model for music source separation. It does not claim to train a new separation model from scratch. Please review the applicable model and software licenses before redistributing or deploying the application.

