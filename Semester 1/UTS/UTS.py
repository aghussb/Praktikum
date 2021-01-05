jawab = 'y'
print()
while jawab == 'y':
    print("Pilih Kendaraan :")
    print("1 - Motor")
    print("2 - Mobil")
    inputMenu = int(input("Masukkan Jenis Kendaraan = "))

    while inputMenu != 1 and inputMenu != 2:
        print("Pilihan Tidak Valid")
        inputMenu = int(input("Masukkan Jenis Kendaraan = "))

    if inputMenu == 1:
        inputJam = int(input("Berapa jam kendaraan diparkir = "))
        if inputJam == 1 or inputJam == 2:
            print("Biaya Parkir : 3000")
        else:
            if inputJam >= 24:
                dendaHarian = ((inputJam - (inputJam % 24)) / 24) * 100000
            else:
                dendaHarian = 0
            hasil = (inputJam - 2) * 2000 + dendaHarian + 3000
            print("Biaya Parkir :", int(hasil))

    elif inputMenu == 2:
        inputJam = int(input("Berapa jam kendaraan diparkir = "))
        if inputJam == 1 or inputJam == 2:
            print("Biaya Parkir : 3000")
        else:
            if inputJam >= 24:
                dendaHarian = ((inputJam - (inputJam % 24)) / 24) * 100000
            else:
                dendaHarian = 0
            hasil = (inputJam - 2) * 4000 + dendaHarian + 3000
            print("Biaya Parkir :", int(hasil))

    jawab = str(input("Ulangi lagi? (y/t) = "))
    print()

print("Terima Kasih")