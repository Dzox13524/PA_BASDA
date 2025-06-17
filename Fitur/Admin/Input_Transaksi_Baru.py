import os
import config
from controler import buttons, clear_terminal
from tabulate import tabulate
from database.connection import list_data, kurangi_kuantitas_bahan_baku, tambah_kuantitas_bahan_baku, simpan_transaksi_dan_detail, nama_kolom, periksa_dan_update_status_menu

def input_transaksi_baru(urutan=config.urutanUser):
    awal = 0
    akhir = 50
    halaman = 1
    cart = []

    def lanjut():
        nonlocal awal, akhir, halaman
        awal = akhir
        akhir += 50
        halaman += 1

    def kembali():
        nonlocal awal, akhir, halaman
        akhir = awal
        awal = akhir - 50
        halaman -= 1

    def tambah_ke_cart(item):
        try:
            qty = int(input(f"Berapa jumlah '{item[1]}' yang ingin ditambahkan? "))
            if qty < 1:
                input("[ERROR] Jumlah harus lebih dari 0.")
                return
        except ValueError:
            input("[ERROR] Input tidak valid.")
            return

        if not kurangi_kuantitas_bahan_baku(qty, item[0]):
            input(f"[INFO] Stok bahan baku tidak cukup untuk menambahkan {qty} porsi '{item[1]}'.")
            return

        for i in cart:
            if i['id_menu'] == item[0]:
                i['qty'] += qty
                i['total'] = i['qty'] * i['harga_menu']
                input(f"[INFO] Jumlah '{item[1]}' di keranjang ditambah menjadi {i['qty']}.")
                return

        cart.append({
            "id_menu": item[0],
            "nama_menu": item[1],
            "harga_menu": item[3],
            "qty": qty,
            "total": qty * item[3]
        })
        input(f"[INFO] '{item[1]}' berhasil dimasukkan ke dalam keranjang.")

    def lihat_cart():
        while True:
            clear_terminal()
            if not cart:
                input("[INFO] Keranjang kosong.")
                break

            print("[KERANJANG SAAT INI]")
            rows = [[i["id_menu"], i["nama_menu"], i["harga_menu"], i["qty"], i["total"]] for i in cart]
            print(tabulate(rows, headers=["ID Menu", "Nama Menu", "Harga", "Qty", "Total"], tablefmt="grid"))

            print("\n[Pilih opsi:]")
            print("1. Tambah jumlah item")
            print("2. Kurangi jumlah item")
            print("3. Hapus item")
            print("4. Kembali")

            pilihan = input("Pilihan (1/2/3/4): ").strip()
            if pilihan == "4":
                break
            if pilihan not in ["1", "2", "3"]:
                input("[WARN] Pilihan tidak valid. Tekan Enter untuk ulang.")
                continue

            try:
                id_menu = int(input("Masukkan ID Menu yang ingin dimodifikasi: "))
                item = next((i for i in cart if i["id_menu"] == id_menu), None)
                if not item:
                    input("[WARN] ID tidak ditemukan di keranjang.")
                    continue
            except ValueError:
                input("[ERROR] Input ID harus angka.")
                continue

            if pilihan == "1":
                try:
                    tambah = int(input("Tambah berapa jumlah? "))
                    if tambah < 1:
                        input("[ERROR] Jumlah harus > 0.")
                        continue
                    if not kurangi_kuantitas_bahan_baku(tambah, item["id_menu"]):
                        input(f"[INFO] Stok bahan baku tidak cukup untuk menambah {tambah} porsi.")
                        continue
                    item["qty"] += tambah
                    item["total"] = item["qty"] * item["harga_menu"]
                    input(f"[INFO] Jumlah '{item['nama_menu']}' jadi {item['qty']}.")
                except ValueError:
                    input("[ERROR] Input tidak valid.")

            elif pilihan == "2":
                try:
                    kurang = int(input("Kurangi berapa jumlah? "))
                    if kurang < 1:
                        input("[ERROR] Jumlah harus > 0.")
                        continue
                    if kurang > item["qty"]:
                        input(f"[ERROR] Jumlah yang dikurangi melebihi jumlah dalam keranjang ({item['qty']}).")
                        continue
                    elif kurang == item["qty"]:
                        input(f"[ERROR] Tidak bisa mengurangi hingga habis. Gunakan opsi hapus item [3] jika ingin menghapus.")
                        continue
                    else:
                        item["qty"] -= kurang
                        item["total"] = item["qty"] * item["harga_menu"]
                        tambah_kuantitas_bahan_baku(kurang, item["id_menu"])
                        input(f"[INFO] Jumlah '{item['nama_menu']}' jadi {item['qty']}.")
                except ValueError:
                    input("[ERROR] Input tidak valid.")

            elif pilihan == "3":
                tambah_kuantitas_bahan_baku(item["qty"], item["id_menu"])
                cart.remove(item)
                input(f"[INFO] Item '{item['nama_menu']}' berhasil dihapus.")

    def checkout():
        if not cart:
            input("[INFO] Keranjang masih kosong, tidak bisa checkout.")
            return

        print("[INFO] Memproses checkout...")
        keranjang_format = [{"id_menu": i["id_menu"], "kuantitas": i["qty"], "harga": i["harga_menu"]} for i in cart]
        berhasil = simpan_transaksi_dan_detail(keranjang_format)
        periksa_dan_update_status_menu()
        if berhasil:
            cart.clear()
            input("[INFO] Transaksi berhasil disimpan dan keranjang dikosongkan.")
        else:
            input("[ERROR] Terjadi kesalahan saat menyimpan transaksi.")

    loop = True
    while loop:
        clear_terminal()
        data = list_data('menu')
        total_halaman = (len(data) + 50 - 1) // 50
        halaman_data = data[awal:akhir]
        columns = nama_kolom('menu')
        print(f"\n=== MENU | Halaman {halaman}/{total_halaman} ===")
        print(tabulate(halaman_data, headers=columns, tablefmt="grid"))

        buttons_parameter = [{
            "Nama": f"Pilih [1 - {len(halaman_data)}] untuk masukkan ke keranjang",
            "command": [1, len(halaman_data)],
            "function": lambda i: tambah_ke_cart(halaman_data[i])
        }]

        if halaman == 1 and total_halaman > 1:
            buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command": "l", "function": lanjut})
        elif halaman < total_halaman:
            buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command": "p", "function": kembali})
            buttons_parameter.append({"Nama": "Halaman Selanjutnya", "command": "l", "function": lanjut})
        elif halaman > 1:
            buttons_parameter.append({"Nama": "Halaman Sebelumnya", "command": "p", "function": kembali})

        buttons_parameter.append({"Nama": "Lihat Keranjang", "command": "c", "function": lihat_cart})
        buttons_parameter.append({"Nama": "Checkout dan Simpan Transaksi", "command": "x", "function": checkout})

        loop = buttons(buttons_parameter)
