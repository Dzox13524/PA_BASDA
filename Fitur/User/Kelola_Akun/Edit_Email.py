import config
import pandas as pd

def Fitur_Edit_Email():
    data = pd.read_csv("./database/Akun.csv")
    Email_Baru = input("Masukkan Email baru: ")
    if '@gmail.com' not in Email_Baru: 
        input('Email Yang Anda Masukkan Tidak Falid!')
        return ''
    elif Email_Baru in data['Email'].values:
        input('Email Yang Anda Masukkan Sudah Digunakan!')
        return ''
    index_list = data.index[data['ID'] == config.ID_Akun].tolist()
    idx = index_list[0]
    data.loc[idx, "Email"] = Email_Baru
    data.to_csv("./database/Akun.csv", index=False)
    input("Data berhasil disimpan.\n")