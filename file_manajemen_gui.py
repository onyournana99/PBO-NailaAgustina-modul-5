import tkinter as tk
from tkinter import ttk, messagebox


# Class Tugas
class Tugas:
    def __init__(self, judul, status="Belum Selesai"):
        self.judul = judul
        self.status = status


# Class Aplikasi GUI
class AplikasiToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("500x400")

        # List of objects
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul Tugas").grid(row=0, column=0, sticky=tk.W)
        self.entry_judul = tk.Entry(frame_input, width=30)
        self.entry_judul.grid(row=0, column=1, padx=5)

        # Frame tombol
        frame_button = tk.Frame(root, padx=10, pady=10)
        frame_button.pack()

        tk.Button(frame_button, text="Tambah", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        # Frame Treeview
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_tabel, columns=("Judul", "Status"), show="headings")
        self.tree.heading("Judul", text="Judul Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

    # Tambah tugas
    def tambah_tugas(self):
        judul = self.entry_judul.get()
        if judul:
            tugas = Tugas(judul)
            self.daftar_tugas.append(tugas)
            self.tree.insert("", tk.END, values=(tugas.judul, tugas.status))
            self.entry_judul.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Judul tugas tidak boleh kosong!")

    # Hapus tugas
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.tree.delete(selected[0])
            del self.daftar_tugas[index]
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    # Edit tugas
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            judul_baru = self.entry_judul.get()
            if judul_baru:
                self.daftar_tugas[index].judul = judul_baru
                self.tree.item(selected[0], values=(judul_baru, self.daftar_tugas[index].status))
                self.entry_judul.delete(0, tk.END)
            else:
                messagebox.showwarning("Peringatan", "Masukkan judul baru!")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    # Tandai selesai
    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.daftar_tugas[index].status = "Selesai"
            self.tree.item(
                selected[0],
                values=(self.daftar_tugas[index].judul, "Selesai")
            )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan ditandai!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiToDo(root)
    root.mainloop()
