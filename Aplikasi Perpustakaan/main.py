
print (100*("="))
print ("Selamat datang di Perpustakaan".center(100))
print (100*("="))
print ()

import csv
from Pinjam_Buku import Fitur1
from Pengembalian_Buku import Fitur2

class Buku:
    def __init__(self, Judul, Pengarang, Tahun, ISBN):
        self.Judul = Judul
        self.Pengarang = Pengarang
        self.Tahun = Tahun
        self.ISBN = ISBN
        self.yang_tersedia = 1

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def Tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        return "Buku telah ditambahkan ke Perpustakaan."

    def Buang_buku(self, ISBN):
        for buku in self.daftar_buku:
            if buku.ISBN == ISBN:
                self.daftar_buku.remove(buku)
                return "Buku dihapus dari perpustakaan."
        return "Buku tidak ditemukan di perpustakaan."

    def Cari_buku(self, daftar):
        temukan_buku = []
        for buku in self.daftar_buku:
            if daftar.lower() in buku.Judul.lower() or daftar.lower() in buku.Pengarang.lower() or daftar.lower() == buku.ISBN:
                temukan_buku.append(buku)
        return temukan_buku

    def Buku_csv(self, filename):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for baris in reader:
                    if len(baris) == 4:  
                        Pengarang, Judul, Tahun, ISBN = baris
                        self.Tambah_buku(Buku(Judul.strip(), Pengarang.strip(), Tahun.strip(), ISBN.strip()))
            return "Buku berhasil dimuat dari file Buku.csv."
        except FileNotFoundError:
            return "File tidak ditemukan."

def main():
    library = Perpustakaan()

    print(library.Buku_csv("Assets/Buku.csv"))

    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Buang Buku")
        print("3. Cari Buku")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            judul1 = input("Masukkan judul buku: ")
            pengarang1 = input("Masukkan nama pengarang: ")
            tahun1 = input("Masukkan tahun terbit: ")
            ISBN1 = input("Masukkan ISBN: ")
            print(library.Tambah_buku(Buku(judul1, pengarang1, tahun1, ISBN1)))
        elif pilihan == "2":
            isbn = input("Masukkan ISBN buku yang akan dihapus: ")
            print(library.Buang_buku(isbn))
        elif pilihan == "3":
            query = input("Masukkan judul, pengarang, atau ISBN untuk mencari: ")
            found_books = library.Cari_buku(query)
            if found_books:
                print("Hasil pencarian:")
                for buku in found_books:
                    print(f"Judul: {buku.Judul}, Pengarang: {buku.Pengarang}, Tahun: {buku.Tahun}, ISBN: {buku.ISBN}")
            else:
                print("Buku tidak ditemukan.")
        elif pilihan == "4":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
