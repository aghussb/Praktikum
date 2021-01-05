def factorial(angka):
    if angka < 2:
        return 1
    else:
        return angka * factorial(angka-1)

inputAngka = int(input("Masukkan Angka = "))
print('Hasil dari Factorial',inputAngka,"adalah",factorial(inputAngka))
