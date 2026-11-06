def desimal_ke_biner(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        sisa = n % 2
        hasil = str(sisa) + hasil
        n = n // 2
    return hasil

bilangan = [13, 64, 127, 200]

print("--- Konversi Desimal ke Biner---")
print("================================")
print(f"{'Desimal':<10} {'Biner':>10}")

for n in bilangan:
    biner = desimal_ke_biner(n)

    print(f"{n:<10} {(biner):>10}")