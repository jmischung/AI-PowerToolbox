import yaml
from yaml.loader import SafeLoader
from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
from st_pages import Page, show_pages
from st_audiorec import st_audiorec

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

        # Instantiate audio recorder
        wav_audio_data = st_audiorec()
    else:
        show_pages([
            Page("welcome.py", "Welcome"),
        ])
        switch_page("welcome")


if __name__ == "__main__":
    app()
