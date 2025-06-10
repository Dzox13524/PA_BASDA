import pandas as pd
from Fitur.Umum.controler import clear_terminal

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

def Fitur_Hapus_Buku(ISBN):
    data = pd.read_csv("./database/Buku.csv")
    hasil_idx = pencarian(data, "ISBN", ISBN)
    if hasil_idx is None:
        input(f"[ERROR] Buku dengan ISBN '{ISBN}' tidak ditemukan.")
        return
    clear_terminal()
    judul = data.loc[hasil_idx, "JudulBuku"]
    data = data.drop(index=hasil_idx).reset_index(drop=True)
    data.to_csv("database/Buku.csv", index=False)
    input(f"Buku {judul} Berhasil Dihapus!")