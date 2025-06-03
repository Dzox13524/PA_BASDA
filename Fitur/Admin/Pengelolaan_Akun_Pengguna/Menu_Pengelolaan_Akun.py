from Fitur.Umum.controler import clear_terminal
import os 

from Fitur.Admin.Pengelolaan_Akun_Pengguna.Cari_Akun import Pencarian
from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import Fitur_ListAkun

def menu_pengelolaan_akun(username, kabupaten, role):
    while True:
        clear_terminal()
        pembuka = f"""╔───────────────────────────────────────────────────╗
║             PENGELOLAAN AKUN PENGGUNA             ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {username.upper() + ' '*(51-len(username) - 12) + '║'}
║ ⊳ Role   : {role + ' '*(51-len(role) - 12) + '║'}
║ ⊳ Lokasi : {kabupaten + ' '*(51-len(kabupaten) - 12) + '║'}
╠───────────────────────────────────────────────────╣\n"""
        idx = 1
        pembuka += """║┌─────────────────────────────────────────────────┐║
║│              OPSI PENGELOLAAN AKUN              │║
║├─────────────────────────────────────────────────┤║\n"""
        for i in os.listdir("./fitur/Admin/Pengelolaan_Akun_Pengguna"):
            if i.endswith(".py") and i != "Menu_Pengelolaan_Akun.py":
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                pembuka += f"""║├▶ {idx}. {nama}{" "*(45-len(str(idx) + nama))}│║\n"""
                idx +=1
        pembuka += f"""║├▶ {idx}. Keluar                                      │║\n"""
        pembuka += """║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
    """
        print(pembuka)
        pilihan = input('Pilih menu: ')
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
                Fitur_ListAkun()
                clear_terminal()
            case '5':
                clear_terminal()
            case '6':
                clear_terminal()
            case '7':
                clear_terminal()
                break
            case ValueError:
                clear_terminal()