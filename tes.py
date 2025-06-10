import os
import config
import importlib
import pandas as pd
from controler import clear_terminal, buttons

def Fitur_Detail_Akun(ID = config.ID_Akun):
    data = pd.read_csv("database/Akun.csv")
    data = data[data['ID'] == ID]
    clear_terminal()
    print(data)
    print("───────────────────────────────────────────")
    print("              DATA AKUN ANDA              ")
    print("───────────────────────────────────────────")
    print(f"    ID Akun    : {data['ID'].values[0]}")
    print(f"    Nama       : {data['Name'].values[0]}")
    print(f"    Email      : {data['Email'].values[0]}")
    print(f"    Nommor HP  : {data['Nomor_Telepon'].values[0]}")
    print(f"    Password   : {data['Password'].values[0]}")
    print(f"    Kecamatan  : {data['Kecamatan'].values[0]}")
    print(f"    Desa       : {data['Desa'].values[0]}\n")
    buttons_parameter = []
    idx = 1
    for i in os.listdir("./fitur/User/Kelola_Akun"):
            if i.endswith(".py") and i not in ["Lihat_Profil.py"] :
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                modul_path = f"Fitur.User.Kelola_Akun.{i.replace(".py", "")}"
                modul = importlib.import_module(modul_path)
                buttons_parameter.append({"Nama": nama, "command":str(idx), "function":getattr(modul, f"Fitur_{i.replace(".py", "")}")})
                idx +=1
    buttons(buttons_parameter)
Fitur_Detail_Akun('2')