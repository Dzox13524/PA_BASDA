import config
import pandas as pd

def Fitur_Edit_Nama():
    data = pd.read_csv("./database/Akun.csv")
    nama_baru = input("Masukkan nama baru: ")
    index_list = data.index[data['ID'] == config.ID_Akun].tolist()
    idx = index_list[0]
    data.loc[idx, "Name"] = nama_baru
    data.to_csv("./database/Akun.csv", index=False)
    input("Data berhasil disimpan.\n")