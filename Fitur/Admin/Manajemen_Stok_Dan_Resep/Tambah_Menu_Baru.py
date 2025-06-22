from database.connection import connectDB, list_data
from controler import clear_terminal


def Fitur_Tambah_Menu_Baru():
    clear_terminal()
    conn, cur = connectDB()

    print("=== Tambah Menu Baru ===")
    nama = input("Nama Menu: ")
    deskripsi = input("Deskripsi: ")

    try:
        harga = float(input("Harga Menu: "))
    except ValueError:
        input("[ERROR] Harga tidak valid.")
        return

    kategori_data = list_data("kategori", "id_kategori")
    if not kategori_data:
        input("[ERROR] Tidak ada kategori tersedia.")
        return

    print("\nPilih Kategori:")
    for i, kat in enumerate(kategori_data):
        print(f"{i + 1}. {kat[1]}")
    try:
        pilih_kat = int(input("Masukkan nomor kategori: "))
        kategori_id = kategori_data[pilih_kat - 1][0]
    except (IndexError, ValueError):
        input("[ERROR] Pilihan tidak valid.")
        return

    cur.execute(
        """
        INSERT INTO menu (nama_menu, deskripsi, harga_menu, status_tersedia, kategori_id_kategori)
        VALUES (%s, %s, %s, TRUE, %s) RETURNING id_menu
        """,
        (nama, deskripsi, harga, kategori_id),
    )
    id_menu = cur.fetchone()[0]
    conn.commit()

    input("\n[INFO] Lanjutkan ke pengisian komposisi bahan baku...")

    while True:
        clear_terminal()
        print("=== Tambahkan Komposisi Menu ===")

        bahan_data = list_data("bahan_baku", "id_bahan_baku")
        print("\nPilih bahan baku:")
        for i, bb in enumerate(bahan_data):
            print(f"{i + 1}. {bb[1]}")
        print(f"{len(bahan_data) + 1}. Tambah Bahan Baru")

        try:
            pilih = int(input("Masukkan pilihan: "))
            if pilih == len(bahan_data) + 1:
                nama_baru = input("Nama Bahan Baru: ")
                satuan_data = list_data("satuan", "id_satuan")
                for i, s in enumerate(satuan_data):
                    print(f"{i + 1}. {s[1]}")
                pilih_satuan = int(input("Pilih satuan: "))
                satuan_id = satuan_data[pilih_satuan - 1][0]
                cur.execute(
                    """
                    INSERT INTO bahan_baku (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan)
                    VALUES (%s, 0, 0, %s) RETURNING id_bahan_baku
                    """,
                    (nama_baru, satuan_id),
                )
                bahan_id = cur.fetchone()[0]
                conn.commit()
            else:
                bahan_id = bahan_data[pilih - 1][0]
        except (ValueError, IndexError):
            input("[ERROR] Pilihan tidak valid.")
            continue

        try:
            jumlah = float(input("Jumlah digunakan: "))
        except ValueError:
            input("[ERROR] Jumlah tidak valid.")
            continue

        cur.execute(
            """
            INSERT INTO komposisi_menu (menu_id_menu, bahan_baku_id_bahan_baku, jumlah_digunakan)
            VALUES (%s, %s, %s)
            """,
            (id_menu, bahan_id, jumlah),
        )
        conn.commit()
        lanjut = input("Tambah bahan lain? (y/n): ").strip().lower()
        if lanjut != "y":
            break

    input("[INFO] Menu berhasil ditambahkan.")
    conn.close()
