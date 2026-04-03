import streamlit as st

from extractor import extract_text
from llm_mod import enhance_text
from llm_mod import expressed_text
from tts_mod import text_to_speech
from tts_mod import generate_audio

USE_LLM = True

st.title("🎧 AI Audiobook Generator (GeminiAI)")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    st.success("File uploaded successfully!")

    text = extract_text(uploaded_file)
    st.text_area("Extracted text",text,height=300)

    if st.button("Generate Audiobook"):

        with st.spinner("Processing..."):


            if USE_LLM:
                text = enhance_text(text)
                st.text_area("Modified text", text, height=300)


            audio_file = text_to_speech(text)


            st.audio(audio_file)


            with open(audio_file, "rb") as f:
                st.download_button(
                    "Download Audiobook",
                    f,
                    file_name="../../../../../infosys audiobook/audiobook.mp3"
                )







expression = st.selectbox(
    "Select Expression",
    ["Normal","Happy 😊", "Sad 😢", "Angry 😡", "Calm 😌", "Excited 🎉"]
)

# Chat-style input
texts = st.chat_input("Type your text here...")

if texts:
    st.chat_message("user").write(texts)


    # Call gTTS function from separate file
    audio_path = generate_audio(texts, expression)
    modified_text = generate_audio(texts, expression)


    st.text_area("LLM text", modified_text, height=300)

    st.chat_message("assistant").write("Here is your generated audio 🎧")

    # Play audio
    audio_file = open(audio_path, "rb")
    st.audio(audio_file.read(), format="audio/mp3")
    audio_file.close()