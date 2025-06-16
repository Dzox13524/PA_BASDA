import config
import psycopg2


def connectDB(
    host=config.hostname,
    user=config.username,
    password=config.password,
    dbname=config.database,
):
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)
        cur = conn.cursor()
        return conn, cur
    except Exception:
        print("Koneksi gagal. silahkan perbaiki!")
        return None, None


#  TAMBAH DATA
def tambah_menu(nama_menu, harga_menu, id_kategori, deskripsi, status_tersedia):
    conn, cur = connectDB()
    insert_menu_query = "INSERT INTO menu (nama_menu, harga_menu, kategori_id_kategori, deskripsi, status_tersedia) VALUES (%s, %s, %s, %s, %s)"

    cur.execute(
        insert_menu_query,
        (nama_menu, harga_menu, id_kategori, deskripsi, status_tersedia),
    )
    conn.commit()
    conn.close()


def tambah_resep(menu_id_menu, bahan_baku_id_bahan_baku, jumlah_digunakan):
    conn, cur = connectDB()
    insert_query = "INSERT INTO komposisi_menu (menu_id_menu, bahan_baku_id_bahan_baku, jumlah_digunakan) VALUES(%s, %s, %s)"

    cur.execute(
        insert_query,
        (menu_id_menu, bahan_baku_id_bahan_baku, jumlah_digunakan),
    )
    conn.commit()
    conn.close()


def tambah_bahan_baku(nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan):
    conn, cur = connectDB()
    insert_query = "INSERT INTO bahan_baku (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan) VALUES (%s, %s, %s, %s)"

    cur.execute(
        insert_query,
        (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan),
    )
    conn.commit()
    conn.close()


# LIAT DATA
def list_menu():
    conn, cur = connectDB()
    query = f"Select * from menu where status_tersedia = 'true'"
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    return data

def list_data(tabel):
    conn, cur = connectDB()
    query = f"Select * from {tabel}"
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    return data


def nama_kolom(table_name):
    conn, cursor = connectDB()
    try:
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)

        column_names = [desc[0] for desc in cursor.description]
        return column_names

    except Exception:
        print("Error saat mengeksekusi query atau mengambil kolom")
        return None, None
    finally:
        if cursor:
            cursor.close()

# Mengurangi data
def tambah_bahan_baku(nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan):
    conn, cur = connectDB()
    insert_query = "INSERT INTO bahan_baku (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan) VALUES (%s, %s, %s, %s)"

    cur.execute(
        insert_query,
        (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan),
    )
    conn.commit()
    conn.close()

# Logika pengurangan bahan baku
def kurangi_kuantitas_bahan_baku(kuantitas, id_menu):
    conn, cur = connectDB()
    try:
        query = f"""
        UPDATE bahan_baku
        SET stok_saat_ini = stok_saat_ini - (km.jumlah_digunakan * {kuantitas})
        FROM komposisi_menu km
        WHERE bahan_baku.id_bahan_baku = km.bahan_baku_id_bahan_baku
        AND km.menu_id_menu = {id_menu}
        AND stok_saat_ini >= (km.jumlah_digunakan * {kuantitas});
        """
        cur.execute(query)
        if cur.rowcount == 0:
            return False
        conn.commit()
        return True
    except Exception as e:
        print(f"[ERROR] Gagal mengurangi kuantitas bahan baku: {e}")
        return False
    finally:
        conn.close()

def tambah_kuantitas_bahan_baku(kuantitas, id_menu):
    conn, cur = connectDB()
    try:
        query = """
        UPDATE bahan_baku
        SET stok_saat_ini = stok_saat_ini + (km.jumlah_digunakan * %s)
        FROM komposisi_menu km
        WHERE bahan_baku.id_bahan_baku = km.bahan_baku_id_bahan_baku
        AND km.menu_id_menu = %s;
        """
        cur.execute(query, (kuantitas, id_menu))
        conn.commit()
        print(f"[INFO] Stok bahan baku untuk menu ID {id_menu} berhasil dikembalikan sebanyak {kuantitas} porsi.")
    except Exception as e:
        print(f"[ERROR] Gagal menambah kuantitas bahan baku: {e}")
    finally:
        conn.close()

# LOGIKA CEK OUT ITEM
def simpan_transaksi_dan_detail(keranjang_pesanan):
    conn, cur = connectDB()
    if conn is None:
        print("[ERROR] Koneksi database gagal.")
        return False
    try:
        conn.autocommit = False

        insert_transaksi_query = "INSERT INTO transaksi (tanggal_transaksi) VALUES (DEFAULT) RETURNING id_transaksi"
        insert_detail_query = """
            INSERT INTO detail_transaksi (transaksi_id_transaksi, menu_id_menu, kuantitas_pesanan, harga_jual_saat_transaksi) 
            VALUES (%s, %s, %s, %s)
        """

        cur.execute(insert_transaksi_query)
        id_transaksi_baru = cur.fetchone()[0]
        print(f"[INFO] Transaksi baru dibuat dengan ID: {id_transaksi_baru}")

        for item in keranjang_pesanan:
            cur.execute(insert_detail_query, (
                id_transaksi_baru,
                item['id_menu'],
                item['qty'],  # pastikan keynya sesuai
                item['harga_menu']
            ))

        conn.commit()
        print("[INFO] Transaksi berhasil disimpan.")
        return True

    except Exception as e:
        conn.rollback()
        print(f"[ERROR] Transaksi gagal: {e}")
        return False
    finally:
        cur.close()
        conn.close()
