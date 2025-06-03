import pandas as pd
from tabulate import tabulate
from Fitur.Umum.controler import clear_terminal

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

data = pd.read_csv("database/Akun.csv")

def sorted_data(urutan):
    usernames = data[urutan].tolist()
    indices = list(range(len(usernames)))
    shaker_sort(indices, usernames)
    sorted_data = data.iloc[indices].reset_index(drop=True)
    sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
    return sorted_data

def list_akun(urutan):
    awal = 0
    akhir= 50
    halaman = 1
    total_halaman = (len(data) + 50 - 1) // 50
    usernames = data[urutan].tolist()
    indices = list(range(len(usernames)))
    shaker_sort(indices, usernames)
    while True:
        clear_terminal()
        sorted_data = data.iloc[indices].reset_index(drop=True)[awal:akhir]
        sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
        result = tabulate(sorted_data, headers=["No","ID","Name","Email","Password","Role","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
        result += f"\n\nTotal User: {len(data)}\n"
        result += f"Halaman {halaman} dari {total_halaman}\n"
        result += "----------------------------------------\n"
        if halaman == 1:
            result += "Tekan [Enter] untuk kembali ke menu utama, ketik [N] untuk halaman selanjutnya\n"
        elif halaman < total_halaman:
            result += "Tekan [Enter] untuk kembali ke menu utama, ketik [N] untuk halaman selanjutnya, atau ketik [P] untuk halaman sebelumnya.\n"
        else:
            result += "Tekan [Enter] untuk kembali ke menu utama, atau ketik [P] untuk halaman sebelumnya.\n"
        result += "----------------------------------------\n"
        print(result)
        inputan = input("Pilihan Anda: ").strip().lower()
        if inputan == 'n' and halaman <= total_halaman:
            awal = akhir
            akhir += 50
            halaman += 1
            continue
        elif inputan == 'p' and halaman > 1:
            akhir = awal
            awal = akhir - 50
            halaman -= 1
            continue
        elif inputan == '':
            break

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
                break
            case '2':
                clear_terminal()
                list_akun("Name")
                break
            case '3':
                clear_terminal()
                list_akun("Kecamatan")
                break
            case '4':
                clear_terminal()
                list_akun("Desa")
                break
            case '5':
                clear_terminal()
                input("Tekan [Enter] untuk kembali ke menu...")
                break
            case _:
                clear_terminal()
                print("Pilihan tidak falid! pilih angka [1-5]")
                input("Tekan [Enter] untuk melanjutkan...")
                continue
