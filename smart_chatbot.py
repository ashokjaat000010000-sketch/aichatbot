import streamlit as st
import google.generativeai as genai

# API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# latest Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
