import pandas as pd
from controler import clear_terminal

def Fitur_Mengembalikan_Buku(idx, judul):
    pinjam = pd.read_csv("./database/Peminjaman.csv")
    pinjam.loc[idx, "Status_Pengembalian"] = "Permintaan_Pengembalian"
    pinjam.to_csv("database/Peminjaman.csv", index=False)
    clear_terminal()
    input(f"Berhasil Mengajukan Pengembalian Buku {judul}!")

def Fitur_Membatalkan_Peminjaman_Buku(idx, judul, idx_Buku):
    data = pd.read_csv("./database/Buku.csv")
    pinjam = pd.read_csv("./database/Peminjaman.csv")
    baptalkan_Peminjaman = pinjam.drop(index=idx).reset_index(drop=True)
    baptalkan_Peminjaman.to_csv("database/Peminjaman.csv", index=False)
    data.loc[idx_Buku, "Stok"] += 1
    data.to_csv("database/Buku.csv", index=False)
    clear_terminal()
    input(f"Berhasil Membatalkan Peminjaman Buku {judul}!")

