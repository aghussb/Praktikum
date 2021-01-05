daftarBukuPelajaran = [
    {'no':1,'buku':'MTK'},
    {'no':2,'buku':'B. Indo'},
    {'no':3,'buku':'B. Inggirs'},
    {'no':4,'buku':'Fisika'},
    {'no':5,'buku':'Biologi'},
    {'no':6,'buku':'PPKN'},
    {'no':7,'buku':'Sejarah Indonesia'},
    {'no':8,'buku':'Pend. Agama Islam'},
    {'no':9,'buku':'Algoritma Pemrograman'},
    {'no':10,'buku':'B. jawa'},
]

daftarBukuCerita = [
    {'no':1,'buku':'kancil dan buaya'},
    {'no':2,'buku':'harimau sang raja'},
    {'no':3,'buku':'bawang putih dan bawang merah'},
    {'no':4,'buku':'sindera'},
    {'no':5,'buku':'rapunsel'},
    {'no':6,'buku':'putri tidur'},
    {'no':7,'buku':'sangkuriang'},
    {'no':8,'buku':'1001 malam'},
    {'no':9,'buku':'kisah nabi dan rosul'},
    {'no':10,'buku':'malin kundang'},
]

print("Daftar buku pelajaran")
print("{:<6} {:<15}".format('No', 'Nama Buku'))
for index,data in enumerate(daftarBukuPelajaran):
    print("{:<6} {:<15}".format(index+1, data['buku']))

print("\n")
print("Daftar buku cerita")
print("{:<6} {:<15}".format('No', 'Nama Buku'))
for index,data in enumerate(daftarBukuCerita):
    print("{:<6} {:<15}".format(index+1, data['buku']))

print("\n")

print("Hari Pertama")
ListBukuPelajaran = []
statusBukuPelajaran = 0
while statusBukuPelajaran < 3:
    inputBukuPelajaran = int(input("Pilih buku pelajaran : "))
    while inputBukuPelajaran > 10:
        print("Buku Pelajaran yang dipilih tidak ada")
        inputBukuPelajaran = int(input("Pilih buku pelajaran : "))
    statusBukuPelajaran += 1
    ListBukuPelajaran.append(daftarBukuPelajaran[inputBukuPelajaran-1]['buku'])

print('Buku pelajaran yang dipinjam =',', '.join(ListBukuPelajaran))

print("\nHari Berikutnya")
ListBukuCerita = []
statusBukuCerita = 0
while statusBukuCerita < 5:
    inputBukuCerita = int(input("Pilih buku cerita : "))
    while inputBukuCerita > 10:
        print("Buku Pelajaran yang dipilih tidak ada")
        inputBukuCerita = int(input("Pilih buku pelajaran : "))
    statusBukuCerita += 1
    ListBukuCerita.append(daftarBukuCerita[inputBukuCerita-1]['buku'])

print('Buku Cerita yang dipinjam =',', '.join(ListBukuCerita))

print("\nSetelah Seminggu")
statusBukuPelajaranBaru = 0
while statusBukuPelajaranBaru < 5:
    inputBukuPelajaranBaru = int(input("Pilih buku pelajaran : "))
    while inputBukuPelajaranBaru > 10:
        print("Buku pelajaran yang dipilih tidak ada")
        inputBukuPelajaranBaru = int(input("Pilih buku pelajaran : "))
    statusBukuPelajaranBaru += 1
    ListBukuPelajaran.append(daftarBukuPelajaran[inputBukuPelajaranBaru-1]['buku'])

del ListBukuPelajaran[2]
del ListBukuPelajaran[1]

print()
statusBukuCeritaBaru = 0
while statusBukuCeritaBaru < 2:
    inputBukuCeritaBaru = int(input("Pilih buku Cerita : "))
    while inputBukuCeritaBaru > 10:
        print("Buku Cerita yang dipilih tidak ada")
        inputBukuCeritaBaru = int(input("Pilih buku Cerita : "))
    statusBukuCeritaBaru += 1
    ListBukuCerita.append(daftarBukuCerita[inputBukuCeritaBaru-1]['buku'])

del ListBukuCerita[3]
del ListBukuCerita[2]
del ListBukuCerita[1]
print('\nBuku Pelajaran siska yang dipinjam saat ini =',', '.join(ListBukuPelajaran))
print('Buku Cerita siska yang dipinjam saat ini =',', '.join(ListBukuCerita))

