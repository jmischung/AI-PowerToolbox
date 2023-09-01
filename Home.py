import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from streamlit.logger import get_logger
from st_pages import Page, show_pages

import yaml
from yaml.loader import SafeLoader

LOGGER = get_logger(__name__)

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
    This function defines the home page of the Streamlit app.

    It sets the title of the page and displays some text. It also prompts the
    user to select a page from the sidebar.
    """

    # Render login module
    name, authentication_status, username = authenticator.login('Login', 'sidebar')

    # Check if user is authenticated
    if authentication_status:
        switch_page("video summarizer")
        # Display title and text
        st.title("Welcome to my AI-Powered Toolbox!")
        st.write("Select a tool from the sidebar to get started.")

        # Set sidebar
        show_pages([
            Page("home.py", "Home", icon="🏠"),
            Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥"),
        ])
        authenticator.logout('Logout', 'sidebar', key='home')
    elif authentication_status is False:
        st.error("Incorrect username or password. Please try again.")
    elif authentication_status is None:
        # Display title and text before login
        st.title("Welcome")
        st.write("""
            You've found Origin 46's AI-Powered Toolbox. All of your analytics, 
            information, and AI-powered apps to make work and life easier are here.\n\n
            To gain access, click the 'Request Access' dropdown below and fill out 
            the form. Once you've been approved, you'll receive an email inviting 
            inviting you to create an account.
        """)

        # Set sidebar
        show_pages([
            Page("home.py", "Home", icon="🏠"),
            Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥"),
        ])

        # Request access form
        expander = st.expander("Request Access", expanded=False)
        with expander.form("Request Access"):
            # Form fields
            st.write("Please fill out the form below to request access.")
            form_name = st.text_input("Name")
            form_email = st.text_input("Email")
            form_note = st.text_area("Note about how you learned about this toolbox")

            # Submit button
            submitted = st.form_submit_button("Submit")
            if submitted:
                LOGGER.info("Submitted")
                st.success(
                    "Your request has been submitted. You will receive an email "
                    "once your request has been approved."
                )


if __name__ == '__main__':
    app()
