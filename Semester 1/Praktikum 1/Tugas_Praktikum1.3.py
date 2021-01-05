kata = "SISTEM INFORMASI"

kataJoin = ''.join(kata.split())
jumlahKata = len(list(set(list(kataJoin))))

panjangKata = 5

print("Jumlah huruf kata pada ",kata," =",jumlahKata)
print("dengan panjang kata =",panjangKata,"huruf")

hasilKurang = jumlahKata - panjangKata

import math

faktorJumlahKata = math.factorial(jumlahKata)
faktorHasilKurang = math.factorial(hasilKurang)
hasilKata = faktorJumlahKata / faktorHasilKurang
print("Jadi banyak kata yang dapat disusun dari",kata,"adalah =",int(hasilKata),"kata")