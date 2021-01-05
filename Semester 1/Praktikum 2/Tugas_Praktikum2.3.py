dataNilai = [
    {'nama': 'Jaka', 'ipk': 3.5, 'skor': 1100},
    {'nama': 'Ida', 'ipk': 3.5, 'skor': 1000}
]

mahasiswaYangLulus = []

print("Mahasiswa yang lulus persyaratan beasiswa dengan minimal IPK 3.0 dan skor yang lebih besar dari 1100 ialah :")

for data in dataNilai:
    if data['ipk'] >= 3.0 and data['skor'] > 1100:
        mahasiswaYangLulus.append(data['nama'])


if len(mahasiswaYangLulus) == 0:
    print("Tidak ada yang lulus")
else:
    print(','.join(mahasiswaYangLulus))