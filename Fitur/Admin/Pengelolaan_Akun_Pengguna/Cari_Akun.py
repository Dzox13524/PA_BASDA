import pandas as pd
from tabulate import tabulate
from Fitur.Umum.controler import clear_terminal
from Fitur.Admin.Pengelolaan_Akun_Pengguna.List_Akun import sorted_data

def Pencarian_fibonacci(data, target):
    n = len(data)
    fib0 = 0
    fib1 = 1
    fibH = fib0 + fib1

    while fibH < n:

        fib0 = fib1
        fib1 = fibH
        fibH = fib0 + fib1
    batas = -1
    while fibH > 1:
        i = batas + fib0

        if i >= n:
            fibH = fib0
            fib1 = fib1 - fib0
            fib0 = fibH - fib1
            continue 

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
    
def Pencarian(berdasarkan, key):
    data = sorted_data(berdasarkan)
    list_data = data[berdasarkan].to_list()
    datas = Pencarian_fibonacci(list_data, key)
    result = data.iloc[datas]
    if datas == -1:
        input(""">> Data tidak ditemukan. <<
              
Tekan [Enter] untuk kembali...""")
    else:
        input(f"""=====================================
            Data Ditemukan           
=====================================
ID Akun    : {result["ID"]}
Nama       : {result["Name"]}
Email      : {result["Email"]}
Password   : {result["Password"]}
Peran      : {result["Role"]}
Kecamatan  : {result["Kecamatan"]}
Desa       : {result["Desa"]}
-------------------------------------
Tekan [Enter] untuk kembali...
-------------------------------------
""")