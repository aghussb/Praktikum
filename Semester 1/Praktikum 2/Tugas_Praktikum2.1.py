umur = int(input("Masukkan Umur = "))

while umur <= 7:
    print("Silakan Coba Lagi")
    umur = int(input("Masukkan Umur = "))

if umur >= 50:
    hasilUmur = 'Tua'
elif umur >= 25:
    hasilUmur = 'Muda'
elif umur >= 17:
    hasilUmur = 'Dewasa'
elif umur >= 7:
    hasilUmur = 'Anak - anak'


print("Umur",umur," = ",hasilUmur)