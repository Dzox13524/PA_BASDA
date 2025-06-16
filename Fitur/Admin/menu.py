from controler import clear_terminal, waktu_sekarang
import os


def menu():
    clear_terminal()
    pembuka = f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Waktu Saat Ini    : {waktu_sekarang() + ' '*(51-len(waktu_sekarang()) - 23) + '║'}
║ ⊳ Stok Bahan Kritis : Stok Bahan Kritis           ║
║ ⊳ Total Penjualan   :                             ║
╠───────────────────────────────────────────────────╣\n"""
    idx = 1
    pembuka += """║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║\n"""
    for i in os.listdir("./fitur/Admin"):
        if i not in ["__pycache__", "menu.py"]:
            nama = i.replace(".py", "")
            nama = nama.replace("_", " ")
            pembuka += f"""║├▶ {idx}. {nama}{" "*(45-len(str(idx) + nama))}│║\n"""
            idx += 1
    pembuka += f"""║├▶ {idx}. Keluar                                      │║\n"""
    pembuka += """║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    print(pembuka)
