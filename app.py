import streamlit as st
import requests

st.title("🤖 Free AI Chatbot")

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

user_input = st.text_input("Ask something")

if user_input:
    output = query({
        "inputs": user_input
    })

    try:
        st.write(output[0]["generated_text"])
    except:
        st.write("Model is loading, please try again in a few seconds.")
