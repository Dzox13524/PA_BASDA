import config

from Fitur.Umum.controler import clear_terminal,buttons
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Hapus_Akun import Fitur_Hapus_Akun
from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import sorted_data

def buat_tabel_bad_character(pola):
    tabel = {}
    panjang = len(pola)
    for i in range(panjang - 1):
        tabel[pola[i]] = panjang - 1 - i
    return tabel

def boyer_moore_cocok(teks, pola):
    panjang_teks = len(teks)
    panjang_pola = len(pola)

    if panjang_pola == 0:
        return True

    tabel = buat_tabel_bad_character(pola)
    posisi = 0

    while posisi <= panjang_teks - panjang_pola:
        indeks = panjang_pola - 1

        while indeks >= 0 and pola[indeks] == teks[posisi + indeks]:
            indeks -= 1

        if indeks < 0:
            return True
        else:
            karakter = teks[posisi + indeks]
            if karakter in tabel:
                lompat = tabel[karakter]
            else:
                lompat = panjang_pola
            posisi += max(1, lompat)
    return False

def pencarian(data, berdasarkan, dicari):
    data_list = data[berdasarkan].tolist()
    hasil = ''
    for idx, item in enumerate(data_list):
           if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
               hasil = idx

    return hasil

def Fitur_Detail_Akun_berdasarkan(idx, urutan= config.urutanUser):
    hasil = pencarian(sorted_data(urutan), urutan, idx)
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