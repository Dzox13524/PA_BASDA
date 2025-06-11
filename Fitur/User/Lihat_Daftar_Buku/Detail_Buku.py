import config

from controler import clear_terminal,buttons,Pencarian_String
from Fitur.Admin.Pengelolaan_Data_Buku.List_Buku import sorted_data
from Fitur.User.Lihat_Daftar_Buku.Pinjam_Buku import Fitur_Pinjam_Buku

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
    buttons_parameter.append({"Nama": "Pinjam Buku", "command":"1", "function":lambda x = data.iloc[idx]['ISBN']:Fitur_Pinjam_Buku(x)})
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
    buttons_parameter.append({"Nama": "Pinjam Buku", "command":"1", "function":lambda x = data['ISBN']:Fitur_Pinjam_Buku(int(x))})
    buttons(buttons_parameter)