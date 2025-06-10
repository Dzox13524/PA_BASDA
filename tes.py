# # # import pandas as pd
# # # from tabulate import tabulate
# # # from Fitur.Umum.controler import clear_terminal

# # # def shaker_sort(arr, key_list):
# # #     kiri = 0
# # #     kanan = len(arr) - 1
# # #     while kiri < kanan:
# # #         for i in range(kiri, kanan):
# # #             if key_list[arr[i]] > key_list[arr[i+1]]:
# # #                 arr[i], arr[i+1] = arr[i+1], arr[i]
# # #         kanan -= 1
# # #         for i in range(kanan, kiri, -1):
# # #             if key_list[arr[i]] < key_list[arr[i-1]]:
# # #                 arr[i], arr[i-1] = arr[i-1], arr[i]
# # #         kiri += 1

# # # data = pd.read_csv("database/Akun.csv")

# # # def sorted_data(urutan):
# # #     usernames = data[urutan].tolist()
# # #     indices = list(range(len(usernames)))
# # #     shaker_sort(indices, usernames)
# # #     sorted_data = data.iloc[indices].reset_index(drop=True)
# # #     sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
# # #     return sorted_data

# # # def Fitur_list_akun(urutan, awal, akhir):
# # #     halaman = 1
# # #     total_halaman = (len(data) + 50 - 1) // 50
# # #     usernames = data[urutan].tolist()
# # #     indices = list(range(len(usernames)))
# # #     shaker_sort(indices, usernames)
# # #     sorted_data = data.iloc[indices].reset_index(drop=True)[awal:akhir]
# # #     sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
# # #     clear_terminal()
# # #     result = tabulate(sorted_data[["No", "Name", "Email", "Nomor_Telepon", "Kecamatan", "Desa"]], headers=["No","Nama","Email","Nomor Hp","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
# # #     result += f"\nTotal User: {len(usernames)} | Halaman {halaman} dari {total_halaman}"
# # #     return result
# # # print(list_akun("Name", 0, 50))

# # # def tes (parameter):
# # #     print(parameter)

# # # def buttons(buttons_info =[]):
# # #     text = '--- PILIH OPSI ---\n\n'
# # #     for idx, data in enumerate(buttons_info):
# # #         text += f"[{idx+1}] {data["Nama"]}\n"
# # #     text += "[K] keluar\n\n"
# # #     text += "---"
# # #     while True:
# # #         print(text)
# # #         pilihan = input("Masukkan Pilihan Anda: ")
# # #         for idx, data in enumerate(buttons_info):
# # #             if pilihan ==str(idx + 1):
# # #                 data["function"]()
# # #                 break
# # #             if pilihan == "k":
# # #                 return

# # # buttons([{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes}])
# # import config
# # import pandas as pd
# # from Fitur.Umum.controler import clear_terminal,buttons
# # from Fitur.Admin.Pengelolaan_Akun_Pengguna.Hapus_Akun import Fitur_Hapus_Akun
# # from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import sorted_data

# # def buat_tabel_bad_character(pola):
# #     tabel = {}
# #     panjang = len(pola)
# #     for i in range(panjang - 1):
# #         tabel[pola[i]] = panjang - 1 - i
# #     return tabel

# # def boyer_moore_cocok(teks, pola):
# #     panjang_teks = len(teks)
# #     panjang_pola = len(pola)

# #     if panjang_pola == 0:
# #         return True

# #     tabel = buat_tabel_bad_character(pola)
# #     posisi = 0

# #     while posisi <= panjang_teks - panjang_pola:
# #         indeks = panjang_pola - 1

# #         while indeks >= 0 and pola[indeks] == teks[posisi + indeks]:
# #             indeks -= 1

# #         if indeks < 0:
# #             return True
# #         else:
# #             karakter = teks[posisi + indeks]
# #             if karakter in tabel:
# #                 lompat = tabel[karakter]
# #             else:
# #                 lompat = panjang_pola
# #             posisi += max(1, lompat)
# #     return False

# # def pencarian(data, berdasarkan, dicari):
# #     data_list = data[berdasarkan].tolist()
# #     hasil = ''
# #     for idx, item in enumerate(data_list):
# #            if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
# #                hasil = idx

