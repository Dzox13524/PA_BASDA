from Fitur.Umum.controler import clear_terminal
import os 

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
            if i.endswith(".py"):
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
                clear_terminal()
            case '2':
                clear_terminal()
            case '3':
                clear_terminal()
                print('Log Out')
                break
            case '4':
                clear_terminal()
            case ValueError:
                clear_terminal()