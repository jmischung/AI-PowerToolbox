"""
This file contains the implementation of the Welcome page for the Streamlit app.
It displays a welcome message and allows the user to log in or submit a form
requesting to be registered and added to the preauthorization list.
"""
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from streamlit.logger import get_logger
from st_pages import Page, show_pages, hide_pages

import yaml
from yaml.loader import SafeLoader

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    This function is the main entry point for the Welcome page. It displays a
    welcome message and allows the user to log in or submit a form requesting to
    be registered and added to the preauthorization list. If the user is
    authenticated, it redirects the user to the Home page for authorized users.
    """
    # Render login module
    name, authentication_status, username = authenticator.login('Login', 'sidebar')

    # Set sidebar
    show_pages([
        Page("welcome.py", "Welcome"),
        Page("pages/home.py", "Home", icon="🏠"),
        Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥"),
        Page("pages/sign_up.py", "Sign Up", icon="📝")
    ])

    # Check if user is authenticated
    if authentication_status:
        # Redirect to home page after login
        switch_page("home")
    elif authentication_status is False:
        st.error("Incorrect username or password. Please try again.")
    elif authentication_status is None:
        # Display title and text before login
        st.title("Welcome")
        st.write("""
            You've found Origin 46's AI-Powered Toolbox. All of our analytics, 
            information, and AI-powered apps to make work and life easier are here.\n\n
            To gain access, click the 'Request Access' dropdown below and fill out 
            the form. Once you've been approved, you'll receive an email inviting 
            you to create an account.
        """)

        # Set sidebar
        hide_pages([
            "Home",
            "Video Summarizer",
            "Sign Up"
        ])

        # Request access form
        expander = st.expander("Request Access", expanded=False)
        with expander.form("Request Access", clear_on_submit=True):
            # Form fields
            st.write("Please fill out the form below to request access.")
            form_name = st.text_input("Name")
            form_email = st.text_input("Email")
            form_note = st.text_area("Note about how you learned about this toolbox")

            # Submit button
            submitted = st.form_submit_button("Submit")
            if submitted:
                LOGGER.info("Submitted")

                # Set up email message
                msg = MIMEMultipart()
                msg['From'] = st.secrets['EMAIL_SENDER']
                msg['To'] = st.secrets['EMAIL_RECIPIENT']
                msg['Subject'] = 'Origin46 - AI Lab New Access Request'

                body = f"Name: {form_name}\nEmail: {form_email}\nMessage: {form_note}"
                msg.attach(MIMEText(body, 'plain'))

                # Send email
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.starttls()
                    smtp.login(
                        st.secrets['EMAIL_SENDER'],
                        st.secrets['EMAIL_PASSWORD']
                    )
                    smtp.send_message(msg)

                st.success(
                    "Your request has been submitted. You will receive an email "
                    "once your request has been approved."
                )


if __name__ == '__main__':
    app()
