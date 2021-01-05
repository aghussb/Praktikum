nama  = str(input("Masukkan Nama "))
nim  = int(input("Masukkan NIM "))

uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))

hitungRataRata = (uts+uas)/2

if int(hitungRataRata) <= 40:
    nilai = 'E'
elif int(hitungRataRata) <= 60:
    nilai = 'D'
elif int(hitungRataRata) <= 70:
    nilai = 'C'
elif int(hitungRataRata) <= 80:
    nilai = 'B'
elif int(hitungRataRata) <= 100:
    nilai = 'A'

print("Nama :",nama)
print("NIM :",nim)
print("Nilai rata-rata anda",int(hitungRataRata))
print("Anda mendapatkan Nilai",nilai)