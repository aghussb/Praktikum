Tuple1 = ()
Tuple2 = (10,30,45,21,12,13,31,90)
Tuple3 = ('pRaktikum', 'praktikum', 'Praktikum', 'PraKtIkuM', 'PRAKTIKUM')

List1 = list(Tuple1)
List2 = list(Tuple2)
List3 = list(Tuple3)

statusTuple1 = 0
while statusTuple1 < 5:
    inputTuple1 = str(input("Masukkan nama kendaraan : "))
    statusTuple1 += 1
    List1.append(inputTuple1)

print(tuple(List3[1].split()+List3[3:5]+List1[4].split()+List1[2].split()))
print(tuple((str(List2[3]).split()+str(List2[5]).split()) * 3))