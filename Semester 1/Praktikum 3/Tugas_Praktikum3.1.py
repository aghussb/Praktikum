import math
size = int(input("Masukkan size = "))
print()
for deretHorizontal in range(size):
    for deretVertikal in range(size):
        if (deretVertikal == 0 or deretVertikal == (size - 1)) or (deretHorizontal == 0 or deretHorizontal == (size - 1)):
            print('0',end='')
        else:
            print(end=' ')
    print()
print()

for deretHorizontal in range(size):
    for deretVertikal in range(size):
        if deretVertikal == (size - 1) or deretHorizontal == 0 or deretHorizontal == (size - 1) \
                or deretHorizontal == math.ceil((size - 1) / 2) or (deretVertikal == 0 and  0<deretHorizontal<math.ceil((size - 1) / 2)):
            print('9',end='')
        else:
            print(end=' ')
    print()
print()

for deretHorizontal in range(size):
    for deretVertikal in range(size):
        if (deretVertikal == (size - 1) and  math.ceil((size - 1) / 2)<deretHorizontal<(size - 1)) \
                or deretHorizontal == 0 or deretHorizontal == (size - 1) or deretHorizontal == math.ceil((size - 1) / 2) \
                or (deretVertikal == 0 and  0<deretHorizontal<math.ceil((size - 1) / 2)):
            print('5',end='')
        else:
            print(end=' ')
    print()
print()