import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def app():
    """
    This function defines the home page of the Streamlit app.

    It sets the title of the page and displays some text. It also prompts the
    user to select a page from the sidebar.
    """
    st.set_page_config(
        page_title="AI-Powered Toolbox",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    st.title("Welcome to my AI-Powered Toolbx!")
    st.write("Select a tool from the sidebar to get started.")

    st.sidebar.success("Select a tool to get started.")


if __name__ == '__main__':
    app()
