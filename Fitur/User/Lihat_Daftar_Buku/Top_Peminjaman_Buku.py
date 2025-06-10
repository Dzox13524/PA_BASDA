import pandas as pd
from datetime import datetime, timedelta
from Fitur.Umum.controler import clear_terminal, buttons
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
    hasil = ''
    for idx, item in enumerate(data_list):
           if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
               hasil = idx

    return hasil

def shaker_sort(arr, key_dict):
    kiri = 0
    kanan = len(arr) - 1
    while kiri < kanan:
        for i in range(kiri, kanan):
            if key_dict[arr[i]] < key_dict[arr[i+1]]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        kanan -= 1
        for i in range(kanan, kiri, -1):
            if key_dict[arr[i]] > key_dict[arr[i-1]]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        kiri += 1

def Fitur_Top_Peminjaman_Buku():
    clear_terminal()
    print("Pilih periode top peminjaman buku:")
    print("1. Mingguan")
    print("2. Bulanan")
    print("3. Sepanjang Waktu")

    while True:
        inputan = input("Masukkan pilihan (1/2/3): ").strip()
        if inputan in ['1', '2', '3']:
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

    
    peminjaman = pd.read_csv("database/Peminjaman.csv")
    buku = pd.read_csv("database/Buku.csv")

    gabung = pd.merge(peminjaman, buku[['ISBN', 'JudulBuku']], on='ISBN', how='left')
    gabung = gabung[gabung['Status_Pengembalian'] != "Permintaan_Peminjaman"]

    gabung['Tanggal_Meminjam'] = pd.to_datetime(gabung['Tanggal_Meminjam'], errors='coerce')

    sekarang = datetime.now()
    if inputan == '1':
        batas = sekarang - timedelta(days=7)
        gabung = gabung[gabung['Tanggal_Meminjam'] >= batas]
        judul_output = "Top Peminjaman Buku Mingguan"
    elif inputan == '2':
        batas = sekarang - timedelta(days=30)
        gabung = gabung[gabung['Tanggal_Meminjam'] >= batas]
        judul_output = "Top Peminjaman Buku Bulanan"
    elif inputan == '3':
        judul_output = "Top Peminjaman Buku Sepanjang Waktu"
    else:
        input("Pilihan Tidak Ada!")
        return
    jumlah_peminjaman = {}
    for i in gabung.to_dict(orient='records'):
        judul = i["JudulBuku"]
        jumlah_peminjaman[judul] = jumlah_peminjaman.get(judul, 0) + 1

    judul_list = list(jumlah_peminjaman.keys())
    shaker_sort(judul_list, jumlah_peminjaman)
    buttons_parameter = []
    clear_terminal()
    print(f"\n--- {judul_output} (5 Teratas) ---")
    print("--------------------------------------------------\n")
    if len(judul_list) > 0:
        for idx, judul in enumerate(judul_list[:5], start=1):
            indeks_buku = pencarian(buku, 'JudulBuku', judul)
            print(f"{idx}. Judul Buku  : {buku["JudulBuku"][indeks_buku]}")
            print(f"   Penulis     : {buku["Penulis"][indeks_buku]}")
            print(f"   Genre       : {buku["Genre"][indeks_buku]}")
            print(f"   Dipinjam    : {jumlah_peminjaman[judul]} kali")
            print(f"   ISBN        : {buku["ISBN"][indeks_buku]}\n")
            buttons_parameter.append({"Nama": buku["JudulBuku"][indeks_buku], "command":f"{idx}", "function":lambda id=buku["ISBN"][indeks_buku]: Fitur_Detail_Buku_berdasarkan(id, "ISBN")})
    else: 
        print("Tidak Ada Peminjaman")
    buttons(buttons_parameter)

# import pandas as pd
# from tabulate import tabulate
# from Fitur.Umum.controler import clear_terminal

