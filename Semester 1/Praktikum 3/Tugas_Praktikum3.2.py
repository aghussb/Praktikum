nilai = int(input("Masukkan Nilai = "))
bilanganPrima = []

for i in range(1,nilai+1):
    statusPrima = 0
    for j in range(1,i+1):
        if i % j == 0:
            statusPrima = statusPrima+1
    if statusPrima == 2:
        bilanganPrima.append(str(i))

print("Bilangan Prima dari nilai",nilai,"adalah",','.join(bilanganPrima))