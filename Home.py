import streamlit as st


def app():
    """
    This function defines the home page of the Streamlit app.

    It sets the title of the page and displays some text. It also prompts the
    user to select a page from the sidebar.
    """
    st.title("Welcome to my AI-Powered Toolbx!")
    st.write("Select a tool from the sidebar to get started.")


if __name__ == '__main__':
    app()
