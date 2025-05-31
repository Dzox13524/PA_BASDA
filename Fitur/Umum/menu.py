from Fitur.Umum.controler import clear_terminal
import pandas as pd
import os 

def menu(email, username, kabupaten, desa, role):
    clear_terminal()
    pembuka = ''
    data = pd.read_csv('database/Akun.csv')
    data2 = data[data['Email'] == email].iloc[0].to_dict()
    if data2['Role'] == 'kepda':
        data2['Role'] = 'Kepala Daerah'
        teks = f"Selamat datang, Kepala Daerah {data2['Daerah']}!"
        if len(teks) > 49:
            teks = f'''Selamat datang, Kepala Daerah\n{kabupaten}!'''
        pembuka = f"""\n╔═══════════════════════════════════════════════════╗\n║{teks:^51}║\n╚═══════════════════════════════════════════════════╝\n"""
    elif data2['Role'] == 'user':
        pembuka = f'Selamat datang {data2['Name'].upper()} selamat berbelanja :>\n\n'

    pembuka += f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {data2['Name'].upper() + ' '*(51-len(data2['Name']) - 12) + '║'}
║ ⊳ Role   : {data2['Role'] + ' '*(51-len(data2['Role']) - 12) + '║'}
║ ⊳ Lokasi : {kabupaten + ' '*(51-len(kabupaten) - 12) + '║'}
╠───────────────────────────────────────────────────╣\n"""
    if role == 'admin':
        idx = 1
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║\n"""
        for i in os.listdir("./fitur/Admin"):
            if i.endswith(".py"):
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                pembuka += f"""║├▶ {idx}. {nama}{" "*(45-len(str(idx) + nama))}│║\n"""
                idx +=1
        pembuka += f"""║├▶ {idx}. Keluar                                      │║\n"""
        pembuka += f"""║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""

    elif role == "user":
        idx = 1
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║\n"""
        for i in os.listdir("./fitur/User"):
            if i.endswith(".py"):
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                pembuka += f"""║├▶ {idx}. {nama}{" "*(45-len(str(idx) + nama))}│║\n"""
            idx +=1
        pembuka += f"""║├▶ {idx}. Keluar                                      │║\n"""
        pembuka += f"""║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    else :
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║
║├▶ 1. Laporan Pengajuan Subsidi                   │║
║├▶ 2. Inventaris Daerah                           │║
║├▶ 3. Log Out                                     │║
║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    print(pembuka)