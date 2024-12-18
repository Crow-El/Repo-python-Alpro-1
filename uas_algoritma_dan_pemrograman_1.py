# Black Box

import time

# Daftar global untuk menyimpan data mahasiswa dan mata kuliah umum
mahasiswa_data = []
mata_kuliah_umum = []

def hitung_waktu(func):
    def wrapper(*args, **kwargs):
        mulai = time.perf_counter()  # Timer dengan presisi tinggi
        hasil = func(*args, **kwargs)
        selesai = time.perf_counter()
        print(f"\nWaktu eksekusi {func.__name__}: {(selesai - mulai) * 1000:.4f} ms")
        return hasil
    return wrapper

@hitung_waktu
def menu_utama():
    while True:
        print("\n=== Sistem KRS ===")
        print("1. Login sebagai Mahasiswa")
        print("2. Login sebagai Dosen")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            menu_mahasiswa()
        elif pilihan == '2':
            menu_dosen()
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

@hitung_waktu
def menu_mahasiswa():
    print("\n=== Menu Mahasiswa ===")
    nama = input("Masukkan nama: ")
    mahasiswa = next((m for m in mahasiswa_data if m['nama'] == nama), None)
    if not mahasiswa:
        print("Nama tidak ditemukan. Hubungi dosen untuk pendaftaran.")
        return

    while True:
        print("\n1. Lihat daftar mata kuliah")
        print("2. Ubah mata kuliah yang dipilih")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            lihat_mata_kuliah(mahasiswa)
        elif pilihan == '2':
            ubah_mata_kuliah(mahasiswa)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

@hitung_waktu
def lihat_mata_kuliah(mahasiswa):
    print("\nMata kuliah umum yang tersedia:")
    for i, mk in enumerate(mata_kuliah_umum, start=1):
        print(f"{i}. {mk}")

    print("\nMata kuliah yang Anda pilih:")
    for i, mk in enumerate(mahasiswa["mata_kuliah"], start=1):
        print(f"{i}. {mk}")

@hitung_waktu
def ubah_mata_kuliah(mahasiswa):
    while True:
        print("\n1. Tambah mata kuliah")
        print("2. Hapus mata kuliah")
        print("3. Edit mata kuliah")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            tambah_mata_kuliah(mahasiswa)
        elif pilihan == '2':
            hapus_mata_kuliah(mahasiswa)
        elif pilihan == '3':
            edit_mata_kuliah(mahasiswa)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

