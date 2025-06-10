import pandas as pd
from controler import clear_terminal,buttons
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Detail_Akun import Fitur_Detail_Akun_berdasarkan
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Hapus_Akun import Fitur_Hapus_Akun

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
    hasil = {
        "rekomendasi": [],
        "cocok": []
    }
    sudah_cocok = []
    
    data_dicari = dicari.split(" ")
    for i in data_dicari:
        kata = i.lower()
        for idx, item in enumerate(data_list):
            item_lower = str(item).lower()
            if boyer_moore_cocok(item_lower, kata):
                if item_lower == dicari.lower():
                    if idx not in sudah_cocok:
                        hasil["cocok"].append({"ditemukan": item, "index": idx})
                        sudah_cocok.append(idx)
                else:
                    hasil["rekomendasi"].append({"ditemukan": item, "index": idx})

    return hasil

mencari = ""
def mencari_berdasarkan(berdasarkan):
    global mencari
    mencari = berdasarkan

def Fitur_Cari_Akun():
    global mencari
    loop = True
    data = pd.read_csv("database/Akun.csv")
    while loop:
        buttons_parameter = []
        clear_terminal()
        buttons_parameter.append({"Nama": "Berdasarkan ID", "command":"1", "function":lambda:mencari_berdasarkan("ID")})
        buttons_parameter.append({"Nama": "Berdasarkan Nama", "command":"2", "function":lambda:mencari_berdasarkan("Name")})
        buttons_parameter.append({"Nama": "Berdasarkan No Hp", "command":"3", "function":lambda:mencari_berdasarkan("Nomor_Telepon")})
        buttons_parameter.append({"Nama": "Berdasarkan Kecamatan", "command":"4", "function":lambda:mencari_berdasarkan("Kecamatan")})
        buttons_parameter.append({"Nama": "Berdasarkan Desa", "command":"5", "function":lambda:mencari_berdasarkan("Desa")})
        loop = buttons(buttons_parameter)
        buttons_parameter = []
        if mencari == "":
            return
        yang_dicari = input("Kamu Mau Mencari Apa: ")
        result = pencarian(data, mencari, yang_dicari)
        clear_terminal()
        print("───────────────────────────────────────────")
        print("              HASIL PENCARIAN")
        print(f"          Kata Kunci: {yang_dicari}")
        print("───────────────────────────────────────────")
        if len(result["cocok"]) > 0:
            print(f"\n  ◎ DATA DITEMUKAN ({len(result["cocok"])} Akun)")
            for idx, res1 in enumerate(result["cocok"]):
                data1 = data.iloc[res1["index"]]
                print("\n───────────────────────────────────────────")
                print(f"  AKUN {idx + 1}:")
                print("───────────────────────────────────────────")
                print(f"    ID Akun    : {data1['ID']}")
                print(f"    Nama       : {data1['Name']}")
                print(f"    Email      : {data1['Email']}")
                print(f"    Kecamatan  : {data1['Kecamatan']}")
                print(f"    Desa       : {data1['Desa']}")
                buttons_parameter.append({"Nama": "Hapus Akun " + data1["Name"], "command":"D" + str(idx +1), "function":lambda i=data1['ID']: Fitur_Hapus_Akun(i)})
        else:
            print("\n  ◎ DATA TIDAK DITEMUKAN\n\n")
            print(f"    Maaf, tidak ada akun yang cocok persis dengan kata kunci {yang_dicari}.\n    Coba periksa kembali ejaan Anda atau lihat bagian rekomendasi di bawah.\n")
            
        print("\n───────────────────────────────────────────")

        if len(result["rekomendasi"]) > 0:
            print(f"\n  ◎ REKOMENDASI (Cocok Sebagian: {len(result["rekomendasi"])} Akun)\n\n")

            for idx, res in enumerate(result["rekomendasi"]):
                data2 = data.iloc[res["index"]]
                print(f"    • {data2["Name"]}") 
                buttons_parameter.append({"Nama": data2["Name"], "command":f"{idx +1}", "function":lambda id=data2["ID"]: Fitur_Detail_Akun_berdasarkan(id,"ID")})
        else:
            print("\n  ◎ TIDAK ADA REKOMENDASI")
            print("───────────────────────────────────────────\n\n")
        print("\n\n")
        buttons(buttons_parameter)  
        mencari =""
        break