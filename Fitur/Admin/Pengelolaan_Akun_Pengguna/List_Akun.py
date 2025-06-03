import pandas as pd
from tabulate import tabulate
from Fitur.Umum.controler import clear_terminal

def shaker_sort_indexed(arr, key_list):
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

data = pd.read_csv("database/Akun.csv")

def sorted_data(urutan):
    usernames = data[urutan].tolist()
    indices = list(range(len(usernames)))
    shaker_sort_indexed(indices, usernames)
    sorted_data = data.iloc[indices].reset_index(drop=True)
    sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
    return sorted_data

def list_akun(urutan):
    awal = 0
    akhir= 50
    usernames = data[urutan].tolist()
    indices = list(range(len(usernames)))
    shaker_sort_indexed(indices, usernames)
    sorted_data = data.iloc[indices].reset_index(drop=True)
    sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))[awal:akhir]
    result = tabulate(sorted_data, headers=["No","ID","Name","Email","Password","Role","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
    result += f"\nTotal User: {len(data)}"
    return print(result)

def Fitur_ListAkun():
    while True:
        clear_terminal()
        print("""1. Urutkan berdasarkan Id
2. Urutkan Berdasar Nama
3. Urutkan Berdasarkan Kecamatan
4. Urutkan Berdasarkan Desa
5. Keluar""")
        pilihan = input("\nPilih [1-5]: ")
        match pilihan:
            case '1':
                clear_terminal()
                list_akun("ID")
                return input("Tekan [Enter] untuk kembali ke menu...")
            case '2':
                clear_terminal()
                list_akun("Name")
                return input("Tekan [Enter] untuk kembali ke menu...")
            case '3':
                clear_terminal()
                list_akun("Kecamatan")
                return input("Tekan [Enter] untuk kembali ke menu...")
            case '4':
                clear_terminal()
                list_akun("Desa")
                return input("Tekan [Enter] untuk kembali ke menu...")
            case '5':
                clear_terminal()
                input("Tekan [Enter] untuk kembali ke menu...")
                break
            case _:
                clear_terminal()
                print("Pilihan tidak falid! pilih angka [1-5]")
                input("Tekan [Enter] untuk melanjutkan...")
                continue
