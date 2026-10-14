
import os
import sys
import shutil
import subprocess
import tempfile
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

st.set_page_config(
    page_title="StemLab | Music Separator",
    page_icon="🎧",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #0b0b12;
    color: #f4f4f8;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
.hero {
    padding: 28px;
    border: 1px solid #29263b;
    border-radius: 18px;
    background: linear-gradient(120deg, #19152b, #111827);
    margin-bottom: 24px;
}
.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
}
.hero p {
    color: #b9b6cb;
    font-size: 16px;
}
.stButton > button {
    background: #8b5cf6;
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 45px;
    font-weight: 600;
    width: 100%;
}
.stButton > button:hover {
    background: #7042d8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🎧 StemLab</h1>
    <p>Separate vocals and instruments from your favourite tracks
    using AI-powered Demucs source separation.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("01 · Upload your audio")
st.write("Choose an audio file to begin.")

uploaded_file = st.file_uploader(
    "Upload audio",
    type=["wav", "mp3", "flac", "ogg", "m4a"],
    help="For best compatibility, start with a WAV or MP3 file."
)

model = st.selectbox(
    "Separation model",
    ["htdemucs", "htdemucs_ft"],
    index=0
)

if uploaded_file:
    st.success(f"Ready: {uploaded_file.name}")
    st.audio(uploaded_file)

    if st.button("✨ Separate audio", use_container_width=True):
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            input_path = temp_path / Path(uploaded_file.name).name
            input_path.write_bytes(uploaded_file.getvalue())

            command = [
                sys.executable,
                "-m", "demucs.separate",
                "-n", model,
                "-o", str(OUTPUT_DIR),
                str(input_path)
            ]

            with st.spinner(
                "Demucs is processing your audio. "
                "This may take several minutes..."
            ):
                try:
                    result = subprocess.run(
                        command,
                        cwd=BASE_DIR,
                        capture_output=True,
                        text=True,
                        timeout=1800
                    )

                    if result.returncode != 0:
                        st.error("Audio separation failed.")
                        st.code(
                            (result.stderr or result.stdout)[-5000:]
                        )
                        st.stop()

                    song_name = input_path.stem
                    result_dir = OUTPUT_DIR / model / song_name

                    if not result_dir.exists():
                        st.error(
                            "Separation finished, but the output "
                            "folder could not be found."
                        )
                        st.stop()

                    st.session_state["result_dir"] = str(result_dir)
                    st.session_state["song_name"] = song_name
                    st.session_state["model"] = model
                    st.success("Audio separation completed!")

                except subprocess.TimeoutExpired:
                    st.error(
                        "Processing timed out. Try a shorter audio file."
                    )
                except Exception as exc:
                    st.error(f"Unexpected error: {exc}")

if st.session_state.get("result_dir"):
    result_dir = Path(st.session_state["result_dir"])

    if result_dir.exists():
        st.divider()
        st.subheader("02 · Your separated tracks")
        st.caption(
            f"Track: {st.session_state['song_name']} "
            f"· Model: {st.session_state['model']}"
        )

        stems = [
            ("vocals", "🎤 Vocals"),
            ("drums", "🥁 Drums"),
            ("bass", "🎸 Bass"),
            ("other", "🎹 Other instruments")
        ]

        columns = st.columns(2)

        for index, (stem, title) in enumerate(stems):
            audio_path = result_dir / f"{stem}.wav"

            if audio_path.exists():
                with columns[index % 2]:
                    st.markdown(f"### {title}")
                    st.audio(str(audio_path))

                    with open(audio_path, "rb") as audio_file:
                        st.download_button(
                            f"Download {stem}",
                            data=audio_file.read(),
                            file_name=f"{stem}.wav",
                            mime="audio/wav",
                            key=f"download_{stem}"
                        )

        st.info(
            "Available stems depend on the selected Demucs model. "
            "The standard four-stem model separates vocals, drums, "
            "bass, and other instruments."
        )
