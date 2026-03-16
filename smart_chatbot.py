import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    try:
  model = genai.GenerativeModel("gemini-1.0-pro")
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(e)
