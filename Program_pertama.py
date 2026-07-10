import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=1,
    messages=[
        {"role": "system", "content": "Kamu adalah Furina istri Fairuz. semua jawaban wajib diakhiri sayang"},
        {"role": "user", "content": "Jelaskan apa itu AI dalam 2 kalimat, gaya santai"}
    ],
)

print(response.choices[0].message.content)