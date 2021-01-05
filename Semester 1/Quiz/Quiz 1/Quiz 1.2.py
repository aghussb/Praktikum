inputRow = int(input("Masukkan ukuran segitiga : "))
inputRow = (inputRow*2)-1
for x in range(inputRow):
    for y in range(inputRow):
        if x == 0 or x == (inputRow-1):
            print('*', end="")
        elif x == y or x + y==inputRow-1:
            print('*',end="")
        else:
            print(" ",end="")
    print()

for x in range(inputRow):
    for y in range(inputRow):
        if x == (inputRow-1):
            print('*', end="")
        elif x == y or x + y==inputRow-1:
            print('*',end="")
        else:
            print(" ",end="")
    print()
