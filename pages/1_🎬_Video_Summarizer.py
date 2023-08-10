import streamlit as st
import utils.video_summarizer_utils as vs


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
    transcription = vs.transcribe_audio('./temp/audio.mp4')
    key_points = vs.key_points_extraction(transcription)

    return key_points


def app():
    """
    This function defines the home page of the Streamlit app.

    It sets the title of the page and displays some text. It also prompts the
    user to select a page from the sidebar.
    """
    st.set_page_config(page_title="Video Summarizer", page_icon="🎬")

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


if __name__ == '__main__':
    app()
