import streamlit as st
import requests

st.title("🤖 Fast Free AI Chatbot")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

def query(payload):
    response = requests.post(
        API_URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    return response.json()

user_input = st.text_input("Ask anything")

if user_input:
    with st.spinner("Thinking..."):
        output = query({
            "inputs": user_input,
            "options": {"wait_for_model": True},
            "parameters": {
                "max_new_tokens": 60,
                "temperature": 0.7
            }
        })

    try:
        st.write(output[0]["generated_text"])
    except:
        st.write("Please try again.")
