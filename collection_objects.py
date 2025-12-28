# class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"


# list berisi 5 objek buku
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Hujan", "Tere Liye", 2016),
    Buku("Dilan 1990", "Pidi Baiq", 2014)
]


# fungsi untuk mencari buku berdasarkan penulis
def cari_buku_berdasarkan_penulis(daftar, nama_penulis):
    hasil = []
    for buku in daftar:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# menampilkan hasil pencarian
penulis_dicari = "Tere Liye"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print(f"=== Hasil Pencarian Buku oleh {penulis_dicari} ===")
if hasil_pencarian:
    for buku in hasil_pencarian:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")
