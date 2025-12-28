class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} - {self.nama} ({self.jurusan}) IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru

import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("800x500")

        # Dictionary of objects
        self.data_mahasiswa = {}

        # frame input
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=0, column=2)
        tk.Label(frame_input, text="Jurusan").grid(row=1, column=0)
        tk.Label(frame_input, text="IPK").grid(row=1, column=2)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1, padx=5)
        self.entry_nama.grid(row=0, column=3, padx=5)
        self.entry_jurusan.grid(row=1, column=1, padx=5)
        self.entry_ipk.grid(row=1, column=3, padx=5)

        # frame button
        frame_button = tk.Frame(root)
        frame_button.pack(pady=5)

        tk.Button(frame_button, text="Tambah", command=self.tambah).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Update IPK", command=self.update).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Hapus", command=self.hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Cari", command=self.cari).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Export", command=self.export).pack(side=tk.LEFT, padx=5)

        # filter
        frame_filter = tk.Frame(root)
        frame_filter.pack(pady=5)

        tk.Label(frame_filter, text="Filter Jurusan").pack(side=tk.LEFT)
        self.filter_jurusan = tk.Entry(frame_filter)
        self.filter_jurusan.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_filter, text="Terapkan", command=self.filter_data).pack(side=tk.LEFT)

        # treeview
        frame_table = tk.Frame(root)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10)

        self.tree = ttk.Treeview(
            frame_table,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # info tambahan
        frame_info = tk.Frame(root)
        frame_info.pack(pady=5)

        tk.Button(frame_info, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_info, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)

    # fungsi crud
    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()

        try:
            ipk = float(self.entry_ipk.get())
        except ValueError:
            messagebox.showwarning("Error", "IPK harus berupa angka!")
            return

        if not nim or not nama or not jurusan:
            messagebox.showwarning("Error", "Semua field wajib diisi!")
            return

        if nim in self.data_mahasiswa:
            messagebox.showwarning("Error", "NIM sudah terdaftar!")
            return

        mhs = Mahasiswa(nim, nama, jurusan, ipk)
        self.data_mahasiswa[nim] = mhs
        self.refresh_tree()

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            del self.data_mahasiswa[nim]
            self.refresh_tree()
        else:
            messagebox.showwarning("Error", "Pilih data yang akan dihapus!")

    def update(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            try:
                ipk_baru = float(self.entry_ipk.get())
            except ValueError:
                messagebox.showwarning("Error", "IPK harus angka!")
                return

            self.data_mahasiswa[nim].update_ipk(ipk_baru)
            self.refresh_tree()
        else:
            messagebox.showwarning("Error", "Pilih mahasiswa!")

    def cari(self):
        keyword = self.entry_nama.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nama.lower() or keyword in mhs.nim:
                self.tree.insert("", tk.END,
                                 values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def filter_data(self):
        jurusan = self.filter_jurusan.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if jurusan in mhs.jurusan.lower():
                self.tree.insert("", tk.END,
                                 values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    # ===== FITUR TAMBAHAN =====
    def rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return
        mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi", mhs.info())

    def export(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for mhs in self.data_mahasiswa.values():
                    f.write(mhs.info() + "\n")
            messagebox.showinfo("Sukses", "Data berhasil diekspor!")

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END,
                             values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()