# def shaker_sort(arr, key_list):
#     kiri = 0
#     kanan = len(arr) - 1
#     while kiri < kanan:
#         for i in range(kiri, kanan):
#             if key_list[arr[i]] > key_list[arr[i+1]]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#         kanan -= 1
#         for i in range(kanan, kiri, -1):
#             if key_list[arr[i]] < key_list[arr[i-1]]:
#                 arr[i], arr[i-1] = arr[i-1], arr[i]
#         kiri += 1

# data = pd.read_csv("database/Buku.csv")

# def sorted_data(urutan):
#     usernames = data[urutan].tolist()
#     indices = list(range(len(usernames)))
#     shaker_sort(indices, usernames)
#     sorted_data = data.iloc[indices].reset_index(drop=True)
#     sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
#     return sorted_data

# def list_buku(urutan):
#     awal = 0
#     akhir= 50
#     halaman = 1
#     total_halaman = (len(data) + 50 - 1) // 50
#     usernames = data[urutan].tolist()
#     indices = list(range(len(usernames)))
#     shaker_sort(indices, usernames)
#     sorted_data = data.iloc[indices].reset_index(drop=True)
#     sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
#     kolom_ditampilkan = ["No","ISBN", "JudulBuku", "Penulis", "Genre", "TahunTerbit", "Stok"]
#     while True:
#         clear_terminal()
#         tampil_data = sorted_data[awal:akhir][kolom_ditampilkan]
#         result = tabulate(tampil_data, headers="keys", tablefmt="fancy_grid", showindex=False, disable_numparse=True)
#         result += f"\n\nTotal User: {len(data)}\n"
#         result += f"Halaman {halaman} dari {total_halaman}\n"
#         result += "----------------------------------------\n"
#         if halaman == 1:
#             result += "Tekan [Enter] untuk kembali ke menu utama, ketik [N] untuk halaman selanjutnya\n"
#         elif halaman < total_halaman:
#             result += "Tekan [Enter] untuk kembali ke menu utama, ketik [N] untuk halaman selanjutnya, atau ketik [P] untuk halaman sebelumnya.\n"
#         else:
#             result += "Tekan [Enter] untuk kembali ke menu utama, atau ketik [P] untuk halaman sebelumnya.\n"
#         result += "----------------------------------------\n"
#         print(result)
#         inputan = input("Pilihan Anda: ").strip().lower()
#         if inputan == 'n' and halaman <= total_halaman:
#             awal = akhir
#             akhir += 50
#             halaman += 1
#             continue
#         elif inputan == 'p' and halaman > 1:
#             akhir = awal
#             awal = akhir - 50
#             halaman -= 1
#             continue
#         elif inputan == '':
#             break

# def Fitur_ListBuku():
#     while True:
#         clear_terminal()
#         print("""1. Urutkan berdasarkan ISBN
# 2. Urutkan Berdasar Judul
# 3. Urutkan Berdasarkan Tahun Terbit
# 4. Urutkan Berdasarkan Stok
# 5. Urutkan Berdasarkan Total Peminjaman
# 6. Keluar""")
#         pilihan = input("\nPilih [1-5]: ")
#         match pilihan:
#             case '1':
#                 clear_terminal()
#                 list_buku("ISBN")
#                 break
#             case '2':
#                 clear_terminal()
#                 list_buku("JudulBuku")
#                 break
#             case '3':
#                 clear_terminal()
#                 list_buku("TahunTerbit")
#                 break
#             case '4':
#                 clear_terminal()
#                 list_buku("Stok")
#                 break
#             case '5':
#                 clear_terminal()
#                 list_buku("TotalDipinjam")
#                 break
#             case '6':
#                 clear_terminal()
#                 input("Tekan [Enter] untuk kembali ke menu...")
#                 break
#             case _:
#                 clear_terminal()
#                 print("Pilihan tidak Valid! pilih angkat [1-5]")
#                 input("Tekan [Enter] untuk melanjutkan...")
#                 continue
