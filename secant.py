# Mencari nilai fxnol dan fxsatu
nilx1 = float(input("Masukkan nilai x yang ke satu = "))
fxnol = float(nilx1 ** 3 + 2 * nilx1 ** 2 + 10 * nilx1 - 20)
print("Hasil fx ke satu adalah ", fxnol)
nilx2 = float(input("Masukkan nilai x yang ke dua = "))
fxsatu = float(nilx2 ** 3 + 2 * nilx2 ** 2 + 10 * nilx2 - 20)
print("Hasil fx ke dua adalah ", fxsatu)

# Menuju rumus
nilxr = float(input("Masukkan nilai Xr = "))
nilxnol = float(input("Masukkan nilai xr sebelumnya = "))
nilxsatu = float(input("Masukkan nilai xr sekarang= "))
hasil = float(nilxr - (fxsatu * (nilxsatu - nilxnol) / (fxsatu - fxnol)))
print("=======================================================")
print(f"Hasil nya nilai xr {hasil}")
print("=======================================================")
hasil2 = abs(hasil - nilxr)
e = 0.00001
print("Hasil dari xr + 1 - xr = ", hasil2)
print("======================================")
if hasil2 < e:
    print("sudah lebih kecil dari epsilon")
else:
    print("belum lebih kecil dari epsilon")

