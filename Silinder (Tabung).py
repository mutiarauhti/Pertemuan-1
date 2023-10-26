print("Program menghitung luas dan volume tabung")
"""
Programmer : Mutiara uhti amelia
Pertemuan : 1
Tanggal : 22 oktober 2023
"""
# Nilai
tinggi = 15
jari_jari = 7
phi = 3.14

# Rumus
luas_selimut = 2 * (phi*jari_jari*tinggi)
luas_permukaan = 2 * (phi*jari_jari*tinggi) + 2 * (phi*jari_jari*jari_jari)
volume = (phi*jari_jari*jari_jari*tinggi)

# Output 
print("Tinggi:", tinggi)
print("Jari-jari:", jari_jari)
print("Phi:", phi)

print("Luas Selimut:", luas_selimut)
print("Luas permukaan:", luas_permukaan)
print("Volume:", volume)
