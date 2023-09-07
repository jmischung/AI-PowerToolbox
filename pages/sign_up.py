"""
This file contains the implementation of the Sign Up page for the Streamlit app.
It uses the `streamlit_authenticator` package for user authentication and
registration. The page is can only be accessed its URL and by users who are not
authenticated.
"""
from time import sleep

import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages

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
    This function is the main entry point for the Sign Up page.
    It sets up the sidebar pages, hides the Home page, and registers the user
    using the authenticator.

    If the user is registered successfully, it updates the config file and
    redirects the user to the Home page.
    """
    # Set sidebar pages
    show_pages([
        Page("pages/home.py", "Home", icon="🏠"),
        Page("pages/sign_up.py", "Sign Up", icon="📝")
    ])

    # Hide home page from sidebar
    hide_pages(["Home"])
    try:
        if authenticator.register_user('Register user', preauthorization=True):
            with open("config.yaml", "w") as file:
                yaml.dump(config, file, sort_keys=False)
            st.success("User registered successfully. You'll be redirected "
                       "to the home page shortly.")
            st.session_state["authentication_status"] = True
            sleep(5)
            switch_page("home")
            st.write(st.session_state)
    except Exception as e:
        st.error(e)


if __name__ == "__main__":
    app()
