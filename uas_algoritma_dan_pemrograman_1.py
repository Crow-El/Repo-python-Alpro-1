# Black box
import time

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.matkul = []

    def tambah_matkul(self, matkul):
        self.matkul.append(matkul)

    def hapus_matkul(self, matkul):
        if matkul in self.matkul:
            self.matkul.remove(matkul)

    def lihat_matkul(self):
        return self.matkul


class SistemKRS:
    def __init__(self):
        self.mahasiswa_list = []
        self.matkul_list = []

    def tambah_mahasiswa(self, nama):
        # Cek apakah nama mahasiswa sudah ada
        if any(mhs.nama == nama for mhs in self.mahasiswa_list):
            return f"Mahasiswa dengan nama '{nama}' sudah terdaftar."
        mahasiswa = Mahasiswa(nama)
        self.mahasiswa_list.append(mahasiswa)
        return f"Mahasiswa '{nama}' berhasil ditambahkan."

    def tambah_matkul(self, matkul):
        if matkul in self.matkul_list:
            return f"Mata kuliah '{matkul}' sudah terdaftar."
        self.matkul_list.append(matkul)
        return f"Mata kuliah '{matkul}' berhasil ditambahkan."

    def lihat_mahasiswa(self):
        return [mhs.nama for mhs in self.mahasiswa_list]

    def lihat_matkul(self, nama_mahasiswa):
        for mhs in self.mahasiswa_list:
            if mhs.nama == nama_mahasiswa:
                return mhs.lihat_matkul()
        return None

    def pilih_matkul(self, nama_mahasiswa, matkul):
        for mhs in self.mahasiswa_list:
            if mhs.nama == nama_mahasiswa:
                if matkul in self.matkul_list:
                    if matkul not in mhs.matkul:
                        mhs.tambah_matkul(matkul)
                        return f"Mata kuliah '{matkul}' berhasil ditambahkan untuk {nama_mahasiswa}."
                    else:
                        return f"Mata kuliah '{matkul}' sudah dipilih oleh {nama_mahasiswa}."
                else:
                    return f"Mata kuliah '{matkul}' tidak tersedia."
        return "Mahasiswa tidak ditemukan."

    def edit_matkul(self, nama_mahasiswa, matkul_lama, matkul_baru):
        for mhs in self.mahasiswa_list:
            if mhs.nama == nama_mahasiswa:
                if matkul_lama in mhs.matkul:
                    if matkul_baru in self.matkul_list:
                        mhs.hapus_matkul(matkul_lama)
                        mhs.tambah_matkul(matkul_baru)
                        return f"Mata kuliah '{matkul_lama}' berhasil diganti dengan '{matkul_baru}' untuk {nama_mahasiswa}."
                    else:
                        return f"Mata kuliah baru '{matkul_baru}' tidak tersedia."
                else:
                    return f"Mata kuliah '{matkul_lama}' tidak ditemukan pada mahasiswa {nama_mahasiswa}."
        return "Mahasiswa tidak ditemukan."


def main():
    sistem = SistemKRS()

    while True:
        print("\n=== Sistem KRS dan Perwalian ===")
        print("1. Tambah Mahasiswa")
        print("2. Tambah Mata Kuliah")
        print("3. Lihat Daftar Mahasiswa")
        print("4. Lihat Mata Kuliah yang Dipilih Mahasiswa")
        print("5. Pilih Mata Kuliah")
        print("6. Edit Mata Kuliah")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        start_time = time.time()  # Mulai pengukuran waktu

        if pilihan == '1':
            nama_mahasiswa = input("Masukkan nama mahasiswa: ")
            print(sistem.tambah_mahasiswa(nama_mahasiswa))

        elif pilihan == '2':
            matkul = input("Masukkan nama mata kuliah: ")
            print(sistem.tambah_matkul(matkul))

        elif pilihan == '3':
            print("Daftar Mahasiswa:")
            mahasiswa_list = sistem.lihat_mahasiswa()
            if mahasiswa_list:
                for mhs in mahasiswa_list:
                    print(f"- {mhs}")
            else:
                print("Belum ada mahasiswa yang terdaftar.")

        elif pilihan == '4':
            nama_mahasiswa = input("Masukkan nama mahasiswa: ")
            matkul_dipilih = sistem.lihat_matkul(nama_mahasiswa)
            if matkul_dipilih is not None:
                if matkul_dipilih:
                    print(f"Mata Kuliah yang Dipilih oleh {nama_mahasiswa}:")
                    for matkul in matkul_dipilih:
                        print(f"- {matkul}")
                else:
                    print(f"{nama_mahasiswa} belum memilih mata kuliah.")
            else:
                print("Mahasiswa tidak ditemukan.")

        elif pilihan == '5':
            nama_mahasiswa = input("Masukkan nama mahasiswa: ")
            matkul = input("Masukkan nama mata kuliah yang dipilih: ")
            print(sistem.pilih_matkul(nama_mahasiswa, matkul))

        elif pilihan == '6':
            nama_mahasiswa = input("Masukkan nama mahasiswa: ")
            matkul_lama = input("Masukkan mata kuliah yang ingin diedit: ")
            matkul_baru = input("Masukkan mata kuliah baru: ")
            print(sistem.edit_matkul(nama_mahasiswa, matkul_lama, matkul_baru))

        elif pilihan == '7':
            print("Keluar dari sistem.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        end_time = time.time()  # Akhiri pengukuran waktu
        execution_time = end_time - start_time  # Hitung waktu eksekusi
        print(f"Waktu eksekusi: {execution_time:.4f} detik")


if __name__ == "__main__":
    main()

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
