import os 
import config
import importlib
from Fitur.Umum.controler import buttons

from Fitur.Admin.Pengelolaan_Data_Buku.List_Buku import Fitur_list_buku
from Fitur.Admin.Pengelolaan_Data_Buku.Detail_Buku import Fitur_Detail_Buku


def menu_pengelolaan_Buku(urutan = config.urutanBuku):
    awal = 0
    akhir = 50
    halaman = 1
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
    loop = True
    while loop:
        result, total_buku, total_halaman = Fitur_list_buku(config.urutanBuku, awal, akhir, halaman)
        result += f"\nUrutan Berdasarkan [{config.urutanBuku}]\n"
        idx = 1
        buttons_parameter = []
        buttons_parameter.append({"Nama": f"Pilih [1 - {total_buku}] untuk melihat detail Buku", "command":[1, total_buku], "function":Fitur_Detail_Buku})
        for i in os.listdir("./fitur/Admin/Pengelolaan_Data_Buku"):
            if i.endswith(".py") and i not in ["Menu_Pengelolaan_Buku.py","List_Buku.py", "Detail_Buku.py", "Hapus_Buku.py", "Tambah_Stok_Buku.py", "Tamplian_Peminjaman_Buku.py"]:
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                modul_path = f"Fitur.Admin.Pengelolaan_Data_Buku.{i.replace(".py", "")}"
                modul = importlib.import_module(modul_path)
                if nama[0].lower() not in [btn["command"] for btn in buttons_parameter]:
                    buttons_parameter.append({"Nama": nama, "command":nama[0].lower(), "function":getattr(modul, f"Fitur_{i.replace(".py", "")}")})
                else: 
                    buttons_parameter.append({"Nama": nama, "command":nama[0:2].lower(), "function":getattr(modul, f"Fitur_{i.replace(".py", "")}")})
                idx +=1
        if halaman == 1:
            buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command":"l", "function":lanjut})
        elif halaman < total_halaman:
            buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command":"p", "function":kembali})
            buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command":"l", "function":lanjut})
        else:
            buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command":"p", "function":kembali})
        print(result)
        loop = buttons(buttons_parameter)