import os
import pytz
import subprocess
from datetime import datetime


# === Jam Terbaru ===
def waktu_sekarang():
    bulan = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember",
    }

    zona_wib = pytz.timezone("Asia/Jakarta")
    sekarang = datetime.now(zona_wib)

    tanggal = sekarang.day
    bulan = bulan[sekarang.month]
    tahun = sekarang.year
    jam = sekarang.strftime("%H:%M")

    hasil = f"{tanggal} {bulan} {tahun}, {jam} WIB"
    return hasil


# === clear terminal ===
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        subprocess.call("clear")


# === Buttons ===
def buttons(paramaeter=[]):
    text = "--- PILIH OPSI ---\n\n"
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
                for i in range(data["command"][0], data["command"][1] + 1):
                    if pilihan == str(i):
                        data["function"](i - 1)
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
