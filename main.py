import config
from controler import clear_terminal
from Fitur.Admin.menu import menu
from Fitur.Admin.Input_Transaksi_Baru import menu_pengelolaan_akun
while True:
    menu()
    pilihan = input("Pilih menu: ")
    match pilihan:
        case "1":
            menu_pengelolaan_akun()
            clear_terminal()
        case "2":
            clear_terminal()
        case "3":
            clear_terminal()
            input("Sedang LogOut!")
            break
        case ValueError:
            clear_terminal()
