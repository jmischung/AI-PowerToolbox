"""
pages_list.py - Defines a list of Page objects for use in the sidebar of the application.

This module defines a list of Page objects that represent the pages in the application. The list is
used to set the sidebar in the main application window. The list can be easily updated by modifying
the Page objects in this file.

Example usage:
    from utils.pages_list import sidebar_pages
    from st_pages import show_pages

    # Set sidebar
    show_pages(sidebar_pages)
"""
from st_pages import Page

# Set sidebar
sidebar_pages = [
    Page("pages/home.py", "Home", icon="🏠"),
    Page("pages/audio_transcriber.py", "Audio Transcriber", icon="🎤"),
    Page("pages/video_summarizer.py", "Video Summarizer", icon="🎥")
]