# #     return hasil

# # def Fitur_Detail_Akun(idx, urutan= config.urutanUser):
# #     hasil = pencarian(sorted_data(urutan), urutan, idx)
# #     data = sorted_data(urutan).iloc[hasil]
# #     clear_terminal()
# #     print("───────────────────────────────────────────")
# #     print(f"  DATA AKUN {data['Name']}:")
# #     print("───────────────────────────────────────────")
# #     print(f"    ID Akun    : {data['ID']}")
# #     print(f"    Nama       : {data['Name']}")
# #     print(f"    Email      : {data['Email']}")
# #     print(f"    Kecamatan  : {data['Kecamatan']}")
# #     print(f"    Desa       : {data['Desa']}")
# #     buttons_parameter = []
# #     buttons_parameter.append({"Nama": "Hapus Akun", "command":"1", "function":lambda idx=idx:Fitur_Hapus_Akun(idx)})
# #     buttons(buttons_parameter)
# # Fitur_Detail_Akun(12, "ID")
# # # print(pencarian(sorted_data("Name"), "Name", "amat"))
# # # print(sorted_data("Name").iloc[5])
# # # print(sorted_data("ID")["Name"])

# # import pandas as pd
# # from tabulate import tabulate

# # lokasiDB = "database/"  # Sesuaikan jika lokasimu beda

# # def Fitur_List_Peminjaman_Buku():
# #     awal = 0
# #     akhir = 50
# #     halaman = 1
# #     loop = True
# #     while loop:
# #         def lanjut():
# #             nonlocal awal, akhir, halaman
# #             awal = akhir
# #             akhir += 50
# #             halaman += 1
# #             return
    
# #         def kembali():
# #             nonlocal awal, akhir, halaman
# #             akhir = awal
# #             awal = akhir - 50
# #             halaman -= 1
# #             return
# #         peminjaman = pd.read_csv("database/Peminjaman.csv")
# #         user = pd.read_csv("database/Akun.csv")
# #         buku = pd.read_csv("database/Buku.csv")


# #         gabung_buku = pd.merge(peminjaman, buku[['ISBN', 'JudulBuku', 'Stok']], on='ISBN', how='left')
# #         gabung_semua = pd.merge(gabung_buku, user[['ID', 'Name']], left_on='ID_User', right_on='ID', how='left')

# #         daftar = gabung_semua
# #         total_halaman = (len(daftar) + 50 - 1) // 50
# #         tabel_data = daftar[[
# #             'JudulBuku', 'Name', 'Tanggal_Meminjam', 'Status_Pengembalian', "Tanggal_Kembali"
# #         ]][awal:akhir]
# #         tabel_data.insert(0, "No", range(1, len(tabel_data) + 1))

# #         tabel_data.columns = [
# #             "No", 'Judul Buku', 'Nama User', 'Tanggal Peminjaman', 'Status', 'Tanggal Kembali'
# #         ]
# #         tabel_data['Tanggal Kembali'] = tabel_data['Tanggal Kembali'].fillna('-')


# #         print(tabulate(tabel_data, headers='keys', tablefmt='fancy_grid', showindex=False))
# #         print(f"\nTotal Peminjaman: {len(daftar)} | Halaman {halaman} dari {total_halaman}")
# #         buttons_parameter = []
# #         if halaman == 1:
# #             buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command":"l", "function":lanjut})
# #         elif halaman < total_halaman:
# #             buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command":"p", "function":kembali})
# #             buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command":"l", "function":lanjut})
# #         else:
# #             buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command":"p", "function":kembali})
        
# #         buttons(buttons_parameter)

# # Fitur_List_Peminjaman_Buku()
# # import pandas as pd
# # from datetime import datetime, timedelta
# # def buat_tabel_bad_character(pola):
# #     tabel = {}
# #     panjang = len(pola)
# #     for i in range(panjang - 1):
# #         tabel[pola[i]] = panjang - 1 - i
# #     return tabel

# # def boyer_moore_cocok(teks, pola):
# #     panjang_teks = len(teks)
# #     panjang_pola = len(pola)

# #     if panjang_pola == 0:
# #         return True

# #     tabel = buat_tabel_bad_character(pola)
# #     posisi = 0

