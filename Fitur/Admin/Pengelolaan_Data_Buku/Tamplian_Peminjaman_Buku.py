import config
from Fitur.Umum.controler import clear_terminal

def Fitur_Tampilan_Peminjaman_Buku():
    while True:
        clear_terminal()
        print("""Tampilkan Berdasarkan
1. Permintaan Peminjaman
2. Menunggu Pengiriman
3. Dipinjam
4. Permintaan Pengembalian
5. Dikembalikan
6. Semua Data Peminjaman
7. Keluar""")
        pilihan = input("Masukkan Pilihan Anda: ")
        match pilihan:
            case '1':
                config.tampilanPeminjaman = "Permintaan_Peminjaman"
                break
            case '2':
                config.tampilanPeminjaman = "Menunggu_Pengiriman"
                break
            case '3':
                config.tampilanPeminjaman = "Dipinjam"
                break
            case '4':
                config.tampilanPeminjaman = "Permintaan_Pengembalian"
                break
            case '5':
                config.tampilanPeminjaman = "Dikembalikan"
                break
            case '6':
                config.tampilanPeminjaman = ""
                break
            case '7':
                input("Ketik Enter Untuk Kemballi")
                break
            case _:
                input("Masukkan Angka [1 - 7]")