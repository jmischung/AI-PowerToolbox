import os
import yaml
from yaml.loader import SafeLoader
from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
from st_pages import Page, show_pages
from st_audiorec import st_audiorec

import whisper
import wave

from utils.pages_list import sidebar_pages

# Load config file
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Set paths
PROJECT_ROOT = Path(__file__).parent.parent
TEMP_DIR = PROJECT_ROOT / 'temp'


def app():
    # Check if user is authenticated
    if st.session_state['authentication_status']:
        authenticator.logout('Logout', 'sidebar', key='audio_transcriber')
        st.title("Audio Transcriber")
        st.write("Instructions here...")
        st.write("")  # Add whitespace between description and radio buttons

        # Set sidebar
        show_pages(sidebar_pages)

        # Instantiate whisper
        model = whisper.load_model("base")

        # Instantiate audio recorder
        wav_audio_data = st_audiorec()

        if wav_audio_data is not None:
            audio_file_path = str(TEMP_DIR / 'audio.wav')

            # Save audio data to file
            with wave.open(audio_file_path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(4)
                wf.setframerate(44100)
                wf.writeframes(wav_audio_data)

            # Transcribe audio
            output = model.transcribe(audio_file_path, fp16=False)
            st.write(output["text"])

            # Delete audio file
            os.remove(audio_file_path)
    else:
        show_pages([
            Page("welcome.py", "Welcome"),
        ])
        switch_page("welcome")


if __name__ == "__main__":
    app()
