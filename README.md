# AI PowerToolbox

This project is a multi-page Streamlit app that houses various tools built around OpenAI's GPT-4. The first tool is a video summarizer that takes a link to a YouTube or Vimeo video, extracts and transcribes the audio using OpenAI Whisper, and then uses GPT-4 to summarize the video.

## Installation

The project requires Python 3.11 and the following Python packages:

- `streamlit`
- `vimeo-downloader`
- `pytube3`

You will also need an OpenAI API key to use GPT-4 and Whisper.

To install the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/GPT4-VideoSummarizer.git
    ```

2. Navigate into the cloned repository:
    ```
    cd GPT4-VideoSummarizer
    ```

3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key as an environment variable:
    ```
    export OPENAI_API_KEY='your-api-key'
    ```

5. Run the Streamlit app:
    ```
    streamlit run app.py
    ```

Please note that this project is intended for personal use and is not officially associated with OpenAI, YouTube, or Vimeo.

Please replace `'your-api-key'` and `'yourusername'` with your actual OpenAI API key and GitHub username, respectively.
