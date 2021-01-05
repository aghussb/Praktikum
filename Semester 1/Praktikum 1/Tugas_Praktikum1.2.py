a = 5
b = 2

n = int(input("Masukkan Suku ke-n = "))
Un = a + (n-1) * b

Sn = (n/2) * (a + Un)
print("Jadi Suku ke-",n,"barisan aritmatika tersebut adalah =",Un)
print("dan jumlah suku ke-",n,"barisan aritmatika tersebut adalah = ",int(Sn))