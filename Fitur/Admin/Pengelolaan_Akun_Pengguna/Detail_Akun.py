import config

from Fitur.Umum.controler import clear_terminal,buttons
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Hapus_Akun import Fitur_Hapus_Akun
from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import sorted_data

def Fitur_Detail_Akun(idx):
    data = sorted_data(urutan =config.urutan)
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
    buttons_parameter.append({"Nama": "Hapus Akun", "command":"1", "function":lambda idx=idx:Fitur_Hapus_Akun(idx)})
    buttons(buttons_parameter)