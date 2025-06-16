import config

from controler import clear_terminal,buttons,Pencarian_String
from Fitur.Admin.Pengelolaan_Data_Buku.Hapus_Buku import Fitur_Hapus_Buku
from Fitur.Admin.Pengelolaan_Data_Buku.Tambah_Stok_Buku import Fitur_Tambah_Stok_Buku
from Fitur.Admin.Pengelolaan_Data_Buku.List_Buku import sorted_data

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
    hasil = Pencarian_String(sorted_data(urutan), urutan, idx)
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