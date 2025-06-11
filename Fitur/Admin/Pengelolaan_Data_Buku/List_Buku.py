import pandas as pd
from tabulate import tabulate
from controler import clear_terminal, shaker_sort

def sorted_data(urutan):
    data = pd.read_csv("database/Buku.csv")
    Judul = data[urutan].tolist()
    indices = list(range(len(Judul)))
    shaker_sort(indices, Judul)
    sorted_data = data.iloc[indices].reset_index(drop=True)
    sorted_data.insert(0, "No", range(1, len(sorted_data) + 1))
    return sorted_data

def Fitur_list_buku(urutan, awal, akhir, halaman):
    data = pd.read_csv("database/Buku.csv")
    total_halaman = (len(data) + 50 - 1) // 50
    Judul = data[urutan].tolist()
    indices = list(range(len(Judul)))
    shaker_sort(indices, Judul)
    sorted_data = data.iloc[indices].reset_index(drop=True)[awal:akhir]
    sorted_data.insert(0, "No", range(awal + 1, awal + len(sorted_data) + 1))
    clear_terminal()
    total_buku = len(Judul)
    result = tabulate(sorted_data[["No","ISBN", "JudulBuku", "Penulis", "Penerbit", "Genre", "TahunTerbit", "Stok"]], headers=["No","ISBN", "JudulBuku", "Penulis", "Penerbit", "Genre", "TahunTerbit", "Stok"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
    result += f"\nTotal Buku: {len(Judul)} | Halaman {halaman} dari {total_halaman}"
    return result, total_buku, total_halaman