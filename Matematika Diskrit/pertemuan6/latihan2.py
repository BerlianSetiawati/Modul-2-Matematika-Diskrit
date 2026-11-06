# --- Fungsi Analisis Dasar ---
def adalah_genap(n):
    return n % 2 == 0

def adalah_prima(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# --- Fungsi Konversi Basis Bilangan ---
def desimal_ke_biner(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 2) + hasil
        n //= 2
    return hasil

def desimal_ke_oktal(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 8) + hasil
        n //= 8
    return hasil

def desimal_ke_hex(n):
    if n == 0:
        return "0"
    digit_hex = "0123456789ABCDEF"
    hasil = ""
    while n > 0:
        sisa = n % 16
        hasil = digit_hex[sisa] + hasil
        n //= 16
    return hasil


# ============================================================
# Program Utama (Menerima Input Pengguna)
# ============================================================
if __name__ == "__main__":
    nama_perangkat = input("Masukkan nama perangkat: ")
    id_input = int(input("Masukkan ID perangkat  : "))

    # Memproses analisis
    genap = adalah_genap(id_input)
    prima = adalah_prima(id_input)
    biner = desimal_ke_biner(id_input)
    oktal = desimal_ke_oktal(id_input)
    heks  = desimal_ke_hex(id_input)

    # Menampilkan Tabel Hasil Analisis
    print("\n" + "=" * 70)
    print(f"{'Nama':<14} {'ID':>5} {'Genap?':>7} {'Prima?':>7} {'Biner':>12} {'Oktal':>6} {'Hex':>6}")
    print("=" * 70)
    print(f"{nama_perangkat:<14} {id_input:>5} {str(genap):>7} {str(prima):>7} {biner:>12} {oktal:>6} {heks:>6}")
    print("=" * 70)

    # Verifikasi dengan Fungsi Bawaan Python
    print("\nVerifikasi fungsi bawaan Python:")
    print(f"  bin() -> {bin(id_input)}")
    print(f"  oct() -> {oct(id_input)}")
    print(f"  hex() -> {hex(id_input).upper()}")