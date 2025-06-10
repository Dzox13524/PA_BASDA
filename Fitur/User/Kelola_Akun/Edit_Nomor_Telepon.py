import config
import pandas as pd

def Fitur_Edit_Nomor_Telepon():
    data = pd.read_csv("./database/Akun.csv")
    index_list = data.index[data['ID'] == config.ID_Akun].tolist()
    idx = index_list[0]
    Nomor_Telepon_Baru = input("Masukkan Nomor Telepon baru: ")
    data.loc[idx, "Nomor_Telepon"] = Nomor_Telepon_Baru
    if Nomor_Telepon_Baru.isdigit():
        if Nomor_Telepon_Baru in data['Nomor_Telepon'].values:
            input('Nomor_Telepon Yang Anda Masukkan Sudah Digunakan!')
            return ''
        data.to_csv("./database/Akun.csv", index=False)
        input("Data berhasil disimpan.\n")
    else:
        input("Nomor Telepon Harus Berupa Angka")