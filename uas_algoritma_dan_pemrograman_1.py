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
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.matkul = []


    def tambah_matkul(self, mata_kuliah):
        self.matkul.append(mata_kuliah)


    def hapus_matkul(self, mata_kuliah):
        if mata_kuliah in self.matkul:
            self.matkul.remove(mata_kuliah)


    def lihat_matkul(self):
        return self.matkul


    def edit_matkul(self, matkul_lama, matkul_baru):
        self.hapus_matkul(matkul_lama)
        self.tambah_matkul(matkul_baru)


class SistemKRS:
    def __init__(self):
        self.mahasiswa = []
        self.daftar_matkul = []


    def tambah_mahasiswa(self, nama):
        mahasiswa = Mahasiswa(nama)
        self.mahasiswa.append(mahasiswa)


    def lihat_mahasiswa(self):
        return [mhs.nama for mhs in self.mahasiswa]


    def tambah_mata_kuliah(self, mata_kuliah):
        self.daftar_matkul.append(mata_kuliah)


    def pilih_matkul(self, nama_mahasiswa, mata_kuliah):
        for mhs in self.mahasiswa:
            if mhs.nama == nama_mahasiswa:
                mhs.tambah_matkul(mata_kuliah)


    def edit_matkul(self, nama_mahasiswa, matkul_lama, matkul_baru):
        for mhs in self.mahasiswa:
            if mhs.nama == nama_mahasiswa:
                mhs.edit_matkul(matkul_lama, matkul_baru)


    def lihat_matkul_mahasiswa(self, nama_mahasiswa):
        for mhs in self.mahasiswa:
            if mhs.nama == nama_mahasiswa:
                return mhs.lihat_matkul()


    def daftar_pilih_matkul(self, nama_mahasiswa):
        for mhs in self.mahasiswa:
            if mhs.nama == nama_mahasiswa:
                print("Daftar Mata Kuliah:")
                for i, matkul in enumerate(self.daftar_matkul):
                    print(f"{i + 1}. {matkul}")
                pilihan = int(input("Pilih nomor mata kuliah: ")) - 1
                if 0 <= pilihan < len(self.daftar_matkul):
                    mhs.tambah_matkul(self.daftar_matkul[pilihan])
                else:
                    print("Pilihan tidak valid.")


sistem = SistemKRS()


def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Daftar Mahasiswa")
        print("3. Tambah Mata Kuliah")
        print("4. Edit Mata Kuliah")
        print("5. Lihat Mata Kuliah Mahasiswa")
        print("6. Daftar Pilih Mata Kuliah")
        print("7. Keluar")
        pilihan = input("Pilih opsi: ")


        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            sistem.tambah_mahasiswa(nama)
        elif pilihan == '2':
            print("Daftar Mahasiswa:", sistem.lihat_mahasiswa())
        elif pilihan == '3':
            matkul = input("Masukkan mata kuliah: ")
            sistem.tambah_mata_kuliah(matkul)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa: ")
            matkul_lama = input("Masukkan mata kuliah lama: ")
            matkul_baru = input("Masukkan mata kuliah baru: ")
            sistem.edit_matkul(nama, matkul_lama, matkul_baru)
        elif pilihan == '5':
            nama = input("Masukkan nama mahasiswa: ")
            print("Mata Kuliah yang dipilih:", sistem.lihat_matkul_mahasiswa(nama))
        elif pilihan == '6':
            nama = input("Masukkan nama mahasiswa: ")
            sistem.daftar_pilih_matkul(nama)
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


menu()


# Chat Gpt
import time 

# Data contoh: Daftar mahasiswa dan mata kuliah
mahasiswa = []
mata_kuliah = []

# Fungsi untuk menambah mahasiswa
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    mahasiswa.append({"nama": nama, "mata_kuliah": []})
    print(f"Mahasiswa {nama} berhasil ditambahkan.")

# Fungsi untuk menambah mata kuliah
def tambah_mata_kuliah():
    nama_mata_kuliah = input("Masukkan nama mata kuliah: ")
    mata_kuliah.append(nama_mata_kuliah)
    print(f"Mata kuliah {nama_mata_kuliah} berhasil ditambahkan.")

# Fungsi untuk melihat daftar mahasiswa
def lihat_mahasiswa():
    print("Daftar Mahasiswa:")
    if mahasiswa:
        for idx, mhs in enumerate(mahasiswa, 1):
            print(f"{idx}. {mhs['nama']}")
    else:
        print("Tidak ada mahasiswa yang terdaftar.")

