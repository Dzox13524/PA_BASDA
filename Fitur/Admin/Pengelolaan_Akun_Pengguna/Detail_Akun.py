import config

from controler import clear_terminal,buttons,Pencarian_String
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Hapus_Akun import Fitur_Hapus_Akun
from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import sorted_data

def Fitur_Detail_Akun_berdasarkan(idx, urutan= config.urutanUser):
    hasil = Pencarian_String(sorted_data(urutan), urutan, idx)
    data = sorted_data(urutan).iloc[hasil]
    clear_terminal()
    print("───────────────────────────────────────────")
    print(f"  DATA AKUN {data['Name']}:")
    print("───────────────────────────────────────────")
    print(f"    ID Akun    : {data['ID']}")
    print(f"    Nama       : {data['Name']}")
    print(f"    Email      : {data['Email']}")
    print(f"    Kecamatan  : {data['Kecamatan']}")
    print(f"    Desa       : {data['Desa']}")
    buttons_parameter = []
    buttons_parameter.append({"Nama": "Hapus Akun", "command":"1", "function":lambda idx=data['ID']:Fitur_Hapus_Akun(idx)})
    buttons(buttons_parameter)

def Fitur_Detail_Akun(idx, urutan = config.urutanUser):
    data = sorted_data(urutan)
    clear_terminal()
    print("───────────────────────────────────────────")
    print(f"  DATA AKUN {data.iloc[idx]['Name']}:")
    print("───────────────────────────────────────────")
    print(f"    ID Akun    : {data.iloc[idx]['ID']}")
    print(f"    Nama       : {data.iloc[idx]['Name']}")
    print(f"    Email      : {data.iloc[idx]['Email']}")
    print(f"    Kecamatan  : {data.iloc[idx]['Kecamatan']}")
    print(f"    Desa       : {data.iloc[idx]['Desa']}")
    buttons_parameter = []
    buttons_parameter.append({"Nama": "Hapus Akun", "command":"1", "function":lambda idx=data.iloc[idx]['ID']:Fitur_Hapus_Akun(idx)})
    buttons(buttons_parameter)