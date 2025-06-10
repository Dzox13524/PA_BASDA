from Fitur.Umum.controler import clear_terminal
import os 

def menu(email, username, kabupaten, desa, role):
    clear_terminal()
    pembuka = ''
    if role == 'user':
        pembuka += f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {username.upper() + ' '*(51-len(username) - 12) + '║'}
║ ⊳ Role   : {role + ' '*(51-len(role) - 12) + '║'}
║ ⊳ Lokasi : {kabupaten + ' '*(51-len(kabupaten) - 12) + '║'}
╠───────────────────────────────────────────────────╣\n"""
        idx = 1
        pembuka += """║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║\n"""
        for i in os.listdir("./fitur/User"):
            if i != "__pycache__":
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                pembuka += f"""║├▶ {idx}. {nama}{" "*(45-len(str(idx) + nama))}│║\n"""
                idx +=1
        pembuka += f"""║├▶ {idx}. Keluar                                      │║\n"""
        pembuka += """║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    if role == 'admin':
        pembuka += f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {username.upper() + ' '*(51-len(username) - 12) + '║'}
║ ⊳ Role   : {role + ' '*(51-len(role) - 12) + '║'}
║ ⊳ Lokasi : {kabupaten + ' '*(51-len(kabupaten) - 12) + '║'}
╠───────────────────────────────────────────────────╣\n"""
        idx = 1
        pembuka += """║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║\n"""
        for i in os.listdir("./fitur/Admin"):
            if i != "__pycache__":
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                pembuka += f"""║├▶ {idx}. {nama}{" "*(45-len(str(idx) + nama))}│║\n"""
                idx +=1
        pembuka += f"""║├▶ {idx}. Keluar                                      │║\n"""
        pembuka += """║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    print(pembuka)