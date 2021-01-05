phi = 3.14

luasKerucut = float(input("Masukkan Luas Kerucut = "))
garisPelukis = float(input("Masukkan Garis Pelukis Kerucut = "))

jariJari = luasKerucut / (phi*garisPelukis)
print("Jari - jari Kerucut tersebut adalah =",jariJari)

print("Menghitung Volume Kerucut")
tinggiKerucut = int(input("Masukkan Tinggi Kerucut = "))
volumeKerucut = (phi*(jariJari**2)*tinggiKerucut)/3

literKerucut = volumeKerucut / 1000

print("Maka volume air tersebut = ", float("{:.2f}".format(literKerucut)),"liter")