# #     while posisi <= panjang_teks - panjang_pola:
# #         indeks = panjang_pola - 1

# #         while indeks >= 0 and pola[indeks] == teks[posisi + indeks]:
# #             indeks -= 1

# #         if indeks < 0:
# #             return True
# #         else:
# #             karakter = teks[posisi + indeks]
# #             if karakter in tabel:
# #                 lompat = tabel[karakter]
# #             else:
# #                 lompat = panjang_pola
# #             posisi += max(1, lompat)
# #     return False

# # def pencarian(data, berdasarkan, dicari):
# #     data_list = data[berdasarkan].tolist()
# #     hasil = ''
# #     for idx, item in enumerate(data_list):
# #            if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
# #                hasil = idx

# #     return hasil

# # def shaker_sort(arr, key_dict):
# #     kiri = 0
# #     kanan = len(arr) - 1
# #     while kiri < kanan:
# #         for i in range(kiri, kanan):
# #             if key_dict[arr[i]] < key_dict[arr[i+1]]:  # descending
# #                 arr[i], arr[i+1] = arr[i+1], arr[i]
# #         kanan -= 1
# #         for i in range(kanan, kiri, -1):
# #             if key_dict[arr[i]] > key_dict[arr[i-1]]:  # descending
# #                 arr[i], arr[i-1] = arr[i-1], arr[i]
# #         kiri += 1


# # def Fitur_Top_Peminjaman_Buku():
# #     inputan = '3'
    
# #     peminjaman = pd.read_csv("database/Peminjaman.csv")
# #     buku = pd.read_csv("database/Buku.csv")

# #     gabung = pd.merge(peminjaman, buku[['ISBN', 'JudulBuku']], on='ISBN', how='left')
# #     gabung = gabung[gabung['Status_Pengembalian'] != "Permintaan_Peminjaman"]

# #     gabung['Tanggal_Meminjam'] = pd.to_datetime(gabung['Tanggal_Meminjam'], errors='coerce')

# #     sekarang = datetime.now()
# #     if inputan == '1':
# #         batas = sekarang - timedelta(days=7)
# #         gabung = gabung[gabung['Tanggal_Meminjam'] >= batas]
# #         judul_output = "Top Peminjaman Buku Mingguan"
# #     elif inputan == '2':
# #         batas = sekarang - timedelta(days=30)
# #         gabung = gabung[gabung['Tanggal_Meminjam'] >= batas]
# #         judul_output = "Top Peminjaman Buku Bulanan"
# #     elif inputan == '3':
# #         judul_output = "Top Peminjaman Buku Sepanjang Waktu"
# #     else:
# #         input("Pilihan Tidak Ada!")
# #         return
# #     jumlah_peminjaman = {}
# #     for i in gabung.to_dict(orient='records'):
# #         judul = i["JudulBuku"]
# #         jumlah_peminjaman[judul] = jumlah_peminjaman.get(judul, 0) + 1


# #     judul_list = list(jumlah_peminjaman.keys())
# #     shaker_sort(judul_list, jumlah_peminjaman)
# #     print(f"\n--- {judul_output} (5 Teratas) ---")
# #     print("--------------------------------------------------\n")
# #     if len(judul_list) > 0:
# #         for idx, judul in enumerate(judul_list[:5], start=1):
# #             indeks_buku = pencarian(buku, 'JudulBuku', judul)
# #             print(f"{idx}. Judul Buku  : {buku["JudulBuku"][indeks_buku]}")
# #             print(f"   Penulis     : {buku["Penulis"][indeks_buku]}")
# #             print(f"   Genre       : {buku["Genre"][indeks_buku]}")
# #             print(f"   Dipinjam    : {jumlah_peminjaman[judul]} kali")
# #             print(f"   ISBN        : {buku["ISBN"][indeks_buku]}\n")
# #     else: 
# #         print("Tidak Ada Peminjaman")


# #     # hasil = pencarian(gabung, "ISBN", )
# #     # clear_terminal()
# #     # print("\n=== Top Peminjaman Buku ({}) ===\n".format(jenis.capitalize()))
# #     # print(tabulate(top_buku, headers='keys', tablefmt='fancy_grid', showindex=False))
# # Fitur_Top_Peminjaman_Buku()
# import config
# import pandas as pd
# from datetime import datetime, timedelta
# from Fitur.Umum.controler import clear_terminal, buttons

