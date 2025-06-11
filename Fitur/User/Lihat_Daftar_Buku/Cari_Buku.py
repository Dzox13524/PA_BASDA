import pandas as pd
from controler import clear_terminal,buttons,Pencarian_Dengan_Rekomendasi
from Fitur.User.Lihat_Daftar_Buku.Detail_Buku import Fitur_Detail_Buku_berdasarkan
from Fitur.User.Lihat_Daftar_Buku.Pinjam_Buku import Fitur_Pinjam_Buku

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
        result = Pencarian_Dengan_Rekomendasi(data, mencari, yang_dicari)
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
                buttons_parameter.append({"Nama": "Pinjam Buku " + data1["JudulBuku"], "command":"p" + str(idx +1), "function":lambda isbn = data1['ISBN']:Fitur_Pinjam_Buku(isbn)})
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