import pandas as pd
import os
from tabulate import tabulate
from Fitur.Umum.controler import clear_terminal

filePeminjaman = "database/Peminjaman.csv"
        
def lihatRiwayatPeminjaman():
    clear_terminal()

    print(f"""╔───────────────────────────────────────────────────╗
║               APLIKASI PERPUSTAKAAN               ║
║            === RIWAYAT PEMINJAMAN ===             ║
╚───────────────────────────────────────────────────╝
""".strip())

    try:
        df = pd.read_csv(filePeminjaman)

        if df.empty:
            print("Tidak ada data!\n")
            input("Tekan Enter untuk kembali...")
            clear_terminal()
            return

        total_data = len(df)
        if total_data > 100:
            page_size = 20
            current_page = 0
            while True:
                clear_terminal()
                print(f"""╔───────────────────────────────────────────────────╗
║               APLIKASI PERPUSTAKAAN               ║
║            === RIWAYAT PEMINJAMAN ===             ║
╚───────────────────────────────────────────────────╝
""".strip())

                start_idx = current_page * page_size
                end_idx = start_idx + page_size
                page_data = df.iloc[start_idx:end_idx]

                table_data = []
                for i, row in page_data.iterrows():
                    table_data.append([
                        i + 1, row["ID_User"], row["ID_Buku"], row["Tanggal_Memintam"], row["Status_Pengembalian"], row["Tanggal_Kembali"]
                    ])

                headers = ["No.", "ID User", "ID Buku", "Tanggal Meminjam", "Status", "Tanggal Pengembalian"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
                print("="*115)

                # Jika sudah di halaman terakhir, tidak perlu opsi next
                if end_idx >= total_data:
                    print("Anda telah berada di halaman terakhir.")
                    input("Tekan Enter untuk kembali...")
                    clear_terminal()
                    break

                user_input = input("Tekan [Enter] untuk kembali ke menu utama, ketik [N] untuk halaman selanjutnya: ").strip().lower()
                if user_input == 'n':
                    current_page += 1
                else:
                    clear_terminal()
                    break

        else:
            # Jika data 100 atau kurang, tampilkan semua tanpa page
            table_data = []
            for i, row in df.iterrows():
                table_data.append([
                    i + 1, row["ID_User"], row["ID_Buku"], row["Tanggal_Memintam"], row["Status_Pengembalian"], row["Tanggal_Kembali"]
                ])

            headers = ["No.", "ID User", "ID Buku", "Tanggal Meminjam", "Status", "Tanggal Pengembalian"]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            print("="*115)
            print("\n")
            input("Tekan Enter untuk lanjut...")
            clear_terminal()

    except IOError:
        print("Anda belum pernah melakukan pemesanan!")
        print("\n")
        input("Tekan Enter untuk kembali...")
        clear_terminal()
