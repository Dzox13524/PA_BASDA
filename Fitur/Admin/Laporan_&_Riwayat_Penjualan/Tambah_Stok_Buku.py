import pandas as pd
from controler import clear_terminal, Pencarian_String


def Fitur_Tambah_Stok_Buku(ISBN):
    data = pd.read_csv("./database/Buku.csv")
    hasil_idx = Pencarian_String(data, "ISBN", ISBN)
    if hasil_idx is None:
        input(f"[ERROR] Buku dengan ISBN '{ISBN}' tidak ditemukan. Tekan Enter untuk kembali...")
        return
    clear_terminal()
    judul = data.loc[hasil_idx, "JudulBuku"]
    try:
        tambahan_stok = int(input(f"Masukkan jumlah stok buku yang ingin ditambahkan untuk '{judul}': "))
        if tambahan_stok < 0:
            input("[ERROR] Jumlah stok tidak boleh negatif. Tekan Enter untuk kembali...")
            return
    except ValueError:
        input("[ERROR] Input tidak valid. Harap masukkan angka bulat. Tekan Enter untuk kembali...")
        return

    data.loc[hasil_idx, "Stok"] += tambahan_stok
    data.to_csv("./database/Buku.csv", index=False)
    input(f"Stok buku '{judul}' berhasil ditambahkan sebanyak {tambahan_stok}. Tekan Enter untuk melanjutkan...")
