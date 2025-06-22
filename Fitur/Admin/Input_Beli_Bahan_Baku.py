import os
import config
from controler import buttons, clear_terminal
from tabulate import tabulate
from database.connection import (
    list_data,
    beli_bahan_baku,
    nama_kolom,
)


def input_beli_bahan_baku():
    awal = 0
    akhir = 50
    halaman = 1
    cart = []

    def lanjut():
        nonlocal awal, akhir, halaman
        if akhir < len(list_data("bahan_baku", "id_bahan_baku")):
            awal = akhir
            akhir += 50
            halaman += 1

    def kembali():
        nonlocal awal, akhir, halaman
        if awal > 0:
            akhir = awal
            awal = max(0, akhir - 50)
            halaman -= 1

    def tambah_ke_cart(item):
        try:
            qty = int(input(f"Berapa jumlah '{item[1]}' yang ingin dibeli? "))
            if qty < 1:
                input("[ERROR] Jumlah harus lebih dari 0.")
                return
        except ValueError:
            input("[ERROR] Input tidak valid untuk jumlah.")
            return

        try:
            harga_satuan = float(input(f"Masukkan harga satuan untuk '{item[1]}': "))
            if harga_satuan < 0:
                input("[ERROR] Harga tidak boleh negatif.")
                return
        except ValueError:
            input("[ERROR] Input tidak valid untuk harga.")
            return

        for i in cart:
            if i["id_bahan_baku"] == item[0]:
                i["qty"] += qty
                i["total"] = i["qty"] * harga_satuan
                i["harga_satuan"] = harga_satuan 
                input(f"[INFO] Jumlah '{item[1]}' di keranjang ditambah menjadi {i['qty']}.")
                return

        cart.append(
            {
                "id_bahan_baku": item[0],
                "nama_bahan": item[1],
                "harga_satuan": harga_satuan,
                "qty": qty,
                "total": qty * harga_satuan,
            }
        )
        input(f"[INFO] '{item[1]}' berhasil dimasukkan ke dalam keranjang.")

    def lihat_cart():
        while True:
            clear_terminal()
            if not cart:
                input("[INFO] Keranjang kosong.")
                break

            print("[KERANJANG PEMBELIAN BAHAN BAKU]")
            rows = [
                [
                    i["id_bahan_baku"],
                    i["nama_bahan"],
                    i["harga_satuan"],
                    i["qty"],
                    i["total"],
                ]
                for i in cart
            ]
            print(
                tabulate(
                    rows,
                    headers=["ID Bahan", "Nama Bahan", "Harga Satuan", "Qty", "Total"],
                    tablefmt="grid",
                )
            )

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
                id_bahan = int(
                    input("Masukkan ID Bahan Baku yang ingin dimodifikasi: ")
                )
                item = next((i for i in cart if i["id_bahan_baku"] == id_bahan), None)
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
                    item["qty"] += tambah
                    item["total"] = item["qty"] * item["harga_satuan"]
                    input(f"[INFO] Jumlah '{item['nama_bahan']}' jadi {item['qty']}.")
                except ValueError:
                    input("[ERROR] Input tidak valid.")

            elif pilihan == "2":
                try:
                    kurang = int(input("Kurangi berapa jumlah? "))
                    if kurang < 1:
                        input("[ERROR] Jumlah harus > 0.")
                        continue
                    if kurang > item["qty"]:
                        input(
                            f"[ERROR] Jumlah yang dikurangi melebihi jumlah dalam keranjang ({item['qty']})."
                        )
                        continue
                    elif kurang == item["qty"]:
                        input(
                            f"[ERROR] Tidak bisa mengurangi hingga habis. Gunakan opsi hapus item [3] jika ingin menghapus."
                        )
                        continue
                    else:
                        item["qty"] -= kurang
                        item["total"] = item["qty"] * item["harga_satuan"]
                        input(
                            f"[INFO] Jumlah '{item['nama_bahan']}' jadi {item['qty']}."
                        )
                except ValueError:
                    input("[ERROR] Input tidak valid.")

            elif pilihan == "3":
                cart.remove(item)
                input(f"[INFO] Item '{item['nama_bahan']}' berhasil dihapus.")

    def checkout():
        if not cart:
            input("[INFO] Keranjang masih kosong, tidak bisa checkout.")
            return

        print("[INFO] Memproses pembelian bahan baku...")

        sukses_semua = True
        for item in cart:
            berhasil = beli_bahan_baku(
                item["id_bahan_baku"], item["qty"], item["harga_satuan"]
            )
            if not berhasil:
                print(
                    f"[ERROR] Gagal menyimpan pembelian bahan baku '{item['nama_bahan']}'"
                )
                sukses_semua = False

        if sukses_semua:
            input(
                "[INFO] Pembelian bahan baku berhasil disimpan dan keranjang dikosongkan."
            )
            cart.clear()
        else:
            input("[ERROR] Terjadi kesalahan saat menyimpan pembelian bahan baku.")

    loop = True
    while loop:
        clear_terminal()
        data = list_data("bahan_baku", "id_bahan_baku")
        total_halaman = (len(data) + 50 - 1) // 50
        halaman_data = data[awal:akhir]
        columns = nama_kolom("bahan_baku")
        print(f"\n=== DAFTAR BAHAN BAKU | Halaman {halaman}/{total_halaman} ===")
        print(tabulate(halaman_data, headers=columns, tablefmt="grid"))

        buttons_parameter = [
            {
                "Nama": f"Pilih [1 - {len(halaman_data)}] untuk masukkan ke keranjang",
                "command": [1, len(halaman_data)],
                "function": lambda i: tambah_ke_cart(halaman_data[i]),
            }
        ]

        if halaman == 1 and total_halaman > 1:
            buttons_parameter.append(
                {"Nama": "Halaman Selanjutnya", "command": "l", "function": lanjut}
            )
        elif halaman < total_halaman:
            buttons_parameter.append(
                {"Nama": "Halaman Sebelumnya", "command": "p", "function": kembali}
            )
            buttons_parameter.append(
                {"Nama": "Halaman Selanjutnya", "command": "l", "function": lanjut}
            )
        elif halaman > 1:
            buttons_parameter.append(
                {"Nama": "Halaman Sebelumnya", "command": "p", "function": kembali}
            )

        buttons_parameter.append(
            {
                "Nama": "Lihat Keranjang Pembelian",
                "command": "c",
                "function": lihat_cart,
            }
        )
        buttons_parameter.append(
            {
                "Nama": "Checkout dan Simpan Pembelian",
                "command": "x",
                "function": checkout,
            }
        )

        loop = buttons(buttons_parameter)
