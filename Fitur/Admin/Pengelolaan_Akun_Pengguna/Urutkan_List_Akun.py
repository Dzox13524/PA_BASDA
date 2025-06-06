import config

from Fitur.Umum.controler import clear_terminal

def Fitur_Urutkan_List_Akun():
    while True:
        clear_terminal()
        print("""Urutkan Berdasarkan
1. Nama
2. Nomor Telepon
3. Kecamatan
4. Desa
5. Keluar""")
        pilihan = input("Masukkan Pilihan Anda: ")
        match pilihan:
            case '1':
                config.urutan = "Name"
                break
            case '2':
                config.urutan = "Nomor_Telepon"
                break
            case '3':
                config.urutan = "Kecamatan"
                break
            case '4':
                config.urutan = "Desa"
                break
            case '5':
                input("Ketik Enter Untuk Kemballi")
                break
            case _:
                input("Masukkan Angka [1 - 5]")