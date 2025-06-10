import config
import pandas as pd
from datetime import datetime, timedelta
from Fitur.Umum.controler import clear_terminal, buttons

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
           if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
               hasil.append(idx)

    return hasil


def Fitur_Riwayat_Peminjaman(ID):
    data = pd.read_csv("./database/Peminjaman.csv")
    
    pencarian()
    pass

# import pandas as pd
# import os
# from tabulate import tabulate
# from Fitur.Umum.controler import clear_terminal

# filePeminjaman = "database/Peminjaman.csv"
        
# def lihatRiwayatPeminjaman():
#     clear_terminal()

#     print(f"""╔───────────────────────────────────────────────────╗
# ║               APLIKASI PERPUSTAKAAN               ║
# ║            === RIWAYAT PEMINJAMAN ===             ║
# ╚───────────────────────────────────────────────────╝
# """.strip())

#     try:
#         df = pd.read_csv(filePeminjaman)

#         if df.empty:
#             print("Tidak ada data!\n")
#             input("Tekan Enter untuk kembali...")
#             clear_terminal()
#             return

#         total_data = len(df)
#         if total_data > 100:
#             page_size = 20
#             current_page = 0
#             while True:
#                 clear_terminal()
#                 print(f"""╔───────────────────────────────────────────────────╗
# ║               APLIKASI PERPUSTAKAAN               ║
# ║            === RIWAYAT PEMINJAMAN ===             ║
# ╚───────────────────────────────────────────────────╝
# """.strip())

#                 start_idx = current_page * page_size
#                 end_idx = start_idx + page_size
#                 page_data = df.iloc[start_idx:end_idx]

#                 table_data = []
#                 for i, row in page_data.iterrows():
#                     table_data.append([
#                         i + 1, row["ID_User"], row["ID_Buku"], row["Tanggal_Memintam"], row["Status_Pengembalian"], row["Tanggal_Kembali"]
#                     ])

#                 headers = ["No.", "ID User", "ID Buku", "Tanggal Meminjam", "Status", "Tanggal Pengembalian"]
#                 print(tabulate(table_data, headers=headers, tablefmt="grid"))
#                 print("="*115)

#                 # Jika sudah di halaman terakhir, tidak perlu opsi next
#                 if end_idx >= total_data:
#                     print("Anda telah berada di halaman terakhir.")
#                     input("Tekan Enter untuk kembali...")
#                     clear_terminal()
#                     break

#                 user_input = input("Tekan [Enter] untuk kembali ke menu utama, ketik [N] untuk halaman selanjutnya: ").strip().lower()
#                 if user_input == 'n':
#                     current_page += 1
#                 else:
#                     clear_terminal()
#                     break

#         else:
#             # Jika data 100 atau kurang, tampilkan semua tanpa page
#             table_data = []
#             for i, row in df.iterrows():
#                 table_data.append([
#                     i + 1, row["ID_User"], row["ID_Buku"], row["Tanggal_Memintam"], row["Status_Pengembalian"], row["Tanggal_Kembali"]
#                 ])

#             headers = ["No.", "ID User", "ID Buku", "Tanggal Meminjam", "Status", "Tanggal Pengembalian"]
#             print(tabulate(table_data, headers=headers, tablefmt="grid"))
#             print("="*115)
#             print("\n")
#             input("Tekan Enter untuk lanjut...")
#             clear_terminal()

#     except IOError:
#         print("Anda belum pernah melakukan pemesanan!")
#         print("\n")
#         input("Tekan Enter untuk kembali...")
#         clear_terminal()
