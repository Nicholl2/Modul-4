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
        self.Buku = []

    def Tambah_buku(self, Buku):
        self.Buku.append(Buku)
        return "Buku telah ditambahkan ke Perpustakaan."

    def Buang_buku(self, ISBN):
        for Buku in self.Buku:
            if Buku.ISBN == ISBN:
                self.Buku.remove(Buku)
                return "Buku dihapus dari perpustakaan."
        return "Buku tidak ditemukan di perpustakaan."

    def Cari_buku(self, query):
        found_books = []
        for book in self.Buku:
            if query.lower() in book.Judul.lower() or query.lower() in book.Pengarang.lower() or query.lower() == book.ISBN:
                found_books.append(book)
        return found_books

    def load_books_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, author, year, isbn = row
                    self.Tambah_buku(Buku(title, author, year, isbn))
            return "Buku berhasil dimuat dari CSV."
        except FileNotFoundError:
            return "File tidak ditemukan."

def main():
    library = Perpustakaan()

    # Load books from CSV file
    print(library.load_books_from_csv("books.csv"))

    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Buang Buku")
        print("3. Cari Buku")
        print("4. Keluar")
        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            title = input("Masukkan judul buku: ")
            author = input("Masukkan nama pengarang: ")
            year = input("Masukkan tahun terbit: ")
            isbn = input("Masukkan ISBN: ")
            print(library.Tambah_buku(Buku(title, author, year, isbn)))
        elif choice == "2":
            isbn = input("Masukkan ISBN buku yang akan dihapus: ")
            print(library.Buang_buku(isbn))
        elif choice == "3":
            query = input("Masukkan judul, pengarang, atau ISBN untuk mencari: ")
            found_books = library.Cari_buku(query)
            if found_books:
                print("Hasil pencarian:")
                for book in found_books:
                    print(f"Judul: {book.Judul}, Pengarang: {book.Pengarang}, Tahun: {book.Tahun}, ISBN: {book.ISBN}")
            else:
                print("Buku tidak ditemukan.")
        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
