print("Program menghitung luas dan volume kerucut")
"""
Programmer : Mutiara uhti amelia
Pertemuan : 1
Tanggal : 22 oktober 2023
"""
# Nilai
jari_jari = 7
s = 20
phi = 3.14
tinggi = 30

# Rumus
luas_selimut = (phi*jari_jari*s)
luas_permukaan = (phi*jari_jari*s) + (phi*jari_jari)
volume = (phi*jari_jari*jari_jari*tinggi) / 3 

#Output
print("Jari-jari:", jari_jari)
print("S:", s)
print("Phi:", phi)
print("Tinggi:", tinggi)

print("Luas selimut:", luas_selimut)
print("Luas permukaan:", luas_permukaan)
print("Volume:", volume)
