# import pandas as pd
# from tabulate import tabulate
# from Fitur.Umum.controler import clear_terminal

# def shaker_sort(arr, key_list):
#     kiri = 0
#     kanan = len(arr) - 1
#     while kiri < kanan:
#         for i in range(kiri, kanan):
#             if key_list[arr[i]] > key_list[arr[i+1]]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#         kanan -= 1
#         for i in range(kanan, kiri, -1):
#             if key_list[arr[i]] < key_list[arr[i-1]]:
#                 arr[i], arr[i-1] = arr[i-1], arr[i]
#         kiri += 1

# data = pd.read_csv("database/Akun.csv")

# def sorted_data(urutan):
#     usernames = data[urutan].tolist()
#     indices = list(range(len(usernames)))
#     shaker_sort(indices, usernames)
#     sorted_data = data.iloc[indices].reset_index(drop=True)
#     sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
#     return sorted_data

# def Fitur_list_akun(urutan, awal, akhir):
#     halaman = 1
#     total_halaman = (len(data) + 50 - 1) // 50
#     usernames = data[urutan].tolist()
#     indices = list(range(len(usernames)))
#     shaker_sort(indices, usernames)
#     sorted_data = data.iloc[indices].reset_index(drop=True)[awal:akhir]
#     sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
#     clear_terminal()
#     result = tabulate(sorted_data[["No", "Name", "Email", "Nomor_Telepon", "Kecamatan", "Desa"]], headers=["No","Nama","Email","Nomor Hp","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
#     result += f"\nTotal User: {len(usernames)} | Halaman {halaman} dari {total_halaman}"
#     return result
# print(list_akun("Name", 0, 50))

# def tes (parameter):
#     print(parameter)

# def buttons(buttons_info =[]):
#     text = '--- PILIH OPSI ---\n\n'
#     for idx, data in enumerate(buttons_info):
#         text += f"[{idx+1}] {data["Nama"]}\n"
#     text += "[K] keluar\n\n"
#     text += "---"
#     while True:
#         print(text)
#         pilihan = input("Masukkan Pilihan Anda: ")
#         for idx, data in enumerate(buttons_info):
#             if pilihan ==str(idx + 1):
#                 data["function"]()
#                 break
#             if pilihan == "k":
#                 return

# buttons([{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes},{"Nama": "Tes", "function":tes}])

data = [1, 100]

for i in range(data[0], data[1]+1):
    print(i)