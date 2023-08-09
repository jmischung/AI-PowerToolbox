import os
import openai
import streamlit as st
from pytube import YouTube

# Set OpenAI API key
openai.api_key = st.secrets


def get_audio_youtube(url):
    # Fetch YouTube video
    yt = YouTube(url)

    # Get medium quality audio stream (assuming a middle bitrate represents "medium" quality)
    audio_streams = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr')
    medium_quality_stream = audio_streams[len(audio_streams) // 2]

    # Download the audio stream
    medium_quality_stream.download(filename='./temp/audio.mp4')


def transcribe_audio(audio_file_path):
    # Transcribe audio
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", file=audio_file)

    # Delete audio file
    os.remove(audio_file_path)

    return transcription['text']
