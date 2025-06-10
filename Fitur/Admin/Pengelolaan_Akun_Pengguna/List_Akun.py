import pandas as pd
from tabulate import tabulate
from controler import clear_terminal

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

def sorted_data(urutan):
    data = pd.read_csv("database/Akun.csv")
    usernames = data[urutan].tolist()
    indices = list(range(len(usernames)))
    shaker_sort(indices, usernames)
    sorted_data = data.iloc[indices].reset_index(drop=True)
    sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
    return sorted_data

def Fitur_list_akun(urutan, awal, akhir, halaman):
    data = pd.read_csv("database/Akun.csv")
    total_halaman = (len(data) + 50 - 1) // 50
    usernames = data[urutan].tolist()
    indices = list(range(len(usernames)))
    shaker_sort(indices, usernames)
    sorted_data = data.iloc[indices].reset_index(drop=True)[awal:akhir]
    sorted_data.insert(0, "No", range(awal + 1, awal + len(sorted_data) + 1))
    clear_terminal()
    total_user = len(usernames)
    result = tabulate(sorted_data[["No", "Name", "Email", "Nomor_Telepon", "Kecamatan", "Desa"]], headers=["No","Nama","Email","Nomor Hp","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
    result += f"\nTotal User: {len(usernames)} | Halaman {halaman} dari {total_halaman}"
    return result, total_user, total_halaman