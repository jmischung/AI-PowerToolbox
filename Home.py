import streamlit as st
import streamlit_authenticator as stauth
from streamlit.logger import get_logger

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
    name, authentication_status, username = authenticator.login('Login', 'main')

    # Check if user is authenticated
    if authentication_status:
        # Display title and text
        st.title("Welcome to my AI-Powered Toolbx!")
        st.write("Select a tool from the sidebar to get started.")

        # Set sidebar
        st.sidebar.success("Select a tool to get started.")
        authenticator.logout('Logout', 'sidebar', key='home')
    elif authentication_status is False:
        st.error("Incorrect username or password. Please try again.")
    elif authentication_status is None:
        st.error("Please enter your username and password to login.")


if __name__ == '__main__':
    app()
