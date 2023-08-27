from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth
import utils.video_summarizer_utils as vs
import yaml
from yaml.loader import SafeLoader

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
    This function defines the home page of the Streamlit app.

    It sets the title of the page and displays some text. It also prompts the
    user to select a page from the sidebar.
    """
    # Render login module
    name, authentication_status, username = authenticator.login('Login', 'main')

    # Check if user is authenticated
    if st.session_state['authentication_status']:
        authenticator.logout('Logout', 'sidebar', key='video_summarizer')
        st.title("Video Summarizer")
        st.write("Instructions here...")
        st.write("")  # Add whitespace between description and radio buttons

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
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')


if __name__ == '__main__':
    app()
