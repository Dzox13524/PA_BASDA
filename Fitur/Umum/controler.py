import os
import subprocess

# === clear terminal ===
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

def buttons(paramaeter =[]):
    text = '--- PILIH OPSI ---\n\n'
    for data in paramaeter:
        if type(data["command"]) == list:
            text += f"[INFO] {data["Nama"]}\n"
        else:
            text += f"[{data["command"]}] {data["Nama"]}\n"
    text += "[K] keluar\n\n"
    text += "---"
    while True:
        print(text)
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "k":
            return False
        ditemukan = False
        for data in paramaeter:
            if type(data["command"]) == list:
                for i in range(data["command"][0], data["command"][1]+ 1):
                    if pilihan == str(i):
                        data["function"](i-1)
                        ditemukan = True
                        return True
            else:
                if pilihan == data["command"]:
                    data["function"]()
                    ditemukan = True
                    return True
                
        if not ditemukan:
            input(f"'{pilihan}' tidak ada dalam pilihan. Tekan Enter untuk lanjut...")
        else:
            return True
