from controler  import clear_terminal
from database.connection import tambah_bahan_baku 


def Fitur_Tambah_Bahan_Baku():
    clear_terminal()
    print("=== Tambah Bahan Baku Baru ===\n")

    try:
        nama = input("Masukkan nama bahan baku       : ").strip()
        stok_saat_ini = float(input("Masukkan stok saat ini         : "))
        stok_minimal = float(input("Masukkan stok minimal          : "))
        satuan_id = int(input("Masukkan ID satuan (angka)     : "))

        tambah_bahan_baku(nama, stok_saat_ini, stok_minimal, satuan_id)

        print(f"\n[SUKSES] Bahan baku '{nama}' berhasil ditambahkan.")
    except :
        print(f"\n[ERROR] Terjadi kesalahan")

    input("\nTekan Enter untuk kembali ke menu...")
