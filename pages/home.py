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

# Set sidebar
show_pages([
    Page("welcome.py", "Welcome"),
    Page("pages/home.py", "Home", icon="🏠"),
    Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥")
])


def app():
    # Check if user is authenticated
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'sidebar', key='home')
        st.title("Home")
        st.write("Welcome to my AI-Powered Toolbox!")

        # Set sidebar pages
        show_pages([
            Page("pages/home.py", "Home", icon="🏠"),
            Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥")
        ])
    else:
        show_pages([
            Page("welcome.py", "Welcome"),
        ])
        switch_page("welcome")


if __name__ == "__main__":
    app()
