import config

from Fitur.Umum.controler import clear_terminal,buttons
from Fitur.Admin.Pengelolaan_Data_Buku.Hapus_Buku import Fitur_Hapus_Buku
from Fitur.Admin.Pengelolaan_Data_Buku.Tambah_Stok_Buku import Fitur_Tambah_Stok_Buku
from Fitur.Admin.Pengelolaan_Data_Buku.List_Buku import sorted_data

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

def Fitur_Detail_Buku(idx, urutan =config.urutanBuku):
    data = sorted_data(urutan)
    clear_terminal()
    print("───────────────────────────────────────────")
    print(f"  DATA BUKU {data.iloc[idx]['JudulBuku']}:")
    print("───────────────────────────────────────────")
    print(f"    ISBN           : {data.iloc[idx]['ISBN']}")
    print(f"    Judul          : {data.iloc[idx]['JudulBuku']}")
    print(f"    Penulis        : {data.iloc[idx]['Penulis']}")
    print(f"    Penerbit       : {data.iloc[idx]['Penerbit']}")
    print(f"    Jumlah Halaman : {data.iloc[idx]['JumlahHalaman']}")
    print(f"    Genre          : {data.iloc[idx]['Genre']}")
    print(f"    Tahun Terbit   : {data.iloc[idx]['TahunTerbit']}")
    print(f"    Stok           : {data.iloc[idx]['Stok']}")
    print(f"    Tanggal Masuk  : {data.iloc[idx]['TanggalMasuk']}")
    print(f"    Ketersediaan   : {data.iloc[idx]['Ketersediaan']}")
    print(f"    Deskripsi      : {data.iloc[idx]['Deskripsi']}")
    print(f"    Ketersediaan   : {data.iloc[idx]['Ketersediaan']}")
    buttons_parameter = []
    buttons_parameter.append({"Nama": "Hapus Buku", "command":"1", "function":lambda idx=data.iloc[idx]['ISBN']:Fitur_Hapus_Buku(idx)})
    buttons_parameter.append({"Nama": "Tambah Stok Buku", "command":"2", "function":lambda idx=data.iloc[idx]['ISBN']:Fitur_Tambah_Stok_Buku(idx)})

    buttons(buttons_parameter)

def Fitur_Detail_Buku_berdasarkan(idx, urutan= config.urutanUser):
    hasil = pencarian(sorted_data(urutan), urutan, idx)
    data = sorted_data(urutan).iloc[hasil]
    clear_terminal()
    print("───────────────────────────────────────────")
    print(f"  DATA BUKU {data['JudulBuku']}:")
    print("───────────────────────────────────────────")
    print(f"    ISBN           : {data['ISBN']}")
    print(f"    Judul          : {data['JudulBuku']}")
    print(f"    Penulis        : {data['Penulis']}")
    print(f"    Penerbit       : {data['Penerbit']}")
    print(f"    Jumlah Halaman : {data['JumlahHalaman']}")
    print(f"    Genre          : {data['Genre']}")
    print(f"    Tahun Terbit   : {data['TahunTerbit']}")
    print(f"    Stok           : {data['Stok']}")
    print(f"    Tanggal Masuk  : {data['TanggalMasuk']}")
    print(f"    Ketersediaan   : {data['Ketersediaan']}")
    print(f"    Deskripsi      : {data['Deskripsi']}")
    print(f"    Ketersediaan   : {data['Ketersediaan']}\n")
    buttons_parameter = []
    buttons_parameter.append({"Nama": "Hapus Buku", "command":"1", "function":lambda idx=data['ISBN']:Fitur_Hapus_Buku(idx)})
    buttons_parameter.append({"Nama": "Tambah Stok Buku", "command":"2", "function":lambda idx=data['ISBN']:Fitur_Tambah_Stok_Buku(idx)})
    buttons(buttons_parameter)