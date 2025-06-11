import pandas as pd
from datetime import datetime, timedelta
from controler import clear_terminal, buttons, Pencarian_String
from Fitur.Admin.Pengelolaan_Data_Buku.Detail_Buku import Fitur_Detail_Buku_berdasarkan

def shaker_sort(arr, key_dict):
    kiri = 0
    kanan = len(arr) - 1
    while kiri < kanan:
        for i in range(kiri, kanan):
            if key_dict[arr[i]] < key_dict[arr[i+1]]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        kanan -= 1
        for i in range(kanan, kiri, -1):
            if key_dict[arr[i]] > key_dict[arr[i-1]]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        kiri += 1

def Fitur_Top_Peminjaman_Buku():
    clear_terminal()
    print("Pilih periode top peminjaman buku:")
    print("1. Mingguan")
    print("2. Bulanan")
    print("3. Sepanjang Waktu")

    while True:
        inputan = input("Masukkan pilihan (1/2/3): ").strip()
        if inputan in ['1', '2', '3']:
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

    
    peminjaman = pd.read_csv("database/Peminjaman.csv")
    buku = pd.read_csv("database/Buku.csv")

    gabung = pd.merge(peminjaman, buku[['ISBN', 'JudulBuku']], on='ISBN', how='left')
    gabung = gabung[gabung['Status_Pengembalian'] != "Permintaan_Peminjaman"]

    gabung['Tanggal_Meminjam'] = pd.to_datetime(gabung['Tanggal_Meminjam'], errors='coerce')

    sekarang = datetime.now()
    if inputan == '1':
        batas = sekarang - timedelta(days=7)
        gabung = gabung[gabung['Tanggal_Meminjam'] >= batas]
        judul_output = "Top Peminjaman Buku Mingguan"
    elif inputan == '2':
        batas = sekarang - timedelta(days=30)
        gabung = gabung[gabung['Tanggal_Meminjam'] >= batas]
        judul_output = "Top Peminjaman Buku Bulanan"
    elif inputan == '3':
        judul_output = "Top Peminjaman Buku Sepanjang Waktu"
    else:
        input("Pilihan Tidak Ada!")
        return
    jumlah_peminjaman = {}
    for i in gabung.to_dict(orient='records'):
        judul = i["JudulBuku"]
        jumlah_peminjaman[judul] = jumlah_peminjaman.get(judul, 0) + 1

    judul_list = list(jumlah_peminjaman.keys())
    shaker_sort(judul_list, jumlah_peminjaman)
    buttons_parameter = []
    clear_terminal()
    print(f"\n--- {judul_output} (5 Teratas) ---")
    print("--------------------------------------------------\n")
    if len(judul_list) > 0:
        for idx, judul in enumerate(judul_list[:5], start=1):
            indeks_buku = Pencarian_String(buku, 'JudulBuku', judul)
            print(f"{idx}. Judul Buku  : {buku["JudulBuku"][indeks_buku]}")
            print(f"   Penulis     : {buku["Penulis"][indeks_buku]}")
            print(f"   Genre       : {buku["Genre"][indeks_buku]}")
            print(f"   Dipinjam    : {jumlah_peminjaman[judul]} kali")
            print(f"   ISBN        : {buku["ISBN"][indeks_buku]}\n")
            buttons_parameter.append({"Nama": buku["JudulBuku"][indeks_buku], "command":f"{idx}", "function":lambda id=buku["ISBN"][indeks_buku]: Fitur_Detail_Buku_berdasarkan(id, "ISBN")})
    else: 
        print("Tidak Ada Peminjaman")
    buttons(buttons_parameter)