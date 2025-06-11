import config
import pandas as pd
from tabulate import tabulate
from controler import clear_terminal, buttons, Pencarian_Hasil_List
from Fitur.User.Lihat_Daftar_Buku.Mengembalikan_Buku import Fitur_Mengembalikan_Buku, Fitur_Membatalkan_Peminjaman_Buku

def Fitur_Riwayat_Peminjaman(ID = config.ID_Akun):
    data = pd.read_csv("./database/Peminjaman.csv", dtype={"ISBN": str})
    buku = pd.read_csv("./database/Buku.csv", dtype={"ISBN": str})
    res = Pencarian_Hasil_List(data, "ID_User", ID)
    daftar_judul = []
    clear_terminal()
    print("======== Data Peminjaman Buku ========\n")
    buttons_parameter = []
    if len(res) > 0:
        for idx, datas in enumerate(res):
            isbn = data.loc[datas, "ISBN"]
            idx_Buku = Pencarian_Hasil_List(buku, "ISBN", isbn)
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
        