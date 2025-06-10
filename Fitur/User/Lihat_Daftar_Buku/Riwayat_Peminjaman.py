import config
import pandas as pd
from tabulate import tabulate
from controler import clear_terminal, buttons
from Fitur.User.Lihat_Daftar_Buku.Mengembalikan_Buku import Fitur_Mengembalikan_Buku, Fitur_Membatalkan_Peminjaman_Buku

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

def Fitur_Riwayat_Peminjaman(ID = config.ID_Akun):
    data = pd.read_csv("./database/Peminjaman.csv", dtype={"ISBN": str})
    buku = pd.read_csv("./database/Buku.csv", dtype={"ISBN": str})
    res = pencarian(data, "ID_User", ID)
    daftar_judul = []
    clear_terminal()
    print("======== Data Peminjaman Buku ========\n")
    buttons_parameter = []
    if len(res) > 0:
        for idx, datas in enumerate(res):
            isbn = data.loc[datas, "ISBN"]
            idx_Buku = pencarian(buku, "ISBN", isbn)
            judul = buku.loc[idx_Buku, "JudulBuku"].values[0]
            tanggal_pinjam = data.loc[datas, "Tanggal_Meminjam"] if "Tanggal_Meminjam" in data.columns else "-"
            tanggal_kembali = data.loc[datas, "Tanggal_Kembali"] if "Tanggal_Kembali" in data.columns else "-"
            status = data.loc[datas, "Status_Pengembalian"] if "Status_Pengembalian" in data.columns else "-"
            daftar_judul.append([len(daftar_judul)+1, judul, isbn, tanggal_pinjam, tanggal_kembali, status])
            if status == 'Dipinjam':
                buttons_parameter.append({"Nama": f"Ajukan pengembalian Buku {judul}", "command":str(idx+1), "function":lambda idx = datas, judul = judul:Fitur_Mengembalikan_Buku(idx, judul)})
            elif status == 'Permintaan_Peminjaman':
                buttons_parameter.append({"Nama": f"Batalkan Peminjaman Buku {judul}", "command":str(idx+1), "function":lambda idx = datas, judul = judul:Fitur_Membatalkan_Peminjaman_Buku(idx, judul, idx_Buku)})
        headers = ["No", "Judul Buku", "ISBN", "Tanggal Pinjam", "Tanggal Kembali", "Status"]
        if len(buttons_parameter) > 0:
            print(tabulate(daftar_judul, headers=headers, tablefmt="fancy_grid"))
            buttons(buttons_parameter)
        else:
            input(tabulate(daftar_judul, headers=headers, tablefmt="fancy_grid"))
    else:
        input("Kamu Belum Meminjam Buku Apapun!")
        