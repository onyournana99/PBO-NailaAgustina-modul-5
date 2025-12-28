import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # Label Judul
        self.label_judul = tk.Label(
            root,
            text="Konversi Celsius ke Fahrenheit",
            font=("Arial", 12)
        )
        self.label_judul.pack(pady=10)

        # Entry Celsius
        self.entry_celsius = tk.Entry(root, width=20)
        self.entry_celsius.pack(pady=5)
        self.entry_celsius.insert(0, "Masukkan suhu (°C)")

        # Button Konversi
        self.btn_konversi = tk.Button(
            root,
            text="Konversi",
            command=self.konversi_suhu
        )
        self.btn_konversi.pack(pady=5)

        # Label Hasil
        self.label_hasil = tk.Label(root, text="")
        self.label_hasil.pack(pady=10)

    def konversi_suhu(self):
        try:
            celsius = float(self.entry_celsius.get())
            fahrenheit = (celsius * 9/5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showwarning(
                "Input Salah",
                "Masukkan angka yang valid!"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
