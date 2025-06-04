from Fitur.Umum.controler import clear_terminal
from tabulate import tabulate
from Fitur.User.Lihat_Daftar_Buku import sorted_data
import os 

def menu_pengelolaan_Buku(username, kabupaten, role, urutan = "JudulBuku"):
    awal = 0
    akhir = 50
    halaman = 1
    data = sorted_data(urutan)[awal:akhir]
    total_halaman = (len(sorted_data(urutan)) + 50 - 1) // 50
    while True:
        idx = 1
        clear_terminal()
        result = tabulate(data[["No","ISBN", "JudulBuku", "Penulis", "Genre", "TahunTerbit", "Stok"]], headers=["No","ISBN", "JudulBuku", "Penulis", "Genre", "TahunTerbit", "Stok"], tablefmt="fancy_grid", showindex=False, disable_numparse=True)
        result += f"\nTotal User: {len(sorted_data(urutan))} | Halaman {halaman} dari {total_halaman}\n\n"
        result += "---\n"
        for i in os.listdir("./fitur/User/Lihat_Daftar_Buku"):
            if i.endswith(".py") and i != "Menu_Lihat_DaftarUS.py" and i != "Lihat_Daftar_Buku.py":
                nama = i.replace(".py", "")
                nama = nama.replace("_", " ")
                result += f"""[{idx}] {nama}\n"""
                idx +=1
        if halaman == 1:
            result += "[L] Halaman Selanjutnya\n"
        elif halaman < total_halaman:
            result += "[P] Halaman Sebelumnya | [L] Halaman Selanjutnya\n"
        else:
            result += "[P] Halaman Sebelumnya\n"
        result += f"""[{idx}] Keluar\n"""
        result += "---\n"
        print(result)
        pilihan = input('Pilih menu: ')
        match pilihan:
            case '1':
                clear_terminal()
            case '2':
                clear_terminal()
            case '3':
                clear_terminal()
                print('Log Out')
                break
            case '4':
                clear_terminal()
            case '5':
                clear_terminal()
            case "p":
                if halaman > 1:
                    akhir = awal
                    awal = akhir - 50
                    halaman -= 1
                continue
            case "l":
                if halaman < total_halaman:
                    awal = akhir
                    akhir += 50
                    halaman += 1
                continue
            case '6':
                clear_terminal()
                break
            case ValueError:
                clear_terminal()