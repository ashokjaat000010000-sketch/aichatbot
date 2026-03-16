import streamlit as st
import google.generativeai as genai
import os

# API key configure
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
