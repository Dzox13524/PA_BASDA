import pandas as pd
from tabulate import tabulate
from Fitur.Umum.controler import buttons,clear_terminal
from Fitur.Admin.Pengelolaan_Data_Buku.Tamplian_Peminjaman_Buku import Fitur_Tampilan_Peminjaman_Buku

def List_Peminjaman(status_filter, awal, akhir, halaman):
    peminjaman = pd.read_csv("database/Peminjaman.csv")
    user = pd.read_csv("database/Akun.csv")
    buku = pd.read_csv("database/Buku.csv")


    gabung_buku = pd.merge(peminjaman, buku[['ISBN', 'JudulBuku', 'Stok']], on='ISBN', how='left')
    gabung_semua = pd.merge(gabung_buku, user[['ID', 'Name']], left_on='ID_User', right_on='ID', how='left')

    if status_filter:
        daftar = gabung_semua[gabung_semua['Status_Pengembalian'] == status_filter]
    else:
        daftar = gabung_semua
    total_halaman = (len(daftar) + 50 - 1) // 50
    tabel_data = daftar[[
        'JudulBuku', 'Name', 'Tanggal_Meminjam', 'Status_Pengembalian', "Tanggal_Kembali"
    ]][awal:akhir]
    tabel_data.insert(0, "No", range(1, len(tabel_data) + 1))

    tabel_data.columns = [
        "No", 'Judul Buku', 'Nama User', 'Tanggal Peminjaman', 'Status', 'Tanggal Kembali'
    ]
    tabel_data['Tanggal Kembali'] = tabel_data['Tanggal Kembali'].fillna('-')

    hasil = tabulate(tabel_data, headers='keys', tablefmt='fancy_grid', showindex=False)
    hasil += f"\nTotal Peminjaman: {len(daftar)} | Halaman {halaman} dari {total_halaman}"
    return hasil, total_halaman

def Fitur_List_Peminjaman_Buku():
    awal = 0
    akhir = 50
    halaman = 1
    loop = True
    while loop:
        def lanjut():
            nonlocal awal, akhir, halaman
            awal = akhir
            akhir += 50
            halaman += 1
            return
    
        def kembali():
            nonlocal awal, akhir, halaman
            akhir = awal
            awal = akhir - 50
            halaman -= 1
            return
        hasil, total_halaman =List_Peminjaman()
        print(hasil)
        buttons_parameter = []
        if halaman == 1:
            buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command":"l", "function":lanjut})
        elif halaman < total_halaman:
            buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command":"p", "function":kembali})
            buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command":"l", "function":lanjut})
        else:
            buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command":"p", "function":kembali})
        buttons_parameter.append({"Nama": "Tampilkan Data Berdasarkan", "command":"t", "function":Fitur_Tampilan_Peminjaman_Buku})
        buttons_parameter.append({"Nama": "Setujui Sema", "command":"t", "function":Fitur_Tampilan_Peminjaman_Buku})
        buttons(buttons_parameter)