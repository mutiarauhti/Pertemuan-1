print("Program menghitung luas dan volume tabung")
"""
Programmer : Mutiara uhti amelia
Pertemuan : 1
Tanggal : 22 oktober 2023
"""
# Nilai
S_1 = 8
S_2 = 12
S_3 = 15 
T = 9
a = 7
t = 10 

# Rumus
keliling_segitiga = S_1 + S_2 + S_3 
luas_segitiga = keliling_segitiga * T
luas_prisma = keliling_segitiga * T + a * t 
volume = 1/2 * a * t * T 

# Output
print("Sisi 1:", S_1)
print("Sisi 2:", S_2)
print("Sisi 3:", S_3)
print("Tinggi prisma:", T)
print("Alas:", a)
print("Tinggi:", t)

print("Keliling segitiga:", keliling_segitiga)
print("Luas segitiga:", luas_segitiga)
print("Luas prisma:", luas_prisma)
print("Volume:", volume)