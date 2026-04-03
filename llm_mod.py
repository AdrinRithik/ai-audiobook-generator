

import google.genai as genai
import streamlit as st

API=st.secrets[API]

client = genai.Client(api_key=API)
def enhance_text(text):
   response=client.models.generate_content(
       model="gemini-2.5-flash",
       contents=f"Rewrite the text in a clean and engaging audiobook narration style:\n{text}"
   )
   return response.text
def expressed_text(texts,expression):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Rewrite the text in a {expression} mode without any emoji:\n{texts}"
    )
    return response.text