# import Fitur.Umum
from  Fitur.Umum.login import login
from Fitur.Umum.register import Register
from Fitur.Umum.controler import clear_terminal
from Fitur.Umum.menu import menu
from Fitur.Admin.Pengelolaan_Akun_Pengguna.Menu_Pengelolaan_Akun import menu_pengelolaan_akun
from Fitur.Admin.Pengelolaan_Data_Buku.Menu_Pengelolaan_Buku import menu_pengelolaan_Buku

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
                    email, username, kabupaten, desa, role = login()
                    if username and kabupaten and desa and role:
                        while True:
                            menu(email, username, kabupaten, desa, role)
                            if role == 'admin':
                                pilihan = input('Pilih menu: ')
                                match pilihan: 
                                    case '1':
                                        menu_pengelolaan_akun(username, kabupaten, role)
                                        clear_terminal()
                                    case '2':
                                        menu_pengelolaan_Buku(username, kabupaten, role)
                                        clear_terminal()
                                    case '3':
                                        clear_terminal()
                                        print('Log Out')     
                                        break
                                    case ValueError:
                                        clear_terminal()
                            elif role == 'user':
                                pilihan = input('Pilih menu: ')
                                match pilihan:
                                    case '1':
                                        clear_terminal()
                                        input('Tekan enter untuk melanjutkan!')
                                    case '2':
                                        clear_terminal()
                                        input('Tekan enter untuk melanjutkan!')
                                    case '3':
                                        clear_terminal()
                                        input('Tekan enter untuk melanjutkan!')
                                    case '4':
                                        clear_terminal()
                                        input('Tekan enter untuk melanjutkan!')
                                    case '5':
                                        clear_terminal()
                                        input('Tekan enter untuk melanjutkan!')
                                    case '6':
                                        clear_terminal()
                                        print('Log Out') 
                                        break
                                    case ValueError:
                                        clear_terminal()
                    else:
                        clear_terminal()
            elif inputan == 3:
                    
                    break
            else :
                input('Pilihan Anda tidak valid! Harap pilih angka 1, 2, atau 3')
        except (ValueError)  :
            input('Pilihan yang Anda masukkan tidak valid. Harap masukkan angka yang benar.')
