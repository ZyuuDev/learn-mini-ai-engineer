import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("=== GENERATOR ALASAN TELAT ===")
tujuan = input("telat ke mana kamu? (sekolah/kerja/main): ")
gaya = input("Gaya alasannya mau kaya gimana nih? (dramatis/ilmiah/absurd): ")

prompt = f"Buatkan 1 alasan telat ke {tujuan} dengan gaya bahasa {gaya} maks 3 kalimat, dlam bahasa Indonesia, dan harus lucu pokoknya."

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "Kamu adalah ahli pembuat alasan kreatif yg tidak menyakiti siapapun."},
        {"role": "user", "content": prompt},
    ],
    temperature=1
)

print("\n ALASANNYA: ")
print(response.choices[0].message.content)