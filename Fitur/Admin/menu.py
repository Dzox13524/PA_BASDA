from controler import clear_terminal, waktu_sekarang
from database.connection import get_total_penjualan_hari_ini, get_bahan_baku_kritis, periksa_dan_update_status_menu
import os


def menu():
    clear_terminal()
    periksa_dan_update_status_menu()
    bahan_menipis, list_bahan_menipis = get_bahan_baku_kritis()
    total, item = get_total_penjualan_hari_ini()
    pembuka = f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Waktu Saat Ini    : {waktu_sekarang() + ' '*(51-len(waktu_sekarang()) - 23) + '║'}
║ ⊳ Stok Bahan Kritis : {(str(bahan_menipis) + ' Bahan'+ ' '*(51-len(str(bahan_menipis)+ ' Bahan') - 23))}║
║ ⊳ Total Penjualan   : {(str(total) + ' Terjual'+ ' '*(51-len(str(total)+ ' Terjual') - 23))}║
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