# Fungsi untuk melihat mata kuliah yang dipilih oleh mahasiswa
def lihat_mata_kuliah_terpilih():
    lihat_mahasiswa()
    nama_mahasiswa = input("Masukkan nama mahasiswa untuk melihat mata kuliah yang dipilih: ")
    mhs = next((mhs for mhs in mahasiswa if mhs['nama'] == nama_mahasiswa), None)
    if mhs:
        if mhs['mata_kuliah']:
            print(f"Mata kuliah yang dipilih oleh {mhs['nama']}:")
            for mk in mhs['mata_kuliah']:
                print(f"- {mk}")
        else:
            print(f"{mhs['nama']} belum memilih mata kuliah.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk memilih mata kuliah
def pilih_mata_kuliah():
    lihat_mahasiswa()
    nama_mahasiswa = input("Masukkan nama mahasiswa yang akan memilih mata kuliah: ")
    mhs = next((mhs for mhs in mahasiswa if mhs['nama'] == nama_mahasiswa), None)
    if mhs:
        print("Daftar Mata Kuliah Tersedia:")
        if mata_kuliah:
            for idx, mk in enumerate(mata_kuliah, 1):
                print(f"{idx}. {mk}")
            pilih = int(input("Pilih nomor mata kuliah untuk ditambahkan (0 untuk batal): "))
            if 0 < pilih <= len(mata_kuliah):
                matkul_terpilih = mata_kuliah[pilih - 1]
                if matkul_terpilih not in mhs['mata_kuliah']:
                    mhs['mata_kuliah'].append(matkul_terpilih)
                    print(f"Mata kuliah {matkul_terpilih} berhasil ditambahkan untuk {mhs['nama']}.")
                else:
                    print(f"{mhs['nama']} sudah memilih mata kuliah {matkul_terpilih}.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Tidak ada mata kuliah yang tersedia.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk mengedit mata kuliah yang dipilih mahasiswa
def edit_mata_kuliah():
    lihat_mahasiswa()
    nama_mahasiswa = input("Masukkan nama mahasiswa yang akan mengedit mata kuliah: ")
    mhs = next((mhs for mhs in mahasiswa if mhs['nama'] == nama_mahasiswa), None)
    if mhs:
        if mhs['mata_kuliah']:
            print(f"Mata kuliah yang dipilih oleh {mhs['nama']}:")
            for idx, mk in enumerate(mhs['mata_kuliah'], 1):
                print(f"{idx}. {mk}")
            pilihan = int(input("Pilih nomor mata kuliah yang ingin dihapus (0 untuk batal): "))
            if 0 < pilihan <= len(mhs['mata_kuliah']):
                mhs['mata_kuliah'].pop(pilihan - 1)
                print(f"Mata kuliah berhasil dihapus.")
            else:
                print("Batal menghapus mata kuliah.")
        else:
            print(f"{mhs['nama']} belum memilih mata kuliah.")

        # Menambahkan mata kuliah baru
        print("Daftar Mata Kuliah Tersedia:")
        if mata_kuliah:
            for idx, mk in enumerate(mata_kuliah, 1):
                print(f"{idx}. {mk}")
            tambah = input("Apakah Anda ingin menambah mata kuliah baru? (y/n): ").lower()
            if tambah == 'y':
                pilih = int(input("Pilih nomor mata kuliah yang ingin ditambahkan: "))
                if 1 <= pilih <= len(mata_kuliah):
                    matkul_terpilih = mata_kuliah[pilih - 1]
                    if matkul_terpilih not in mhs['mata_kuliah']:
                        mhs['mata_kuliah'].append(matkul_terpilih)
                        print(f"Mata kuliah {matkul_terpilih} berhasil ditambahkan untuk {mhs['nama']}.")
                    else:
                        print(f"{mhs['nama']} sudah memilih mata kuliah {matkul_terpilih}.")
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Tidak ada mata kuliah yang tersedia.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Menu utama
def menu():
    while True:
        start_time = time.time()  # Mulai waktu eksekusi
        print("\n=== Sistem KRS dan Perwalian ===")
        print("1. Tambah Mahasiswa")
        print("2. Tambah Mata Kuliah")
        print("3. Lihat Daftar Mahasiswa")
        print("4. Lihat Mata Kuliah yang Dipilih Mahasiswa")
        print("5. Pilih Mata Kuliah")
        print("6. Edit Mata Kuliah yang Dipilih Mahasiswa")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tambah_mata_kuliah()
        elif pilihan == "3":
            lihat_mahasiswa()
        elif pilihan == "4":
            lihat_mata_kuliah_terpilih()
        elif pilihan == "5":
            pilih_mata_kuliah()
        elif pilihan == "6":
            edit_mata_kuliah()
        elif pilihan == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

        end_time = time.time()  # Akhiri waktu eksekusi
        execution_time = end_time - start_time  # Hitung durasi
        print(f"Waktu eksekusi: {execution_time:.4f} detik")  # Tampilkan waktu eksekusi

# Menjalankan menu
if __name__ == "__main__":
    menu()
