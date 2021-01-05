jawab = 'y'

def operatorTambah(angka1,angka2):
    return angka1+angka2

def operatorKurang(angka1,angka2):
    return angka1 - angka2

def operatorBagi(angka1,angka2):
    return angka1 / angka2

def operatorKali(angka1,angka2):
    return angka1 * angka2

while jawab == 'y':
    angkaPertama = int(input("Masukkan Angka Pertama = "))
    angkaKedua = int(input("Masukkan Angka Kedua = "))
    print()
    print("Pilih Operasi")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Bagi")
    print("4. Kali")
    inpuMenu = int(input("Masukkan Menu Operasi = "))

    while inpuMenu > 4:
        print("Menu tidak ada")
        inpuMenu = int(input("Masukkan Menu Operasi = "))

    if inpuMenu == 1:
        print(angkaPertama,'+',angkaKedua,'=',operatorTambah(angkaPertama,angkaKedua))
    elif inpuMenu == 2:
        print(angkaPertama,'-',angkaKedua,'=',operatorKurang(angkaPertama,angkaKedua))
    elif inpuMenu == 3:
        print(angkaPertama,'/',angkaKedua,'=',operatorBagi(angkaPertama,angkaKedua))
    elif inpuMenu == 4:
        print(angkaPertama,'*',angkaKedua,'=',operatorKali(angkaPertama,angkaKedua))

    jawab = str(input("Ingin mengulang?(y/n) "))