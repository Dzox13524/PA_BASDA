import pandas as pd
from tabulate import tabulate

def Pencarian_fibonacci(data, target):
    n = len(data)
    fib0 = 0
    fib1 = 1
    fibH = fib0 + fib1

    while fibH <= n:
        fib0 = fib1
        fib1 = fibH
        fibH = fib0 + fib1
    batas = -1
    while fibH > 1:
        i = batas + fib0

        if data[i] < target:
            fibH = fib1
            fib1 = fib0
            fib0 = fibH - fib1
            batas = i
        elif data[i] > target:
            fibH = fib0
            fib1 = fib1 - fib0
            fib0 = fibH - fib1
        else:
            return i
        
    if fib1 and batas + 1 < n and data[batas + 1] == target:
        return batas + 1

    return -1
    
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

def list_akun():
    input("Pilih [1-5]")
    usernames = data["Name"].tolist()
    indices = list(range(len(usernames)))
    shaker_sort_indexed(indices, usernames)
    sorted_data = data.iloc[indices].reset_index(drop=True)[0:50]
    sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
    return tabulate(sorted_data, headers=["No","ID","Name","Email","Password","Role","Kecamatan","Desa"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
