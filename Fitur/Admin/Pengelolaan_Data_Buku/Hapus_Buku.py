import pandas as pd
from controler import clear_terminal,Pencarian_String

def Fitur_Hapus_Buku(ISBN):
    data = pd.read_csv("./database/Buku.csv")
    hasil_idx = Pencarian_String(data, "ISBN", ISBN)
    if hasil_idx is None:
        input(f"[ERROR] Buku dengan ISBN '{ISBN}' tidak ditemukan.")
        return
    clear_terminal()
    judul = data.loc[hasil_idx, "JudulBuku"]
    data = data.drop(index=hasil_idx).reset_index(drop=True)
    data.to_csv("database/Buku.csv", index=False)
    input(f"Buku {judul} Berhasil Dihapus!")