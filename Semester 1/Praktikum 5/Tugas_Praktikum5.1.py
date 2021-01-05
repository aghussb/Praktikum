List1 = []
List2 = []
List3 = []
List4 = []
List5 = [13,31,2,19,96]
statusList1 = 0
while statusList1 < 13:
    inputList1 = str(input("Masukkan hewan bersayap : "))
    statusList1 += 1
    List1.append(inputList1)
print()
statusList2 = 0
while statusList2 < 5:
    inputList2 = str(input("Masukkan hewan berkaki 2 : "))
    statusList2 += 1
    List2.append(inputList2)
print()
statusList3 = 0
while statusList3 < 5:
    inputList3 = str(input("Masukkan nama teman terdekat anda : "))
    statusList3 += 1
    List3.append(inputList3)
print()
statusList4 = 0
while statusList4 < 5:
    inputList4 = int(input("Masukkan tanggal lahir teman tersebut : "))
    statusList4 += 1
    List4.append(inputList4)
print(List1[0:5]+List4,'\n')
List3[4] = 'Rio'
print(List3,'\n')
tempList5 = List5.copy()
del tempList5[4]
del tempList5[2]
print(tempList5,'\n')
print(List4 + List5)
print("Nilai Max dari List 4 dan List 5 adalah",max(List4 + List5))
print("Nilai Min dari List 4 dan List 5 adalah",min(List4 + List5))