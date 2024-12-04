import math
import time
# WAssap
# Fungsi untuk mencari panjang Persegi Panjang
def cari_panjang_persegi_panjang(lebar, luas, keliling):
    if lebar is not None and luas is not None:
        return round(luas / lebar, 2)
    elif keliling is not None and lebar is not None:
        return round((keliling / 2) - lebar, 2)
    elif keliling is not None and luas is not None:
        lebar = keliling / 2 - (luas / (keliling / 2))
        return round(lebar, 2)
    return "Data tidak lengkap"

# Fungsi untuk mencari lebar Persegi Panjang
def cari_lebar_persegi_panjang(panjang, luas, keliling):
    if panjang is not None and luas is not None:
        return round(luas / panjang, 2)
    elif keliling is not None and panjang is not None:
        return round((keliling / 2) - panjang, 2)
    elif keliling is not None and luas is not None:
        panjang = keliling / 2 - (luas / (keliling / 2))
        return round(panjang, 2)
    return "Data tidak lengkap"

# Fungsi untuk mencari sisi Persegi
def cari_sisi_persegi(luas, keliling):
    if luas is not None:
        return round(math.sqrt(luas), 2)
    elif keliling is not None:
        return round(keliling / 4, 2)
    return "Data tidak lengkap"

# Fungsi untuk mencari radius Lingkaran
def cari_radius_lingkaran(luas, keliling):
    if luas is not None:
        return round(math.sqrt(luas / math.pi), 2)
    elif keliling is not None:
        return round(keliling / (2 * math.pi), 2)
    return "Data tidak lengkap"

# Fungsi untuk memastikan input adalah angka yang valid
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Angka tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Input tidak valid, harap masukkan angka.")

# Fungsi utama untuk memilih bentuk dan melakukan perhitungan
def main():
    while True:
        print("\nPilih bentuk yang ingin dihitung:")
        print("1. Persegi Panjang")
        print("2. Persegi")
        print("3. Lingkaran")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            print("\nMenghitung Persegi Panjang")
            print("Pilih perhitungan yang ingin dilakukan:")
            print("a. Mencari panjang Persegi Panjang")
            print("b. Mencari lebar Persegi Panjang")
            sub_pilihan = input("Masukkan pilihan (a/b): ")

            if sub_pilihan == 'a':
                # Input untuk mencari panjang Persegi Panjang
                lebar = get_float_input("Masukkan lebar (0 jika tidak diketahui): ")
                luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
                keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")

                # Mulai pengukuran waktu
                waktumulai = time.time()

                if lebar == 0 and luas != 0 and keliling != 0:
                    panjang = cari_panjang_persegi_panjang(lebar=None, luas=luas, keliling=keliling)
                    print(f"Panjang Persegi Panjang: {panjang}")
                elif luas == 0 and lebar != 0 and keliling != 0:
                    luas_result = round(lebar * keliling / 2, 2)
                    print(f"Luas Persegi Panjang: {luas_result}")
                elif keliling == 0 and lebar != 0 and luas != 0:
                    keliling_result = round(2 * (lebar + (luas / lebar)), 2)
                    print(f"Keliling Persegi Panjang: {keliling_result}")
                else:
                    print("Data tidak cukup atau tidak valid untuk perhitungan.")

                # Menghitung waktu selesai
                waktuselesai = time.time()
                print(f"Waktu hitung: {waktuselesai - waktumulai:.5f} detik")

            elif sub_pilihan == 'b':
                # Input untuk mencari lebar Persegi Panjang
                panjang = get_float_input("Masukkan panjang (0 jika tidak diketahui): ")
                luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
                keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")

                # Mulai pengukuran waktu
                waktumulai = time.time()

                if panjang == 0 and luas != 0 and keliling != 0:
                    lebar = cari_lebar_persegi_panjang(panjang=None, luas=luas, keliling=keliling)
                    print(f"Lebar Persegi Panjang: {lebar}")
                elif luas == 0 and panjang != 0 and keliling != 0:
                    luas_result = round(panjang * keliling / 2, 2)
                    print(f"Luas Persegi Panjang: {luas_result}")
                elif keliling == 0 and panjang != 0 and luas != 0:
                    keliling_result = round(2 * (panjang + (luas / panjang)), 2)
                    print(f"Keliling Persegi Panjang: {keliling_result}")
                else:
                    print("Data tidak cukup atau tidak valid untuk perhitungan.")

                # Menghitung waktu selesai
                waktuselesai = time.time()
                print(f"Waktu hitung: {waktuselesai - waktumulai:.5f} detik")

        elif pilihan == '2':
            print("\nMenghitung Persegi")
            luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
            keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")

            # Mulai pengukuran waktu
            waktumulai = time.time()

            if luas == 0 and keliling != 0:
                sisi = cari_sisi_persegi(luas=None, keliling=keliling)
                print(f"Sisi Persegi: {sisi}")
            elif keliling == 0 and luas != 0:
                sisi = cari_sisi_persegi(luas=luas, keliling=None)
                print(f"Sisi Persegi: {sisi}")
            else:
                print("Data tidak cukup atau tidak valid untuk perhitungan.")

            # Menghitung waktu selesai
            waktuselesai = time.time()
            print(f"Waktu hitung: {waktuselesai - waktumulai:.5f} detik")

        elif pilihan == '3':
            print("\nMenghitung Lingkaran")
            luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
            keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")

            # Mulai pengukuran waktu
            waktumulai = time.time()

            if luas == 0 and keliling != 0:
                radius = cari_radius_lingkaran(luas=None, keliling=keliling)
                print(f"Radius Lingkaran: {radius}")
            elif keliling == 0 and luas != 0:
                radius = cari_radius_lingkaran(luas=luas, keliling=None)
                print(f"Radius Lingkaran: {radius}")
            else:
                print("Data tidak cukup atau tidak valid untuk perhitungan.")

            # Menghitung waktu selesai
            waktuselesai = time.time()
            print(f"Waktu hitung: {waktuselesai - waktumulai:.5f} detik")

        elif pilihan == '4':
            print("Terima kasih! Program dihentikan.")
            break

        else:
            print("Pilihan tidak valid!")

# Memanggil fungsi utama untuk menjalankan program
main()

