def Fitur_Mengembalikan_Buku():
    pass

# import pandas as pd
# import os
# from datetime import datetime
# from tabulate import tabulate
# from Fitur.Umum.controler import clear_terminal

# filePeminjaman = "database/Peminjaman.csv"

# def kembalikanBuku():
#     clear_terminal()
#     print(f"""╔───────────────────────────────────────────────────╗
# ║               APLIKASI PERPUSTAKAAN               ║
# ║              === PENGEMBALIAN BUKU ===            ║
# ╚───────────────────────────────────────────────────╝
# """.strip())

#     try:
#         df = pd.read_csv(filePeminjaman)

#         # Filter hanya yang belum dikembalikan
#         df_pending = df[df["Status_Pengembalian"] == "Belum Dikembalikan"]

#         if df_pending.empty:
#             print("Tidak ada buku yang perlu dikembalikan!\n")
#             input("Tekan Enter untuk kembali...")
#             clear_terminal()
#             return

#         table_data = []
#         for i, row in df_pending.iterrows():
#             table_data.append([
#                 i + 1, row["ID_User"], row["ID_Buku"], row["Tanggal_Memintam"], row["Status_Pengembalian"]
#             ])

#         headers = ["No.", "ID User", "ID Buku", "Tanggal Meminjam", "Status"]
#         print(tabulate(table_data, headers=headers, tablefmt="grid"))
#         print("="*80)

#         try:
#             pilihan = int(input("Masukkan nomor peminjaman yang ingin dikembalikan: "))
#             if pilihan < 1 or pilihan > len(df_pending):
#                 raise ValueError("Nomor tidak valid.")

#             index_terpilih = df_pending.index[pilihan - 1]

#             df.at[index_terpilih, "Status_Pengembalian"] = "Sudah Dikembalikan"
#             df.at[index_terpilih, "Tanggal_Kembali"] = datetime.now().strftime("%Y-%m-%d")

#             df.to_csv(filePeminjaman, index=False)

#             print("\nBuku berhasil dikembalikan!")
#             input("Tekan Enter untuk kembali...")
#             clear_terminal()

#         except ValueError as ve:
#             print(f"Input salah: {ve}")
#             input("Tekan Enter untuk kembali...")
#             clear_terminal()

#     except FileNotFoundError:
#         print("Data peminjaman belum tersedia.")
#         input("Tekan Enter untuk kembali...")
#         clear_terminal()
