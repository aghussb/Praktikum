import locale

def formatRupiah(angka):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format_string("%.*f", (0, angka), True)
    return "Rp. "+rupiah


inputNama = str(input("Masukkan Nama : "))
inputNIM = str(input("Masukkan NIM : "))

dataMenu  = [
    {"nama":"Nasi Goreng","harga":10000},
    {"nama":"Nasi Kuning","harga":13000},
    {"nama":"Nasi Pecel","harga":5000},
    {"nama":"Es Jeruk","harga":4000},
    {"nama":"Es Teh","harga":3000},
]

dataPesanan = []

print("Halo, ",inputNama)
print("ingin pesan apa kamu hari ini?")
ulangMenu = True
while ulangMenu == True:

    print("----------------------------------")
    print("\nMenu")
    print("----------------------------------")
    print("{:<6} {:<15} {:<15}".format('No', 'Nama Menu', 'Harga'))
    for idx, itemMenu in enumerate(dataMenu):
        print("{:<6} {:<15} {:<15}".format(idx+1, itemMenu['nama'],formatRupiah(itemMenu['harga'])))
    print("----------------------------------")
    print("0. Checkout")
    print("----------------------------------")

    inputMenu = int(input("Pilih pesanan anda = "))

    if inputMenu == 0:
        ulangMenu = False
    else:
        inputPorsi = int(input("Berapa porsi yang anda pesan? "))
        objMenu = dataMenu[inputMenu-1]
        objMenu['porsi'] = inputPorsi
        objMenu['total_harga'] = objMenu['harga'] * inputPorsi

        for idx,itemPesanan in enumerate(dataPesanan):
            if itemPesanan['nama'] == objMenu['nama']:
                del dataPesanan[idx]

        dataPesanan.append(objMenu)

print("----------------------------------")
print("Pesanan Anda")
totalBayar = 0
for idx, itemPesanan in enumerate(dataPesanan):
    print("Pesanan ke-",idx+1,'=',itemPesanan['porsi'],itemPesanan['nama'],formatRupiah(itemPesanan['total_harga']))
    totalBayar += itemPesanan['total_harga']

print("Total pembayaran adalah ",formatRupiah(totalBayar),'\n')

diskon = 0
fakultas = ''
prodi = ''

if inputNIM[3:7] == "4411" :
     diskon =  0.25
     fakultas = 'Teknik'
     prodi = 'Sistem Informasi'
elif inputNIM[3:7] == "4111" :
     diskon =  0.1
     fakultas = 'Teknik'
     prodi = 'Teknik Informatika'
elif inputNIM[2:7] == "4211" :
     diskon =  0.1
     fakultas = 'Teknik'
     prodi = 'Teknik Industri'
elif inputNIM[3:7] == "4311" :
     diskon =  0.1
     fakultas = 'Teknik'
     prodi = 'Teknik Elektro'
elif inputNIM[3:7] == "4811" :
     diskon =  0.1
     fakultas = 'Teknik'
     prodi = 'Teknik Mesin'
elif inputNIM[3:7] == "4911" :
     diskon =  0.1
     fakultas = 'Teknik'
     prodi = 'Teknik Mekatro'
elif inputNIM[3:7] == "2211":
     fakultas = 'Ekonomi'
     prodi = 'Akuntansi'
elif inputNIM[3:7] == "2311":
     fakultas = 'Ekonomi'
     prodi = 'Ekonomi Pembangunan'
elif inputNIM[3:7] == "2111":
     fakultas = 'Ekonomi'
     prodi = 'Manajemen'
elif inputNIM[3:7] == "1111":
     fakultas = 'Hukum'
     prodi = 'Ilmu Hukum'
elif inputNIM[3:7] == "7211":
     fakultas = 'ISIB'
     prodi = 'Ekonomi Syariah'
elif inputNIM[3:7] == "7111":
     fakultas = 'ISIB'
     prodi = 'Hukum Bisnis Syariah'
elif inputNIM[3:7] == "5311":
     fakultas = 'ISIB'
     prodi = 'Ilmu Komunikasi'
elif inputNIM[3:7] == "6211":
     fakultas = 'ISIB'
     prodi = 'Pendidikan Bahasa dan Sastra Indonesia'
elif inputNIM[3:7] == "6511":
     fakultas = 'ISIB'
     prodi = 'Pendidikan Guru Anak Usia Dini'
elif inputNIM[3:7] == "6411":
     fakultas = 'ISIB'
     prodi = 'Pendidikan Ilmu Pengetahuan Alam'
elif inputNIM[3:7] == "6311":
     fakultas = 'ISIB'
     prodi = 'Pendidikan Informatika'
elif inputNIM[3:7] == "6111":
     fakultas = 'ISIB'
     prodi = 'PGSD'
elif inputNIM[3:7] == "5411":
     fakultas = 'ISIB'
     prodi = 'Psikologi'
elif inputNIM[3:7] == "5111":
     fakultas = 'ISIB'
     prodi = 'Sastra Inggris'
elif inputNIM[3:7] == "5211":
     fakultas = 'ISIB'
     prodi = 'Sosiologi'
elif inputNIM[3:7] == "3211":
     fakultas = 'Pertanian'
     prodi = 'AGRIBISNIS'
elif inputNIM[3:7] == "3111":
     fakultas = 'Pertanian'
     prodi = 'AGROEKOTEKNOLOGI'
elif inputNIM[3:7] == "3411":
     fakultas = 'Pertanian'
     prodi = 'Ilmu Kelautan'
elif inputNIM[3:7] == "3311":
     fakultas = 'Pertanian'
     prodi = 'Teknologi Industri Pertanian'

print("Anda mahasiswa Fakultas : ",fakultas)
print("Anda mahasiswa Prodi : ", prodi)

if diskon != 0:
    print("Anda Mahasiswa",prodi,"sehingga mendapat diskon",str(int(diskon*100))+'%')
    print("Harga setelah diskon adalah Rp. ",totalBayar-(totalBayar*diskon))

inputPembayaran = int(input("Masukkan jumlah uang yang anda bayarkan : "))
while inputPembayaran < totalBayar-(totalBayar*diskon):
    print("Uang anda kurang")
    inputPembayaran = int(input("Masukkan jumlah uang yang anda bayarkan : "))
print("Total uang yang anda bayarkan",formatRupiah(inputPembayaran))
print("Kembalian anda adalah Rp.",inputPembayaran-(totalBayar-(totalBayar*diskon)))
print("Terima Kasih")
