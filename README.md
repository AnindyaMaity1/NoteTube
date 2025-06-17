# 🎬 YouTube Video Summarizer App

This Streamlit app allows you to quickly summarize YouTube videos. It extracts the video transcript and uses Google's Gemini models to provide a detailed summary.

## 🚀 How to Use

1.  **Enter YouTube Link:** Paste the link of the YouTube video you want to summarize in the input box.
2.  **Get Detailed Notes:** Click the "Get Detailed Notes" button.
3.  **View Summary:** The app will display a detailed summary of the video's content.

## ⚙️ Setup Instructions

1.  **Install Dependencies:**
    ```bash
    pip install streamlit python-dotenv google-generativeai youtube-transcript-api
    ```
2.  **Set up Environment Variables:**
    * Create a `.env` file in the project directory.
    * Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY=YOUR_API_KEY
        ```
3.  **Run the App:**
    ```bash
    streamlit run your_script_name.py
    ```

## 📝 Code Overview

* **`import streamlit as st`**:  Imports the Streamlit library for creating the app's UI.
* **`from dotenv import load_dotenv`**: Loads environment variables from a `.env` file.
* **`import google.generativeai as genai`**: Imports the Google Generative AI library.
* **`import os`**: Used for accessing environment variables.
* **`from youtube_transcript_api import YouTubeTranscriptApi`**:  Used to extract transcripts from YouTube videos.
* **`extract_transcript_details(youtube_video_url)`**: Extracts the transcript from a given YouTube video URL.
* **`find_suitable_gemini_model()`**:  Finds a suitable Gemini model for generating content.
* **`generate_gemini_content(transcript_text, prompt)`**: Generates a summary of the transcript using the Gemini model.

## 👨‍💻 Developed By

**Anindya Maity**
