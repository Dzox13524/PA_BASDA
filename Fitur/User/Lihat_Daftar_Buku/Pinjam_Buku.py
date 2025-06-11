import config
import pandas as pd
from controler import clear_terminal, buttons

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

def Pinjam_Buku(ISBN, Waktu):
    data = pd.read_csv("./database/Buku.csv")
    pinjam = pd.read_csv("./database/Peminjaman.csv")
    hasil_idx = pencarian(data, "ISBN", ISBN)
    if hasil_idx is None:
        input(f"[ERROR] Buku dengan ISBN '{ISBN}' tidak ditemukan.")
        return
    clear_terminal()
    No = len(pd.DataFrame(pinjam))
    Newdata = {
        'ID': f"P{No:03d}",
        'ID_User': config.ID_Akun,
        'ISBN':ISBN,
        'Durasi_Peminjaman':Waktu,
        'Tanggal_Meminjam':None,
        'Status_Pengembalian':"Permintaan_Peminjaman",
        'Tanggal_Kembali':None
            }
    datanew = pd.DataFrame([Newdata])
    datanew.to_csv("./database/Peminjaman.csv",mode='a',header=False ,index=False)
    data.loc[hasil_idx, "Stok"] -= 1
    data.to_csv("database/Buku.csv", index=False)
    input(f"Berhasil Meminjam Buku {data.loc[hasil_idx, "JudulBuku"]} Selama {Waktu} Hari!")


def Fitur_Pinjam_Buku(ISBN):
    data = pd.read_csv("./database/Buku.csv")
    hasil_idx = pencarian(data, "ISBN", ISBN)
    clear_terminal()
    print(f"Kamu Ingin Meminjam {data.loc[hasil_idx, "JudulBuku"]} Berapa Hari ?")
    buttons_parameter = []
    waktu = [3,5,7]
    for i,data in enumerate(waktu):
        buttons_parameter.append({"Nama": f"{data} Hari", "command":str(i+1), "function":lambda x = data:Pinjam_Buku(ISBN, x)})
    buttons(buttons_parameter)