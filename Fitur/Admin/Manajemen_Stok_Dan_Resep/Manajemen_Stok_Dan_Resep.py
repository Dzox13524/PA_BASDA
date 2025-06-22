import os
import importlib
from controler import clear_terminal, waktu_sekarang, buttons


def menu_Manajemen_Stok_Dan_Resep():
    clear_terminal()
    waktu = waktu_sekarang()
    pembuka = f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Waktu Saat Ini    : {waktu + ' '*(51-len(waktu) - 23) + '║'}
║ ⊳ Stok Bahan Kritis : Stok Bahan Kritis           ║
║ ⊳ Total Penjualan   :                             ║
╠───────────────────────────────────────────────────╣
"""

    idx = 1
    buttons_parameter = []

    pembuka += """║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║
"""

    path_folder = "./Fitur/Admin/Manajemen_Stok_Dan_Resep"
    modul_prefix = "Fitur.Admin.Manajemen_Stok_Dan_Resep"

    for i in os.listdir(path_folder):
        if i.endswith(".py") and i not in [
            "__pycache__",
            "Manajemen_Stok_Dan_Resep.py",
        ]:
            nama = i.replace(".py", "").replace("_", " ")
            pembuka += f"║├▶ {idx}. {nama}{' '*(45 - len(str(idx) + nama))}│║\n"

            modul_path = f"{modul_prefix}.{i.replace('.py', '')}"
            modul = importlib.import_module(modul_path)

            cmd = nama[0].lower()
            if cmd in [btn["command"] for btn in buttons_parameter]:
                cmd = nama[:2].lower()

            buttons_parameter.append(
                {
                    "Nama": nama,
                    "command": cmd,
                    "function": getattr(modul, f"Fitur_{i.replace('.py', '')}"),
                }
            )

            idx += 1

    pembuka += f"║├▶ {idx}. Keluar{' '*(45 - len(str(idx) + 'Keluar'))}│║\n"
    pembuka += """║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    buttons(buttons_parameter)
