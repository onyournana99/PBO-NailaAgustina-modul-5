# class Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.nama} ({self.email})"


#  menyimpan objek pelanggan
data_pelanggan = {}


# menambah pelanggan
def tambah_pelanggan(id_pelanggan, nama, email):
    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah terdaftar!")
    else:
        data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")


# menghapus pelanggan
def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


# mencari pelanggan
def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        print("Pelanggan ditemukan:", data_pelanggan[id_pelanggan].info())
    else:
        print("Pelanggan tidak ditemukan.")


# fungsi menampilkan seluruh pelanggan
def tampilkan_pelanggan():
    print("\n=== Daftar Pelanggan ===")
    if not data_pelanggan:
        print("Belum ada data pelanggan.")
    else:
        for id_pelanggan, pelanggan in data_pelanggan.items():
            print(f"{id_pelanggan}: {pelanggan.info()}")


tambah_pelanggan("PL001", "Leni", "Leni@gmail.com")
tambah_pelanggan("PL002", "Dian", "Dian@gmail.com")
tambah_pelanggan("PL003", "Odi", "Odi@gmail.com")

tampilkan_pelanggan()

cari_pelanggan("PL002")

hapus_pelanggan("PL001")

tampilkan_pelanggan()
