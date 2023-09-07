"""
This file contains the implementation of the Home page for the Streamlit app.
It is the main entry point for authenticated users and displays a welcome
message and sets up the sidebar pages for the app. If the user is not
authenticated, it redirects the user to the Welcome page. The page can only be
accessed by authenticated users.
"""
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages


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


def app():
    """
    This function is the main entry point for the Home page.
    It checks if the user is authenticated and displays the Home page with the sidebar pages.
    If the user is not authenticated, it redirects the user to the Welcome page.
    """
    # Check if user is authenticated
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'sidebar', key='home')
        st.title("Home")
        st.write("Welcome to my AI-Powered Toolbox!")

        # Set sidebar pages
        show_pages([
            Page("pages/home.py", "Home", icon="🏠"),
            Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥"),
        ])
    else:
        show_pages([
            Page("welcome.py", "Welcome"),
        ])
        switch_page("welcome")


if __name__ == "__main__":
    app()
