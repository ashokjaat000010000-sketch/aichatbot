import streamlit as st
import google.generativeai as genai

# API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 AI Chatbot")

# user input
user_input = st.text_input("Type your question")

# button
if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
    else:
        st.write("Please type something")
