import os 
import config
import importlib
from Fitur.Umum.controler import buttons

from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import Fitur_list_akun
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Detail_Akun import Fitur_Detail_Akun

def menu_pengelolaan_akun(urutan = config.urutanUser):
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
        result, total_user, total_halaman = Fitur_list_akun(config.urutanUser, awal, akhir, halaman)
        result += f"\nUrutan Berdasarkan [{config.urutanUser}]\n"
        idx = 1
        buttons_parameter = []
        buttons_parameter.append({"Nama": f"Pilih [1 - {total_user}] untuk melihat detail Akun", "command":[1, total_user], "function":Fitur_Detail_Akun})
        for i in os.listdir("./fitur/Admin/Pengelolaan_Akun_Pengguna"):
            if i.endswith(".py") and i not in ["Menu_Pengelolaan_Akun.py","List_Akun.py", "Detail_Akun.py", "Hapus_Akun.py"]:
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                modul_path = f"Fitur.Admin.Pengelolaan_Akun_Pengguna.{i.replace(".py", "")}"
                modul = importlib.import_module(modul_path)
                buttons_parameter.append({"Nama": nama, "command":nama[0].lower(), "function":getattr(modul, f"Fitur_{i.replace(".py", "")}")
})
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