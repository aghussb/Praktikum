inputRow = int(input("Masukkan Angka : "))

for x in range(1, inputRow+1):
    for y in range(1, x + 1):
        print(x * y, end=" ")
    print()
