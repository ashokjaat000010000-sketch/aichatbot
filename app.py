import streamlit as st
import google.generativeai as genai

st.title("🤖 AI Chatbot")

# configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# working Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

user_input = st.text_input("Ask something")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
