import streamlit as st
import google.generativeai as genai

# API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model
model = genai.GenerativeModel("gemini-pro")

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
