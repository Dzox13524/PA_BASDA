from Fitur.Umum.controler import clear_terminal
from tabulate import tabulate
import os 

from Fitur.Admin.Pengelolaan_Akun_Pengguna.Cari_Akun import Pencarian
from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import sorted_data



def menu_pengelolaan_akun(username, kabupaten, role, urutan = "Name"):
    awal = 0
    akhir = 50
    halaman = 1
    data = sorted_data(urutan)[awal:akhir]
    total_halaman = (len(sorted_data(urutan)) + 50 - 1) // 50
    while True:
        idx = 1
        clear_terminal()
        result = tabulate(data[["No", "Name", "Email", "Nomor_Telepon", "Kecamatan", "Desa"]], headers=["No","Nama","Email","Nomor Hp","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
        result += f"\nTotal User: {len(sorted_data(urutan))} | Halaman {halaman} dari {total_halaman}\n\n"
        result += "---\n"
        for i in os.listdir("./fitur/Admin/Pengelolaan_Akun_Pengguna"):
            if i.endswith(".py") and i != "Menu_Pengelolaan_Akun.py" and i != "List_Akun.py":
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                result += f"""[{idx}] {nama}\n"""
                idx +=1
        if halaman == 1:
            result += "[L] Halaman Selanjutnya\n"
        elif halaman < total_halaman:
            result += "[P] Halaman Sebelumnya | [L] Halaman Selanjutnya\n"
        else:
            result += "[P] Halaman Sebelumnya\n"
        result += f"""[{idx}] Keluar\n"""
        result += "---\n"
        print(result)
        pilihan = input('Pilih menu: ').strip().lower()
        match pilihan:
            case '1':
                Pencarian("Name", "Ahmat")
                clear_terminal()
            case '2':
                clear_terminal()
            case '3':
                clear_terminal()
                print('Log Out')
                break
            case '4':
                clear_terminal()
            case '5':
                clear_terminal()
                break
            case "p":
                if halaman > 1:
                    akhir = awal
                    awal = akhir - 50
                    halaman -= 1
                continue
            case "l":
                if halaman < total_halaman:
                    awal = akhir
                    akhir += 50
                    halaman += 1
                continue
            case ValueError:
                clear_terminal()