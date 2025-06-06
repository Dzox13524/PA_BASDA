import pandas as pd
from Fitur.Umum.controler import clear_terminal


def Fitur_Hapus_Akun(idx):
    data = pd.read_csv("database/Akun.csv")
    clear_terminal()
    akun = data.iloc[idx]["Name"]
    data = data.drop(index=idx).reset_index(drop=True)
    data.to_csv("database/Akun.csv", index=False)
    input(f"Akun {akun} Berhasil Dihapus!")
    pass