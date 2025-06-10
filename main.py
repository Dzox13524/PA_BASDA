# import Fitur.Umum
import config
from Fitur.Umum.login import login
from Fitur.Umum.register import Register
from Fitur.Umum.controler import clear_terminal
from Fitur.Umum.menu import menu
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Menu_Pengelolaan_Akun import menu_pengelolaan_akun
from Fitur.Admin.Pengelolaan_Data_Buku.Menu_Pengelolaan_Buku import menu_pengelolaan_Buku

from Fitur.User.Lihat_Daftar_Buku.Menu_Buku import U_menu_pengelolaan_Buku
while True:
        clear_terminal()
        print("""╔───────────────────────────────────────────────────╗
║               APLIKASI PERPUSTAKAAN               ║
╠───────────────────────────────────────────────────╣
║┌─────────────────────────────────────────────────┐║
║│                    OPSI MENU                    │║
║├─────────────────────────────────────────────────┤║
║├▶ 1. Registrasi                                  │║
║├▶ 2. Login                                       │║
║├▶ 3. Keluar                                      │║
║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
""".strip())
        print("")
        try:
            inputan = int(input('Masukkan nomor [1-3]: '))
            if inputan == 1:
                print(Register())
            elif inputan == 2:
                    email, username, kabupaten, desa, role,ID_User = login()
                    config.ID_Akun = ID_User
                    if username and kabupaten and desa and role:
                        while True:
                            menu(email, username, kabupaten, desa, role)
                            if role == 'admin':
                                pilihan = input('Pilih menu: ')
                                match pilihan: 
                                    case '1':
                                        menu_pengelolaan_akun()
                                        clear_terminal()
                                    case '2':
                                        menu_pengelolaan_Buku()
                                        clear_terminal()
                                    case '3':
                                        clear_terminal()
                                        input('Sedang LogOut!')     
                                        break
                                    case ValueError:
                                        clear_terminal()
                            elif role == 'user':
                                pilihan = input('Pilih menu: ')
                                match pilihan:
                                    case '1':
                                        clear_terminal()
                                    case '2':
                                        U_menu_pengelolaan_Buku()
                                    case '3':
                                        clear_terminal()
                                        input('Sedang LogOut!') 
                                        break
                                    case ValueError:
                                        clear_terminal()
                    else:
                        clear_terminal()
            elif inputan == 3:
                    clear_terminal()
                    print('Terima kasih telah menjalankan program.')
                    break
            else :
                input('Pilihan Anda tidak valid! Harap pilih angka 1, 2, atau 3')
        except (ValueError)  :
            input('Pilihan yang Anda masukkan tidak valid. Harap masukkan angka yang benar.')
