import yaml
from yaml.loader import SafeLoader
from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
from st_pages import Page, show_pages

import utils.video_summarizer_utils as vs

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


def summarize_video(video_platform, video_url, page_embed):
    """
    This function takes the video platform, URL, and page embed and returns
    a summary of the video.

    Args:
        video_platform (str): The video platform (either "YouTube" or "Vimeo").
        video_url (str): The URL of the video.
        page_embed (str): The page embed (optional).

    Returns:
        str: A summary of the video.
    """
    # Call function to summarize video
    vs.get_audio_youtube(video_url)
    transcription = vs.transcribe_audio(TEMP_DIR / 'audio.mp4')
    key_points = vs.key_points_extraction(transcription)

    return key_points


def app():
    """
    The primary application function for the Streamlit video summarizer app.

    This function initializes the Streamlit application, handles user authentication,
    and provides interface elements for video selection and summarization.

    Based on user authentication status, it displays the corresponding interface:
    - Authenticated users are presented with options to select a video platform,
    input a video URL, optionally input a page embed, and get a video summary.
    - Non-authenticated users receive an error message.
    """
    # Render login module
    name, authentication_status, username = authenticator.login('Login', 'main')

    # Check if user is authenticated
    if st.session_state['authentication_status']:
        authenticator.logout('Logout', 'sidebar', key='video_summarizer')
        st.title("Video Summarizer")
        st.write("Instructions here...")
        st.write("")  # Add whitespace between description and radio buttons

        # Set sidebar
        show_pages([
            Page("pages/home.py", "Home", icon="🏠"),
            Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥")
        ])

        # Add radio buttons for video platform selection
        video_platform = st.radio("Select a video platform", ("YouTube", "Vimeo"), index=0)

        # Add text input for video URL
        video_url = st.text_input("Video URL")

        # Add optional text input for page embed
        page_embed = st.text_input("Page Embed (optional)", value="", key="page_embed")

        # Add button to summarize video
        if st.button("Summarize"):
            summary = summarize_video(video_platform, video_url, page_embed)
            st.markdown(summary)
    else:
        show_pages([
            Page("welcome.py", "Welcome"),
        ])
        switch_page("welcome")


if __name__ == '__main__':
    app()
