import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# UI - Header
st.markdown("<h3 style='text-align: center; color: green;'>Enter YouTube Video Link Below</h3>", unsafe_allow_html=True)

# Input - YouTube Link
youtube_link = st.text_input("YouTube Link")

# Thumbnail Preview
if youtube_link:
    try:
        video_id = youtube_link.split("v=")[1].split("&")[0]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    except IndexError:
        st.error("Please provide a valid YouTube link (e.g., https://www.youtube.com/watch?v=VIDEO_ID)")

# Prompt Template
prompt = """You are a YouTube video summarizer. You will be taking the transcript text 
and summarizing the entire video and providing the important summary in points within 
900 words. Please provide the summary of the text given here: """

# Function: Extract Transcript
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t["text"] for t in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"An error occurred while extracting transcript: {e}")
        return None

# Function: Find Suitable Gemini Model
def find_suitable_gemini_model():
    try:
        preferred_models = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro", "gemini-1.0-pro"]

        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)

        for p_model in preferred_models:
            for a_model in available_models:
                if p_model in a_model:
                    return a_model  # Full name like 'models/gemini-1.5-flash'

        if available_models:
            return available_models[0]

        st.error("No suitable Gemini model found that supports 'generateContent'.")
        return None
    except Exception as e:
        st.error(f"Error listing Gemini models: {e}. Please check your API key and internet connection.")
        return None

# Function: Generate Summary
def generate_gemini_content(transcript_text, prompt):
    model_name = find_suitable_gemini_model()
    if not model_name:
        return None

    # st.info(f"Using Gemini model: {model_name}")

    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating summary with {model_name}: {e}")
        return None

# Main Action Button
if st.button("Get Detailed Notes"):
    if not youtube_link:
        st.error("Please enter a YouTube link before getting notes.")
    else:
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            if summary:
                st.markdown("## 📄 Detailed Notes:")
                st.write(summary)

# Footer
footer = '''
<div style="text-align: center; margin-top: 50px;">
    <hr style="border-top: 1px solid #ccc;">
    <p style="color: #666; font-size: 0.9em;">Developed with ❤️ by <strong>Anindya Maity</strong></p>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)
