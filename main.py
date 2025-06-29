import config
from controler import clear_terminal
from Fitur.Admin.menu import menu
from Fitur.Admin.Input_Transaksi_Baru import input_transaksi_baru
from Fitur.Admin.Input_Pengluaran import Fitur_Tambah_Pengeluaran
from Fitur.Admin.Laporan_Dan_Riwayat_Penjualan.Laporan_Dan_Riwayat_Penjualan import menu_Laporan
from Fitur.Admin.Manajemen_Stok_Dan_Resep.Manajemen_Stok_Dan_Resep import menu_Manajemen_Stok_Dan_Resep
from Fitur.Admin.Input_Beli_Bahan_Baku import input_beli_bahan_baku
while True:
    menu()
    pilihan = input("Pilih menu: ")
    match pilihan:
        case "1":
            input_beli_bahan_baku()
            clear_terminal()
        case "2":
            Fitur_Tambah_Pengeluaran()
            clear_terminal()
        case "3":
            input_transaksi_baru()
            clear_terminal()
        case "4":
            clear_terminal()
            menu_Laporan()
        case "5":
            clear_terminal()
            menu_Manajemen_Stok_Dan_Resep()
        case "6":
            break
        case ValueError:
            clear_terminal()
