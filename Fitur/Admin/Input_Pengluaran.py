from datetime import datetime
from database.connection import tambah_pengeluaran
from controler import clear_terminal

def Fitur_Tambah_Pengeluaran():
    while True:
        clear_terminal()
        print("=== TAMBAH DATA PENGELUARAN ===\n")

        deskripsi = input("Masukkan deskripsi pengeluaran   : ").strip()
        if not deskripsi:
            print("[ERROR] Deskripsi tidak boleh kosong!")
            input("Tekan Enter untuk ulangi...")
            continue

        try:
            jumlah = float(input("Masukkan jumlah pengeluaran (Rp): ").strip())
            if jumlah <= 0:
                raise ValueError
        except ValueError:
            print("[ERROR] Jumlah harus berupa angka positif!")
            input("Tekan Enter untuk ulangi...")
            continue

        konfirmasi = input(f"\nSimpan pengeluaran \"{deskripsi}\" sebesar Rp{jumlah:,.0f}? (y/n): ").strip().lower()
        if konfirmasi != "y":
            print("Pengeluaran dibatalkan.")
            input("Tekan Enter untuk kembali ke menu...")
            return

        tanggal_sekarang = datetime.now()
        tambah_pengeluaran(tanggal_sekarang, deskripsi, jumlah)
        print("\n[SUKSES] Data pengeluaran berhasil ditambahkan.")
        input("Tekan Enter untuk kembali ke menu...")
        return
