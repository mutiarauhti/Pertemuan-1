print("Program menghitung luas dan volume limas segi empat")
"""
Programmer : Mutiara uhti amelia
Pertemuan : 1
Tanggal : 22 oktober 2023
"""
# Nilai
alas = 10
tinggi = 15
sisi_tegak = 12 

# Rumus 
luas_alas = alas*alas
luas_sisi_tegak = 4*(alas * sisi_tegak) / 2
luas = luas_alas + luas_sisi_tegak
volume = (luas_alas * tinggi) / 3

# output 
print("Alas:", alas)
print("Tinggi:", tinggi)
print("Sisi tegak:", sisi_tegak)

print("Luas:", luas)
print("Volume:", volume)

