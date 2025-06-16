import pandas as pd
from controler import clear_terminal,Pencarian_String

def Fitur_Hapus_Akun(ID):
    data = pd.read_csv("database/Akun.csv")
    hasil_idx = Pencarian_String(data, "ID", ID)
    if hasil_idx is None:
        input(f"[ERROR] Akun dengan ID '{ID}' tidak ditemukan.")
        return
    clear_terminal()
    nama = data.loc[hasil_idx, "Name"]
    data = data.drop(index=hasil_idx).reset_index(drop=True)
    data.to_csv("database/Akun.csv", index=False)
    input(f"Akun {nama} Berhasil Dihapus!")