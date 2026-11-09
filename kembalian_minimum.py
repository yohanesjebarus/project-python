
def kembalian_minimum(total):
    pecahan = [10000, 5000, 2000, 1000]
    hasil = {}

    if total < 0 or total % 1000 != 0:
        print("Nominal harus kelipatan Rp1.000!")
        return None

    for uang in pecahan:
        jumlah = total // uang

        if jumlah > 0:
            hasil[uang] = jumlah
            total = total % uang

    return hasil


total = int(input("Masukkan nominal kembalian: Rp"))

hasil = kembalian_minimum(total)

if hasil is not None:
    print("\nRincian kembalian:")
    jumlah_lembar = 0

    for uang, jumlah in hasil.items():
        print(f"Rp{uang:,} : {jumlah} lembar")
        jumlah_lembar += jumlah

    print("Total lembar uang:", jumlah_lembar)