# def buat_tabel_bad_character(pola):
#     tabel = {}
#     panjang = len(pola)
#     for i in range(panjang - 1):
#         tabel[pola[i]] = panjang - 1 - i
#     return tabel

# def boyer_moore_cocok(teks, pola):
#     panjang_teks = len(teks)
#     panjang_pola = len(pola)

#     if panjang_pola == 0:
#         return True

#     tabel = buat_tabel_bad_character(pola)
#     posisi = 0

#     while posisi <= panjang_teks - panjang_pola:
#         indeks = panjang_pola - 1

#         while indeks >= 0 and pola[indeks] == teks[posisi + indeks]:
#             indeks -= 1

#         if indeks < 0:
#             return True
#         else:
#             karakter = teks[posisi + indeks]
#             if karakter in tabel:
#                 lompat = tabel[karakter]
#             else:
#                 lompat = panjang_pola
#             posisi += max(1, lompat)
#     return False

# def pencarian(data, berdasarkan, dicari):
#     data_list = data[berdasarkan].tolist()
#     hasil = ''
#     for idx, item in enumerate(data_list):
#            if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
#                hasil = idx

#     return hasil

# def Pinjam_Buku(ISBN, Waktu):

#     tanggal_pinjam = datetime.today()
#     tanggal_pinjam_str = tanggal_pinjam.strftime('%Y-%m-%d')
#     tanggal_kembali = tanggal_pinjam + timedelta(days=Waktu)
#     tanggal_kembali_str = tanggal_kembali.strftime('%Y-%m-%d')


#     data = pd.read_csv("./database/Buku.csv")
#     pinjam = pd.read_csv("./database/Peminjaman.csv")
#     hasil_idx = pencarian(data, "ISBN", ISBN)
#     if hasil_idx is None:
#         input(f"[ERROR] Buku dengan ISBN '{ISBN}' tidak ditemukan.")
#         return
#     clear_terminal()
#     No = len(pd.DataFrame(pinjam))
#     Newdata = {
#         'ID': f"P{No:03d}",
#         'ID_User': config.ID_Akun,
#         'ISBN':ISBN,
#         'Tanggal_Meminjam':tanggal_pinjam_str,
#         'Status_Pengembalian':None,
#         'Tanggal_Kembali':tanggal_kembali_str
#             }
#     datanew = pd.DataFrame([Newdata])
#     datanew.to_csv("./database/Peminjaman.csv",mode='a',header=False ,index=False)
#     data.loc[hasil_idx, "Stok"] -= 1
#     data.to_csv("database/Buku.csv", index=False)
#     input(f"Berhasil Meminjam Buku {data.loc[hasil_idx, "JudulBuku"]}")


# def Fitur_Pinjam_Buku(ISBN):
#     data = pd.read_csv("./database/Buku.csv")
#     hasil_idx = pencarian(data, "ISBN", ISBN)
#     print(f"Kamu Ingin Meminjam {data.loc[hasil_idx, "JudulBuku"]} Berapa Hari ?")
#     buttons_parameter = []
#     waktu = [3,5,7]
#     for i,data in enumerate(waktu):
#         buttons_parameter.append({"Nama": f"{data} Hari", "command":str(i+1), "function":lambda x = data:Pinjam_Buku(ISBN, x)})
#     buttons(buttons_parameter)

import pandas as pd
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
    hasil = []
    for idx, item in enumerate(data_list):
        if boyer_moore_cocok(str(item), str(dicari)):
            if str(item) == str(dicari):
                hasil.append(idx)
    return hasil

def Fitur_Riwayat_Peminjaman(ID):
    data = pd.read_csv("./database/Peminjaman.csv")
    buku = pd.read_csv("./database/Buku.csv")
    res = pencarian(data, "ID_User", ID)
    Judul = []

    for i in res:
        Judul.append(buku["JudulBuku"][pencarian(buku, "ISBN", data["ISBN"][i])].values[0])

    
    print(Judul)

        
Fitur_Riwayat_Peminjaman(2)