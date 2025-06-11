import pandas as pd
from controler import clear_terminal,buttons,Pencarian_Dengan_Rekomendasi
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Detail_Akun import Fitur_Detail_Akun_berdasarkan
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Hapus_Akun import Fitur_Hapus_Akun

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
        result = Pencarian_Dengan_Rekomendasi(data, mencari, yang_dicari)
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