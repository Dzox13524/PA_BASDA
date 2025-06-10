import pandas as pd
from Fitur.Umum.controler import clear_terminal,buttons
from Fitur.User.Lihat_Daftar_Buku.Detail_Buku import Fitur_Detail_Buku_berdasarkan

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
    hasil = {}
    hasil["rekomendasi"] = []
    hasil["cocok"] = []
    data_dicari = dicari.split(" ")
    for i in data_dicari:
        data_dicari = i.lower()

        for idx, item in enumerate(data_list):
            if boyer_moore_cocok(str(item).lower(), data_dicari):
                
                if str(item).lower() == dicari.lower():
                    hasil["cocok"].append({"ditemukan":item, "index":idx})
                else:
                    hasil["rekomendasi"].append({"ditemukan":item, "index":idx})

    return hasil

mencari = ""
def mencari_berdasarkan(berdasarkan):
    global mencari
    mencari = berdasarkan

def Fitur_Cari_Buku():
    global mencari
    loop = True
    data = pd.read_csv("database/Buku.csv")
    while loop:
        buttons_parameter = []
        clear_terminal()
        buttons_parameter.append({"Nama": "Berdasarkan ISBN", "command":"1", "function":lambda:mencari_berdasarkan("ISBN")})
        buttons_parameter.append({"Nama": "Berdasarkan Judul", "command":"2", "function":lambda:mencari_berdasarkan("JudulBuku")})
        buttons_parameter.append({"Nama": "Berdasarkan Penulis", "command":"3", "function":lambda:mencari_berdasarkan("Penulis")})
        buttons_parameter.append({"Nama": "Berdasarkan Penerbit", "command":"4", "function":lambda:mencari_berdasarkan("Penerbit")})
        buttons_parameter.append({"Nama": "Berdasarkan Jumlah Halaman", "command":"5", "function":lambda:mencari_berdasarkan("JumlahHalaman")})
        buttons_parameter.append({"Nama": "Berdasarkan Genre", "command":"6", "function":lambda:mencari_berdasarkan("Genre")})
        buttons_parameter.append({"Nama": "Berdasarkan Tahun Terbit", "command":"7", "function":lambda:mencari_berdasarkan("TahunTerbit")})
        buttons_parameter.append({"Nama": "Berdasarkan Stok", "command":"8", "function":lambda:mencari_berdasarkan("Stok")})
        buttons_parameter.append({"Nama": "Berdasarkan Total Dipinjam", "command":"9", "function":lambda:mencari_berdasarkan("TotalDipinjam")})
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
            print(f"\n  ◎ DATA DITEMUKAN ({len(result["cocok"])} BUKU)")
            for idx, res1 in enumerate(result["cocok"]):
                data1 = data.iloc[res1["index"]]
                print("\n───────────────────────────────────────────")
                print(f"    BUKU {idx + 1}:")
                print("───────────────────────────────────────────")
                print(f"    ISBN           : {data1['ISBN']}")
                print(f"    Judul          : {data1['JudulBuku']}")
                print(f"    Penulis        : {data1['Penulis']}")
                print(f"    Penerbit       : {data1['Penerbit']}")
                print(f"    Jumlah Halaman : {data1['JumlahHalaman']}")
                print(f"    Genre          : {data1['Genre']}")
                print(f"    Tahun Terbit   : {data1['TahunTerbit']}")
                print(f"    Stok           : {data1['Stok']}")
                print(f"    Tanggal Masuk  : {data1['TanggalMasuk']}")
                print(f"    Ketersediaan   : {data1['Ketersediaan']}")
                print(f"    Deskripsi      : {data1['Deskripsi']}")
                print(f"    Ketersediaan   : {data1['Ketersediaan']}")
                buttons_parameter.append({"Nama": "Pinjam Buku " + data1["JudulBuku"], "command":"p" + str(idx +1), "function":lambda:None})
        else:
            print("\n  ◎ DATA TIDAK DITEMUKAN\n\n")
            print(f"    Maaf, tidak ada buku yang cocok persis dengan kata kunci {yang_dicari}.\n    Coba periksa kembali ejaan Anda atau lihat bagian rekomendasi di bawah.\n")
            
        print("\n───────────────────────────────────────────")

        if len(result["rekomendasi"]) > 0:
            print(f"\n  ◎ REKOMENDASI (Cocok Sebagian: {len(result["rekomendasi"])} Buku)\n\n")

            for idx, res in enumerate(result["rekomendasi"]):
                data2 = data.iloc[res["index"]]
                print(f"    • {data2['JudulBuku']}") 
                buttons_parameter.append({"Nama": data2["JudulBuku"], "command":f"{idx +1}", "function":lambda id=data2["ISBN"]: Fitur_Detail_Buku_berdasarkan(id, "ISBN")})
        else:
            print("\n  ◎ TIDAK ADA REKOMENDASI")
            print("───────────────────────────────────────────\n\n")
        print("\n\n")
        buttons(buttons_parameter)
        mencari =""
        break