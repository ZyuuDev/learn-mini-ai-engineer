print("Hello World")
print("Aku lagi belajar AI Engineer anjay\n\n")

nama = "ZyuuDev"
umur = "18"
tinggi = "168.8"
hobi = "ngoding"
sedang_belajar = True
print(nama)
print(umur)
print(tinggi)
print(sedang_belajar)
print("\n")

kalimat = f"Halo namaku {nama} dan aku suka {hobi}!"
print(kalimat)

belanjaan = ["indomie", "kopi", "telur"]
print(belanjaan)
print(belanjaan[0])
print(len(belanjaan))
belanjaan.append("matcha")
print(belanjaan)

siswa = {
    "nama": "fairuz",
    "kelas": "XII",
    "jurusan": "RPL"
}
print(siswa["nama"])
siswa["hobi"] = "coding"
print(siswa)

pesan = "harga"
if pesan == "harga":
    print("Harganya seket ewu kak")
elif pesan == "stok":
    print("stok masi banyaaaq")
else:
    print("maaf aku gak paham maksudnya")

buah = ["mangga", "melon", " semangka"]
for item in buah:
    print(f"aku suka banget sama {item}")

while True:
    jawab = input("ketik 'stop untuk berhenti: ")
    if jawab == "stop":
        break

def sapa(nama):
    hasil = f"halo {nama}, selamat sinau!"
    return hasil

pesan1 = sapa("zyuudev")
pesan2 = sapa("Fairuz")
print(pesan1)
print(pesan2)