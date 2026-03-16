import streamlit as st
import google.generativeai as genai

st.title("🤖 Gemini AI Chatbot")

# configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# latest Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# input box
user_input = st.text_input("Ask anything")

# response
if user_input:
    try:
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(e)