@hitung_waktu
def tambah_mata_kuliah(mahasiswa):
    print("\nPilih mata kuliah untuk ditambahkan:")
    for i, mk in enumerate(mata_kuliah_umum, start=1):
        print(f"{i}. {mk}")

    try:
        pilihan = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan <= len(mata_kuliah_umum):
            mk = mata_kuliah_umum[pilihan - 1]
            if mk not in mahasiswa["mata_kuliah"]:
                mahasiswa["mata_kuliah"].append(mk)
                print(f"Mata kuliah {mk} berhasil ditambahkan.")
            else:
                print("Mata kuliah sudah ada dalam daftar Anda.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@hitung_waktu
def hapus_mata_kuliah(mahasiswa):
    print("\nPilih mata kuliah untuk dihapus:")
    for i, mk in enumerate(mahasiswa["mata_kuliah"], start=1):
        print(f"{i}. {mk}")

    try:
        pilihan = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan <= len(mahasiswa["mata_kuliah"]):
            mk = mahasiswa["mata_kuliah"].pop(pilihan - 1)
            print(f"Mata kuliah {mk} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@hitung_waktu
def edit_mata_kuliah(mahasiswa):
    print("\nPilih mata kuliah untuk diedit:")
    for i, mk in enumerate(mahasiswa["mata_kuliah"], start=1):
        print(f"{i}. {mk}")

    try:
        pilihan = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan <= len(mahasiswa["mata_kuliah"]):
            mk_baru = input("Masukkan nama mata kuliah baru: ")
            mahasiswa["mata_kuliah"][pilihan - 1] = mk_baru
            print("Mata kuliah berhasil diubah.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@hitung_waktu
def menu_dosen():
    while True:
        print("\n=== Menu Dosen ===")
        print("1. Fungsi perwalian")
        print("2. Lihat data mahasiswa")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            fungsi_perwalian()
        elif pilihan == '2':
            lihat_data_mahasiswa()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

@hitung_waktu
def fungsi_perwalian():
    while True:
        print("\n1. Tambah nama mahasiswa")
        print("2. Tambah mata kuliah umum")
        print("3. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            mahasiswa_data.append({"nama": nama, "mata_kuliah": []})
            print("Mahasiswa berhasil ditambahkan.")
        elif pilihan == '2':
            mk = input("Masukkan nama mata kuliah umum: ")
            if mk not in mata_kuliah_umum:
                mata_kuliah_umum.append(mk)
                print("Mata kuliah berhasil ditambahkan.")
            else:
                print("Mata kuliah sudah ada dalam daftar.")
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

@hitung_waktu
def lihat_data_mahasiswa():
    while True:
        print("\n1. Hapus data mahasiswa")
        print("2. Edit data mahasiswa")
        print("3. Lihat daftar mahasiswa")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            hapus_data_mahasiswa()
        elif pilihan == '2':
            edit_data_mahasiswa()
        elif pilihan == '3':
            print("\nDaftar mahasiswa:")
            for i, mhs in enumerate(mahasiswa_data, start=1):
                print(f"{i}. {mhs['nama']}")
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

@hitung_waktu
def hapus_data_mahasiswa():
    print("\nPilih mahasiswa untuk dihapus:")
    for i, mhs in enumerate(mahasiswa_data, start=1):
        print(f"{i}. {mhs['nama']}")

    try:
        pilihan = int(input("Masukkan nomor mahasiswa: "))
        if 1 <= pilihan <= len(mahasiswa_data):
            mahasiswa = mahasiswa_data.pop(pilihan - 1)
            print(f"Data mahasiswa {mahasiswa['nama']} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@hitung_waktu
def edit_data_mahasiswa():
    print("\nPilih mahasiswa untuk diedit:")
    for i, mhs in enumerate(mahasiswa_data, start=1):
        print(f"{i}. {mhs['nama']}")
    try:
        pilihan = int(input("Masukkan nomor mahasiswa: "))
        if 1 <= pilihan <= len(mahasiswa_data):
            mahasiswa = mahasiswa_data[pilihan - 1]
            nama_baru = input(f"Masukkan nama baru untuk {mahasiswa['nama']}: ")
            mahasiswa['nama'] = nama_baru
            print(f"Nama mahasiswa berhasil diubah menjadi {nama_baru}.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Jalankan program utama
menu_utama()



# Copilot AI
import time

# Variabel global untuk menyimpan data
data_mahasiswa = []  # Array untuk menyimpan data mahasiswa
matkul_umum = []     # Array untuk menyimpan mata kuliah umum (diinput oleh dosen)

def penghitung_waktu(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Menggunakan perf_counter untuk presisi tinggi
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"\nWaktu eksekusi {func._name_}: {(end_time - start_time) * 1000:.4f} ms")
        return result
    return wrapper

@penghitung_waktu
def menu_utama():
    while True:
        print("\n=== Sistem KRS ===")
        print("1. Masuk sebagai Mahasiswa")
        print("2. Masuk sebagai Dosen")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            menu_mahasiswa()
        elif pilihan == '2':
            menu_dosen()
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@penghitung_waktu
def menu_mahasiswa():
    print("\n=== Menu Mahasiswa ===")
    nama = input("Masukkan nama Anda: ")
    mahasiswa = next((m for m in data_mahasiswa if m['nama'] == nama), None)
    if not mahasiswa:
        print("Nama Anda belum terdaftar. Silakan hubungi dosen untuk pendaftaran.")
        return

    while True:
        print("\n1. Lihat daftar mata kuliah")
        print("2. Ubah daftar mata kuliah yang dipilih")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            lihat_matkul(mahasiswa)
        elif pilihan == '2':
            ubah_matkul(mahasiswa)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@penghitung_waktu
def lihat_matkul(mahasiswa):
    print("\nDaftar mata kuliah umum yang tersedia:")
    for i, matkul in enumerate(matkul_umum, start=1):
        print(f"{i}. {matkul}")

    print("\nDaftar mata kuliah yang Anda pilih:")
    for i, matkul in enumerate(mahasiswa["matkul"], start=1):
        print(f"{i}. {matkul}")

@penghitung_waktu
def ubah_matkul(mahasiswa):
    while True:
        print("\n1. Tambah mata kuliah")
        print("2. Hapus mata kuliah")
        print("3. Edit mata kuliah")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            tambah_matkul(mahasiswa)
        elif pilihan == '2':
            hapus_matkul(mahasiswa)
        elif pilihan == '3':
            edit_matkul(mahasiswa)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@penghitung_waktu
def tambah_matkul(mahasiswa):
    print("\nPilih mata kuliah untuk ditambahkan:")
    for i, matkul in enumerate(matkul_umum, start=1):
        print(f"{i}. {matkul}")

    try:
        pilihan = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan <= len(matkul_umum):
            matkul = matkul_umum[pilihan - 1]
            if matkul not in mahasiswa["matkul"]:
                mahasiswa["matkul"].append(matkul)
                print(f"Mata kuliah {matkul} berhasil ditambahkan.")
            else:
                print("Mata kuliah sudah ada dalam daftar Anda.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@penghitung_waktu
def hapus_matkul(mahasiswa):
    print("\nPilih mata kuliah untuk dihapus:")
    for i, matkul in enumerate(mahasiswa["matkul"], start=1):
        print(f"{i}. {matkul}")

    try:
        pilihan = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan <= len(mahasiswa["matkul"]):
            matkul = mahasiswa["matkul"].pop(pilihan - 1)
            print(f"Mata kuliah {matkul} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@penghitung_waktu
def edit_matkul(mahasiswa):
    print("\nPilih mata kuliah untuk diedit:")
    for i, matkul in enumerate(mahasiswa["matkul"], start=1):
        print(f"{i}. {matkul}")

    try:
        pilihan = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan <= len(mahasiswa["matkul"]):
            matkul_baru = input("Masukkan nama mata kuliah baru: ")
            mahasiswa["matkul"][pilihan - 1] = matkul_baru
            print("Mata kuliah berhasil diubah.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@penghitung_waktu
def menu_dosen():
    while True:
        print("\n=== Menu Dosen ===")
        print("1. Pemilihan fungsi perwalian")
        print("2. Melihat data mahasiswa")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            fungsi_perwalian()
        elif pilihan == '2':
            lihat_data_mahasiswa()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@penghitung_waktu
def fungsi_perwalian():
    while True:
        print("\n1. Tambah nama mahasiswa")
        print("2. Tambah mata kuliah umum")
        print("3. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            data_mahasiswa.append({"nama": nama, "matkul": []})
            print("Mahasiswa berhasil ditambahkan.")
        elif pilihan == '2':
            matkul = input("Masukkan nama mata kuliah umum: ")
            if matkul not in matkul_umum:
                matkul_umum.append(matkul)
                print("Mata kuliah berhasil ditambahkan.")
            else:
                print("Mata kuliah sudah ada dalam daftar.")
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@penghitung_waktu
def lihat_data_mahasiswa():
    while True:
        print("\n1. Hapus data mahasiswa")
        print("2. Edit data mahasiswa")
        print("3. Lihat daftar mahasiswa")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            hapus_data_mahasiswa()
        elif pilihan == '2':
            edit_data_mahasiswa()
        elif pilihan == '3':
            print("\nDaftar mahasiswa:")
            for i, mhs in enumerate(data_mahasiswa, start=1):
                print(f"{i}. {mhs['nama']}")
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@penghitung_waktu
def hapus_data_mahasiswa():
    print("\nPilih mahasiswa untuk dihapus:")
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"{i}. {mhs['nama']}")

    try:
        pilihan = int(input("Masukkan nomor mahasiswa: "))
        if 1 <= pilihan <= len(data_mahasiswa):
            mahasiswa = data_mahasiswa.pop(pilihan - 1)
            print(f"Data mahasiswa {mahasiswa['nama']} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@penghitung_waktu
def edit_data_mahasiswa():
    print("\nPilih mahasiswa untuk diedit:")
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"{i}. {mhs['nama']}")
    try:
        pilihan = int(input("Masukkan nomor mahasiswa: "))
        if 1 <= pilihan <= len(data_mahasiswa):
            mahasiswa = data_mahasiswa[pilihan - 1]
            nama_baru = input(f"Masukkan nama baru untuk {mahasiswa['nama']}: ")
            mahasiswa['nama'] = nama_baru
            print(f"Nama mahasiswa berhasil diubah menjadi {nama_baru}.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Jalankan program utama
menu_utama()



# Chat-GPT
import time

data_mahasiswa = []
matkul_umum = []

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"\nWaktu eksekusi {func.__name__}: {(end_time - start_time) * 1000:.4f} ms")
        return result
    return wrapper

@timing_decorator
def main_menu():
    while True:
        print("\n=== Sistem KRS ===")
        print("1. Masuk sebagai Mahasiswa")
        print("2. Masuk sebagai Dosen")
        print("3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            mahasiswa_menu()
        elif choice == '2':
            dosen_menu()
        elif choice == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@timing_decorator
def mahasiswa_menu():
    print("\n=== Menu Mahasiswa ===")
    nama = input("Masukkan nama Anda: ")
    mahasiswa = next((m for m in data_mahasiswa if m['nama'] == nama), None)
    if not mahasiswa:
        print("Nama Anda belum terdaftar. Silakan hubungi dosen untuk pendaftaran.")
        return

    while True:
        print("\n1. Lihat daftar mata kuliah")
        print("2. Ubah daftar mata kuliah yang dipilih")
        print("3. Kembali ke menu utama")
        choice = input("Pilih opsi: ")

        if choice == '1':
            lihat_matkul(mahasiswa)
        elif choice == '2':
            ubah_matkul(mahasiswa)
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@timing_decorator
def lihat_matkul(mahasiswa):
    print("\nDaftar mata kuliah umum yang tersedia:")
    for i, matkul in enumerate(matkul_umum, start=1):
        print(f"{i}. {matkul}")

    print("\nDaftar mata kuliah yang Anda pilih:")
    for i, matkul in enumerate(mahasiswa["matkul"], start=1):
        print(f"{i}. {matkul}")

@timing_decorator
def ubah_matkul(mahasiswa):
    while True:
        print("\n1. Tambah mata kuliah")
        print("2. Hapus mata kuliah")
        print("3. Edit mata kuliah")
        print("4. Kembali")
        choice = input("Pilih opsi: ")

        if choice == '1':
            tambah_matkul(mahasiswa)
        elif choice == '2':
            hapus_matkul(mahasiswa)
        elif choice == '3':
            edit_matkul(mahasiswa)
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@timing_decorator
def tambah_matkul(mahasiswa):
    print("\nPilih mata kuliah untuk ditambahkan:")
    for i, matkul in enumerate(matkul_umum, start=1):
        print(f"{i}. {matkul}")

    try:
        choice = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= choice <= len(matkul_umum):
            matkul = matkul_umum[choice - 1]
            if matkul not in mahasiswa["matkul"]:
                mahasiswa["matkul"].append(matkul)
                print(f"Mata kuliah {matkul} berhasil ditambahkan.")
            else:
                print("Mata kuliah sudah ada dalam daftar Anda.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@timing_decorator
def hapus_matkul(mahasiswa):
    print("\nPilih mata kuliah untuk dihapus:")
    for i, matkul in enumerate(mahasiswa["matkul"], start=1):
        print(f"{i}. {matkul}")

    try:
        choice = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= choice <= len(mahasiswa["matkul"]):
            matkul = mahasiswa["matkul"].pop(choice - 1)
            print(f"Mata kuliah {matkul} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@timing_decorator
def edit_matkul(mahasiswa):
    print("\nPilih mata kuliah untuk diedit:")
    for i, matkul in enumerate(mahasiswa["matkul"], start=1):
        print(f"{i}. {matkul}")

    try:
        choice = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= choice <= len(mahasiswa["matkul"]):
            matkul_baru = input("Masukkan nama mata kuliah baru: ")
            mahasiswa["matkul"][choice - 1] = matkul_baru
            print("Mata kuliah berhasil diubah.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@timing_decorator
def dosen_menu():
    while True:
        print("\n=== Menu Dosen ===")
        print("1. Pemilihan fungsi perwalian")
        print("2. Melihat data mahasiswa")
        print("3. Kembali ke menu utama")
        choice = input("Pilih opsi: ")

        if choice == '1':
            fungsi_perwalian()
        elif choice == '2':
            lihat_data_mahasiswa()
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@timing_decorator
def fungsi_perwalian():
    while True:
        print("\n1. Tambah nama mahasiswa")
        print("2. Tambah mata kuliah umum")
        print("3. Kembali")
        choice = input("Pilih opsi: ")

        if choice == '1':
            nama = input("Masukkan nama mahasiswa: ")
            data_mahasiswa.append({"nama": nama, "matkul": []})
            print("Mahasiswa berhasil ditambahkan.")
        elif choice == '2':
            matkul = input("Masukkan nama mata kuliah umum: ")
            if matkul not in matkul_umum:
                matkul_umum.append(matkul)
                print("Mata kuliah berhasil ditambahkan.")
            else:
                print("Mata kuliah sudah ada dalam daftar.")
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@timing_decorator
def lihat_data_mahasiswa():
    while True:
        print("\n1. Hapus data mahasiswa")
        print("2. Edit data mahasiswa")
        print("3. Lihat daftar mahasiswa")
        print("4. Kembali")
        choice = input("Pilih opsi: ")

        if choice == '1':
            hapus_data_mahasiswa()
        elif choice == '2':
            edit_data_mahasiswa()
        elif choice == '3':
            print("\nDaftar mahasiswa:")
            for i, mhs in enumerate(data_mahasiswa, start=1):
                print(f"{i}. {mhs['nama']}")
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

@timing_decorator
def hapus_data_mahasiswa():
    print("\nPilih mahasiswa untuk dihapus:")
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"{i}. {mhs['nama']}")

    try:
        choice = int(input("Masukkan nomor mahasiswa: "))
        if 1 <= choice <= len(data_mahasiswa):
            mahasiswa = data_mahasiswa.pop(choice - 1)
            print(f"Data mahasiswa {mahasiswa['nama']} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

@timing_decorator
def edit_data_mahasiswa():
    print("\nPilih mahasiswa untuk diedit:")
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"{i}. {mhs['nama']}")
    try:
        choice = int(input("Masukkan nomor mahasiswa: "))
        if 1 <= choice <= len(data_mahasiswa):
            mahasiswa = data_mahasiswa[choice - 1]
            nama_baru = input(f"Masukkan nama baru untuk {mahasiswa['nama']}: ")
            mahasiswa['nama'] = nama_baru
            print(f"Nama mahasiswa berhasil diubah menjadi {nama_baru}.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Jalankan program utama
main_menu()
