from tabulate import tabulate
from controler import clear_terminal
from database.connection import get_laporan_penjualan_per_menu


def Fitur_Laporan_Penjualan():
    while True:
        clear_terminal()
        print("=== LAPORAN PENJUALAN PER MENU ===")
        print("Pilih periode laporan:")
        print("1. Minggu ini")
        print("2. Bulan ini")
        print("3. Tahun ini")
        print("4. Semua")
        print("5. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan (1-5): ").strip()

        if pilihan == "1":
            periode_filter, judul = "minggu", "Minggu Ini"
        elif pilihan == "2":
            periode_filter, judul = "bulan", "Bulan Ini"
        elif pilihan == "3":
            periode_filter, judul = "tahun", "Tahun Ini"
        elif pilihan == "4":
            periode_filter, judul = None, "Semua Periode"
        elif pilihan == "5":
            break
        else:
            print("[ERROR] Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk lanjut...")
            continue

        clear_terminal()
        print(f"\nMemuat laporan penjualan untuk {judul}...\n")
        data = get_laporan_penjualan_per_menu(periode_filter)

        if not data:
            print(f"[INFO] Tidak ada data penjualan untuk {judul}.")
            input("\nTekan Enter untuk kembali...\n")
            continue

        tabel = []
        for nama_menu, total_terjual, total_pendapatan in data:
            tabel.append([nama_menu, total_terjual, f"Rp{total_pendapatan:,.2f}"])

        print(f"LAPORAN PENJUALAN PER MENU ({judul})\n")
        print(
            tabulate(
                tabel,
                headers=["Nama Menu", "Jumlah Terjual", "Total Pendapatan"],
                tablefmt="fancy_grid",
            )
        )
        input("\nTekan Enter untuk kembali ke pilihan periode...\n")
