import streamlit as st
import google.generativeai as genai

# API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# model
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
