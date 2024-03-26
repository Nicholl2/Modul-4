class Fitur2:
    def Pengembalian_buku(self, Buku, Peminjam):
        Buku.yang_tersedia += 1
        return f"{Peminjam} telah mengembalikan {Buku.Judul}."