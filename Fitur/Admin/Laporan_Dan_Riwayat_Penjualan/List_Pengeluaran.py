from tabulate import tabulate
from database.connection import get_pengeluaran
from controler import format_tanggal_waktu_wib

def Fitur_List_Pengeluaran():
    while True:
        print("Pilih periode pengeluaran yang ingin ditampilkan:")
        print("1. Minggu ini")
        print("2. Bulan ini")
        print("3. Tahun ini")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ").strip()
        if pilihan == "1":
            periode = "minggu"
        elif pilihan == "2":
            periode = "bulan"
        elif pilihan == "3":
            periode = "tahun"
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("[ERROR] Pilihan tidak valid. Silakan coba lagi.")
            continue

        data = get_pengeluaran(periode)
        data_formatted = []
        for row in data:
            tanggal, deskripsi, jumlah = row
            tanggal_str = format_tanggal_waktu_wib(tanggal)
            data_formatted.append((tanggal_str, deskripsi, jumlah))

        if not data:
            print(f"[INFO] Tidak ada data pengeluaran untuk periode {periode}.")
        else:
            print(f"\nData pengeluaran untuk periode {periode}:\n")
            print(tabulate(data_formatted, headers=["Tanggal", "Deskripsi", "Jumlah"], tablefmt="grid"))
        input("\nTekan Enter untuk kembali ke menu...\n")