import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 AI Bot: Hello! Mujhse kuch bhi pucho. (bye likho exit ke liye)")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Bye bhai 👋")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user}
        ]
    )

    print("Bot:", response.choices[0].message.content)