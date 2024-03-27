class Fitur1:
    def Pinjam_buku(self, Buku, Peminjam):
        if Buku.yang_tersedia > 0:
            Buku.yang_tersedia -= 1
            return f"{Buku.Judul} telah dipinjam oleh {Peminjam}."
        else:
            return f"Maaf, {Buku.Judul} sedang tidak tersedia"

