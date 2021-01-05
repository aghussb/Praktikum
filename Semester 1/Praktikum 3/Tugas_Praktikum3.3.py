jawab = 'y'
while jawab == 'y':
    hari = int(input("Masukkan Hari = "))
    if hari > 7:
        hitungHari = (hari-7) * 2000
        if hari >= 14:
            hitungMinggu = (((hari - (hari%7))/7)-1)*5000
        else:
            hitungMinggu = 0;
        hasilHitung = hitungHari + hitungMinggu
        print("Anda meminjam buku selama",hari,"hari, dan dikenai denda sebesar",round(hasilHitung))
    else:
        print("Buku dikembalikan")
    jawab = str(input("Menghitung lagi atau tidak (y/n) = "))

print("Terima Kasih")