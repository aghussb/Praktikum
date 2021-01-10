from datetime import datetime

import getpass
import locale
import module

statusMasuk = True


def formatRupiah(angka):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format_string("%.*f", (0, angka), True)
    return "Rp. " + rupiah


while statusMasuk:
    print("\n1. Login")
    print("2. Register")

    inputMenu = int(input("Masukkan Menu = "))

    while inputMenu != 1 and inputMenu != 2:
        print("Menu tidak valid")
        inputMenu = int(input("Masukkan Menu = "))

    authMod = module.module("user")
    produkMod = module.module("produk")
    laporanMod = module.module("laporan")
    while inputMenu == 1 or inputMenu == 2:
        if inputMenu == 1:
            print("\nLogin")
            inputUsername = str(input("Masukkan Username = "))
            inputPassword = getpass.getpass(prompt="Masukkan Password = ")

            statusLogin = False
            statusLogout = False
            dataLogin = {}
            pilihanRegister = 't'
            for dataUser in authMod.dataRead():
                if dataUser['username'] == inputUsername and dataUser['password'] == inputPassword:
                    dataLogin = dataUser
                    statusLogin = True
                    pilihanRegister = 't'

            if statusLogin == False and statusLogout == False:
                print("Username atau Password salah")
                pilihanRegister = str(input("Tidak ada akun, Register? (y/n)"))

            if pilihanRegister == 'y':
                inputMenu = 2

            daftarBelanjaPembeli = []

            while statusLogin:
                if dataLogin['status'] == 1:
                    print("\nInfo Produk\n")
                    print("{:<6} {:<15} {:<10} {:<15}".format('No', 'Nama', 'Jumlah Beli', 'Jumlah Harga'))
                    for idx, dataProduk in enumerate(produkMod.dataRead()):
                        print("{:<6} {:<15} {:<10} {:<15}".format(idx + 1, dataProduk['nama'], dataProduk['stock'],
                                                                  formatRupiah(dataProduk['harga'])))

                    print("\nSelamat Datang", dataLogin['nama'])
                    print("\n1. Tambah Produk")
                    print("2. Ubah Produk")
                    print("3. Hapus Produk")
                    print("4. Laporan Belanja Pembeli")
                    print("5. Logout")
                    inputMenuData = int(input("Masukkan Menu = "))
                    while inputMenuData > 5:
                        print("Menu tidak valid")
                        inputMenuData = int(input("Masukkan Menu = "))

                    if inputMenuData == 1:
                        inputNamaProduk = str(input("Masukkan Nama Produk = "))
                        inputStockProduk = int(input("Masukkan Stock Produk = "))
                        inputHargaProduk = int(input("Masukkan Harga Produk = "))
                        dataProduk = {
                            "nama": inputNamaProduk,
                            "stock": inputStockProduk,
                            "harga": inputHargaProduk
                        }
                        print(produkMod.saveData(dataProduk, 1, 0))
                    elif inputMenuData == 2:
                        print("Info Produk\n")
                        print("{:<6} {:<15} {:<10} {:<10}".format('No', 'Nama', 'Stock', 'Harga'))

                        for idx, dataProduk in enumerate(produkMod.dataRead()):
                            print("{:<6} {:<15} {:<10} {:<10}".format(idx + 1, dataProduk['nama'], dataProduk['stock'],
                                                                      formatRupiah(dataProduk['harga'])))
                        inputProduk = int(input("\nMasukkan Nomor Produk = "))
                        while inputProduk > len(produkMod.dataRead()):
                            print("Produk tidak ada!!!")
                            inputProduk = int(input("Masukkan Nomor Produk = "))

                        inputStockProduk = int(input("Masukkan Stock Produk = "))
                        inputHargaProduk = int(input("Masukkan Harga Produk = "))
                        dataProduk = {
                            "stock": inputStockProduk,
                            "harga": inputHargaProduk
                        }
                        print(produkMod.saveData(dataProduk, 2, inputProduk))
                    elif inputMenuData == 3:
                        print("Info Produk\n")
                        print("{:<6} {:<15} {:<10} {:<10}".format('No', 'Nama', 'Stock', 'Harga'))

                        for idx, dataProduk in enumerate(produkMod.dataRead()):
                            print("{:<6} {:<15} {:<10} {:<10}"
                                  .format(idx + 1, dataProduk['nama'], dataProduk['stock'],
                                          formatRupiah(dataProduk['harga'])))
                        inputProduk = int(input("\nMasukkan Nomor Produk = "))
                        while inputProduk > len(produkMod.dataRead()):
                            print("Produk tidak ada!!!")
                            inputProduk = int(input("Masukkan Nomor Produk = "))
                        print(produkMod.deleteData(inputProduk))
                    elif inputMenuData == 4:
                        print()
                        print("{:<6} {:<15} {:<15} {:<15}".format('No', 'Tanggal', 'Jam', 'Jumlah Uang'))
                        for idx, data in enumerate(laporanMod.dataRead()):
                            print("{:<6} {:<15} {:<15} {:<15}"
                                  .format(idx + 1, data['tanggal'], data['waktu'], formatRupiah(data['tunai'])))
                        print()
                        inputMenuLaporan = int(input("Masukkan Nomor Laporan = "))
                        while inputMenuLaporan > len(laporanMod.dataRead()):
                            print("Nomor Laporan Tidak Ada!!!")
                            inputMenuLaporan = int(input("Masukkan Nomor Laporan = "))
                        print()
                        print('-------------------------------------')
                        print('\t    INVEST MART')
                        print('=====================================')
                        print("{:<12} {:<15} {:<15}".format('Tgl.',
                                                            laporanMod.dataRead()[inputMenuLaporan - 1]['tanggal'],
                                                            laporanMod.dataRead()[inputMenuLaporan - 1]['waktu']))
                        print('=====================================')
                        jumlahStockBelanja = 0
                        jumlahHargaBelanja = 0
                        for idx, itemBelanja in enumerate(laporanMod.dataRead()[inputMenuLaporan - 1]['data']):
                            print("{:<16} {:<11} {:<15}".format(itemBelanja['nama'], itemBelanja['stock'],
                                                                formatRupiah(itemBelanja['harga'])))
                            jumlahStockBelanja += itemBelanja['stock']
                            jumlahHargaBelanja += itemBelanja['harga']

                        print('-------------------------------------')
                        print("{:<16} {:<11} {:<15}".format('Total Item', jumlahStockBelanja,
                                                            formatRupiah(jumlahHargaBelanja)))
                        print("{:<16} {:<11} {:<15}".format('Tunai', '', formatRupiah(
                            laporanMod.dataRead()[inputMenuLaporan - 1]['tunai'])))
                        print("{:<16} {:<11} {:<15}".format('Kembalian', '', formatRupiah(
                            laporanMod.dataRead()[inputMenuLaporan - 1]['tunai'] - jumlahHargaBelanja)))
                        print('=====================================')
                        print('TERIMA KASIH. SELAMAT BELANJA KEMBALI')
                        print('-------------------------------------')
                    elif inputMenuData == 5:
                        statusLogin = False
                        statusLogout = True
                        inputMenu = 3

                else:
                    print("\nInfo Produk\n")
                    print("{:<6} {:<15} {:<10} {:<10}".format('No', 'Nama', 'Stock', 'Harga'))
                    for idx, dataProduk in enumerate(produkMod.dataRead()):
                        print("{:<6} {:<15} {:<10} {:<10}"
                              .format(idx + 1, dataProduk['nama'], dataProduk['stock'],
                                      formatRupiah(dataProduk['harga'])))
                    print("\nSelamat Datang", dataLogin['nama'])
                    print("\nBelanja Pembeli\n")
                    print("{:<6} {:<15} {:<10} {:<10}".format('No', 'Nama', 'Stock', 'Harga'))
                    for idx, itemBelanja in enumerate(daftarBelanjaPembeli):
                        print("{:<6} {:<15} {:<10} {:<10}"
                              .format(idx + 1, itemBelanja['nama'], itemBelanja['stock'],
                                      formatRupiah(itemBelanja['harga'])))
                    print("\n1. Tambah Produk Belanja")
                    print("2. Hapus Produk Belanja")
                    print("3. Bayar Belanja")
                    print("4. Logout")
                    inputMenuData = int(input("Masukkan Menu = "))
                    while inputMenuData != 1 and inputMenuData != 2 and inputMenuData != 3 and inputMenuData != 4:
                        print("Menu tidak valid")
                        inputMenuData = int(input("Masukkan Menu = "))

                    if inputMenuData == 1:
                        mengulangTambahProduk = 'y'
                        while mengulangTambahProduk == 'y':
                            inputProdukBelanja = int(input("Masukkan Nomor Produk  = "))
                            while inputProdukBelanja > len(produkMod.dataRead()):
                                print("Produk Tidak Ada!!!")
                                inputProdukBelanja = int(input("Masukkan Nomor Produk  = "))

                            inputStockBelanja = int(input("Masukkan Jumlah Pembelian Produk  = "))
                            while inputStockBelanja > produkMod.dataRead()[inputProdukBelanja - 1]['stock']:
                                print("Jumlah melebihi stock!!!")
                                print("Stock di produk", produkMod.dataRead()[inputProdukBelanja - 1]['nama'], 'adalah',
                                      produkMod.dataRead()[inputProdukBelanja - 1]['stock'])
                                inputStockBelanja = int(input("Masukkan Jumlah Pembelian Produk  = "))

                            jumlahHargaProduk = inputStockBelanja * produkMod.dataRead()[inputProdukBelanja - 1][
                                'harga']

                            for idx, item in enumerate(daftarBelanjaPembeli):
                                if produkMod.dataRead()[inputProdukBelanja - 1]['nama'] == item['nama']:
                                    del daftarBelanjaPembeli[idx]

                            dictionaryProdukBelanja = {
                                "id": inputProdukBelanja - 1,
                                "nama": produkMod.dataRead()[inputProdukBelanja - 1]['nama'],
                                "stock": inputStockBelanja,
                                "harga": int(jumlahHargaProduk)
                            }
                            daftarBelanjaPembeli.append(dictionaryProdukBelanja)
                            mengulangTambahProduk = str(input("Ingin menambah produk lagi? (y/n) : "))
                    elif inputMenuData == 2:
                        inputNomorProduk = int(input("Masukkan Nomor Produk yang mau dihapus = "))
                        while inputNomorProduk > len(produkMod.dataRead()):
                            print("Produk Tidak Ada!!!")
                            inputNomorProduk = int(input("Masukkan Nomor Produk yang mau dihapus = "))

                        del daftarBelanjaPembeli[inputNomorProduk - 1]

                    elif inputMenuData == 3:
                        if len(daftarBelanjaPembeli) == 0:
                            print("\nBelanjaan Kosong!!!")
                        else:
                            jumlahHargaBelanja = 0
                            for item in daftarBelanjaPembeli:
                                jumlahHargaBelanja += item['harga']

                            inputUangPembeli = int(input("Masukkan Uang Pembeli = "))
                            while inputUangPembeli < jumlahHargaBelanja:
                                print("Uang kurang!!!")
                                inputUangPembeli = int(input("Masukkan Uang Pembeli = "))

                            print()
                            print('-------------------------------------')
                            print('\t    INVEST MART')
                            print('=====================================')
                            print("{:<12} {:<15} {:<15}".format('Tgl.', datetime.today().strftime('%d-%m-%Y'),
                                                                datetime.today().strftime('%H:%M:%S')))
                            print('=====================================')
                            jumlahStockBelanja = 0
                            for idx, itemBelanja in enumerate(daftarBelanjaPembeli):
                                print("{:<16} {:<11} {:<15}".format(itemBelanja['nama'], itemBelanja['stock'],
                                                                    formatRupiah(itemBelanja['harga'])))
                                jumlahStockBelanja += itemBelanja['stock']

                            print('-------------------------------------')
                            print("{:<16} {:<11} {:<15}".format('Total Item', jumlahStockBelanja,
                                                                formatRupiah(jumlahHargaBelanja)))
                            print("{:<16} {:<11} {:<15}".format('Tunai', '', formatRupiah(inputUangPembeli)))
                            print("{:<16} {:<11} {:<15}".format('Kembalian', '',
                                                                formatRupiah(inputUangPembeli - jumlahHargaBelanja)))
                            print('=====================================')
                            print('TERIMA KASIH. SELAMAT BELANJA KEMBALI')
                            print('-------------------------------------')
                            produkMod.simpanBelanja(daftarBelanjaPembeli, inputUangPembeli,
                                                    datetime.today().strftime('%d-%m-%Y'),
                                                    datetime.today().strftime('%H:%M:%S'))
                            daftarBelanjaPembeli = []
                    elif inputMenuData == 4:
                        statusLogin = False
                        statusLogout = True
                        inputMenu = 3

        elif inputMenu == 2:
            print("\nRegister")
            inputNama = str(input("Masukkan Nama = "))
            inputUsername = str(input("Masukkan Username = "))
            inputPassword = str(input("Masukkan Password = "))
            dataRegister = {
                "nama": inputNama,
                "username": inputUsername,
                "password": inputPassword,
                "status": 2
            }
            print(authMod.authSave(dataRegister))
            inputMenu = 1
