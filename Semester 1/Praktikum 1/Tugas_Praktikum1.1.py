fahrenheit = 0
reamur = 0
kelvin = 0

celcius = int(input("Masukkan Celcius = "))

fahrenheit = (celcius * 9 / 5) + 32
print(celcius,"°C = ",float("{:.2f}".format(fahrenheit)),"°F (Fahrenheit)")

reamur = (4/5)*celcius
print(celcius, "°C = ", float("{:.2f}".format(reamur)), "R (Reamur)")

kelvin = celcius + 273.15
print(celcius, "°C = ", kelvin, "K (Kelvin)")

