import config
from Fitur.Umum.controler import clear_terminal

def Fitur_Urutkan_List_Buku():
    while True:
        clear_terminal()
        print("""Urutkan Berdasarkan
1. Judul Buku
2. Penulis
3. Penerbit
4. Genre
5. Tahun Terbit
6. Stok
7. Keluar""")
        pilihan = input("Masukkan Pilihan Anda: ")
        match pilihan:
            case '1':
                config.urutanBuku = "JudulBuku"
                break
            case '2':
                config.urutanBuku = "Penulis"
                break
            case '3':
                config.urutanBuku = "Penerbit"
                break
            case '4':
                config.urutanBuku = "Genre"
                break
            case '5':
                config.urutanBuku = "TahunTerbit"
                break
            case '6':
                config.urutanBuku = "Stok"
                break
            case '7':
                input("Ketik Enter Untuk Kemballi")
                break
            case _:
                input("Masukkan Angka [1 - 7]")