import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )

    st.write(response.choices[0].message.content)
