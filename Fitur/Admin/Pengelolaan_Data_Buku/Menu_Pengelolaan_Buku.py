from Fitur.Umum.controler import clear_terminal
import os 

def menu_pengelolaan_buku(username, kabupaten, role):
    while True:
        clear_terminal()
        pembuka = f"""╔───────────────────────────────────────────────────╗
║                 PENGELOLAAN BUKU                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {username.upper() + ' '*(51-len(username) - 12) + '║'}
║ ⊳ Role   : {role + ' '*(51-len(role) - 12) + '║'}
║ ⊳ Lokasi : {kabupaten + ' '*(51-len(kabupaten) - 12) + '║'}
╠───────────────────────────────────────────────────╣\n"""
        idx = 1
        pembuka += """║┌─────────────────────────────────────────────────┐║
║│              OPSI PENGELOLAAN BUku              │║
║├─────────────────────────────────────────────────┤║\n"""
        for i in os.listdir("./fitur/Admin/Pengelolaan_Data_Buku"):
            if i.endswith(".py") and i != "Menu_Pengelolaan_Buku.py":
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
            case '4':
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