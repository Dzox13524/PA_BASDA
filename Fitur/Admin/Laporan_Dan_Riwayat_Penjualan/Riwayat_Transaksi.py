from tabulate import tabulate
from controler import format_tanggal_waktu_wib, clear_terminal

from database.connection import get_detail_riwayat_transaksi

def Fitur_Riwayat_Transaksi():
    while True:
        clear_terminal()
        print("\nPilih periode detail riwayat transaksi yang ingin ditampilkan:")
        print("1. Minggu ini")
        print("2. Bulan ini")
        print("3. Tahun ini")
        print("4. Lihat Semua Transaksi (Tanpa Filter Periode)")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan (1-5): ").strip()
        periode_filter = None

        if pilihan == "1":
            periode_filter = "minggu"
            judul = "Minggu Ini"
        elif pilihan == "2":
            periode_filter = "bulan"
            judul = "Bulan Ini"
        elif pilihan == "3":
            periode_filter = "tahun"
            judul = "Tahun Ini"
        elif pilihan == "4":
            periode_filter = None
            judul = "Semua Transaksi"
        elif pilihan == "5":
            print("Kembali ke menu utama.")
            break
        else:
            print("[ERROR] Pilihan tidak valid. Silakan coba lagi.")
            continue

        clear_terminal()
        print(f"\nMemuat detail riwayat transaksi untuk periode {judul}...")
        data_transaksi_mentah = get_detail_riwayat_transaksi(periode_filter)

        if not data_transaksi_mentah:
            print(f"[INFO] Tidak ada detail riwayat transaksi untuk periode {judul}.")
            input("\nTekan Enter untuk kembali ke menu...\n")
            continue

        tabel_data = []
        transaksi_terakhir = None

        for row in data_transaksi_mentah:
            tanggal, id_transaksi, nama_menu, kuantitas, harga_satuan, subtotal_item, total_bayar_transaksi = row
            tanggal_formatted = format_tanggal_waktu_wib(tanggal)
            if id_transaksi != transaksi_terakhir:
                tampilkan_tanggal = tanggal_formatted
                tampilkan_total = f"Rp{float(total_bayar_transaksi):,.2f}"
                transaksi_terakhir = id_transaksi
            else:
                tampilkan_tanggal = ""
                tampilkan_total = ""

            tabel_data.append([
                id_transaksi,
                tampilkan_tanggal,
                nama_menu,
                kuantitas,
                f"Rp{harga_satuan:,.2f}",
                f"Rp{subtotal_item:,.2f}",
                tampilkan_total
            ])

        headers = ["ID Transaksi", "Tanggal", "Nama Menu", "Qty", "Harga Satuan", "Subtotal", "Total Transaksi"]

        print(f"\nData Detail Riwayat Transaksi untuk periode {judul}:\n")
        print(tabulate(tabel_data, headers=headers, tablefmt="grid", stralign="center", numalign="right"))

        input("\nTekan Enter untuk kembali ke menu...\n")