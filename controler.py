import os
import subprocess

# === Searching (BOOYER MOORE) === 

def buat_tabel_bad_character(pola):
    tabel = {}
    panjang = len(pola)
    for i in range(panjang - 1):
        tabel[pola[i]] = panjang - 1 - i
    return tabel

def boyer_moore_cocok(teks, pola):
    panjang_teks = len(teks)
    panjang_pola = len(pola)

    if panjang_pola == 0:
        return True

    tabel = buat_tabel_bad_character(pola)
    posisi = 0

    while posisi <= panjang_teks - panjang_pola:
        indeks = panjang_pola - 1

        while indeks >= 0 and pola[indeks] == teks[posisi + indeks]:
            indeks -= 1

        if indeks < 0:
            return True
        else:
            karakter = teks[posisi + indeks]
            if karakter in tabel:
                lompat = tabel[karakter]
                if lompat <= 0:
                    lompat = 1
            else:
                lompat = panjang_pola
            posisi += lompat

    return False


# === Beberapa Metode Pencarian === 
def Pencarian_Dengan_Rekomendasi(data, berdasarkan, dicari):
    data_list = data[berdasarkan].tolist()
    hasil = {
        "rekomendasi": [],
        "cocok": []
    }
    sudah_cocok = []
    
    data_dicari = dicari.split(" ")
    for i in data_dicari:
        kata = i.lower()
        for idx, item in enumerate(data_list):
            item_lower = str(item).lower()
            if boyer_moore_cocok(item_lower, kata):
                if item_lower == dicari.lower():
                    if idx not in sudah_cocok:
                        hasil["cocok"].append({"ditemukan": item, "index": idx})
                        sudah_cocok.append(idx)
                else:
                    if idx not in sudah_cocok:
                        hasil["rekomendasi"].append({"ditemukan": item, "index": idx})
                        sudah_cocok.append(idx)
    return hasil

def Pencarian_String(data, berdasarkan, dicari):
    data_list = data[berdasarkan].tolist()
    hasil = ''
    for idx, item in enumerate(data_list):
           if boyer_moore_cocok(str(item).lower(), str(dicari).lower()):
               hasil = idx
    return hasil

def Pencarian_Hasil_List(data, berdasarkan, dicari):
    data_list = data[berdasarkan].tolist()
    hasil = []
    for idx, item in enumerate(data_list):
        if boyer_moore_cocok(str(item), str(dicari)):
            if str(item) == str(dicari):
                hasil.append(idx)
    return hasil

# === Seker sort ===
def shaker_sort(arr, key_list):
    kiri = 0
    kanan = len(arr) - 1
    while kiri < kanan:
        for i in range(kiri, kanan):
            if key_list[arr[i]] > key_list[arr[i+1]]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        kanan -= 1
        for i in range(kanan, kiri, -1):
            if key_list[arr[i]] < key_list[arr[i-1]]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        kiri += 1
        
def shaker_sort_terbesar(arr, key_list):
    kiri = 0
    kanan = len(arr) - 1
    while kiri < kanan:
        for i in range(kiri, kanan):
            if key_list[arr[i]] < key_list[arr[i+1]]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        kanan -= 1
        for i in range(kanan, kiri, -1):
            if key_list[arr[i]] > key_list[arr[i-1]]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        kiri += 1
# === clear terminal ===
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

# === Buttons ===
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
