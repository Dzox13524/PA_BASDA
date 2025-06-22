import config
import psycopg2
from datetime import datetime, timedelta
from calendar import monthrange


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

def beli_bahan_baku(bahan_baku_id_bahan_baku, jumlah_beli, harga_per_satuan):
    conn, cur = connectDB()
    query = "INSERT INTO pembelian_bahan_baku (bahan_baku_id_bahan_baku, jumlah_beli, harga_per_satuan) VALUES (%s, %s, %s)"
    cur.execute(
        query,
        (bahan_baku_id_bahan_baku, jumlah_beli, harga_per_satuan),
    )
    query = f"""UPDATE bahan_baku
SET stok_saat_ini = stok_saat_ini + {jumlah_beli}
WHERE id_bahan_baku = {bahan_baku_id_bahan_baku}"""
    cur.execute(
        query,
        (bahan_baku_id_bahan_baku, jumlah_beli, harga_per_satuan),
    )
    conn.commit()
    conn.close()
    return True

def tambah_bahan_baku(nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan):
    conn, cur = connectDB()
    insert_query = "INSERT INTO bahan_baku (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan) VALUES (%s, %s, %s, %s)"

    cur.execute(
        insert_query,
        (nama_bahan, stok_saat_ini, stok_minimal, satuan_id_satuan),
    )
    conn.commit()
    conn.close()


def tambah_pengeluaran(tanggal_pengeluaran, deskripsi, jumlah):
    conn, cur = connectDB()
    insert_query = """
    INSERT INTO pengeluaran (tanggal_pengeluaran, deskripsi, jumlah)
    VALUES (%s, %s, %s)
    """
    cur.execute(insert_query, (tanggal_pengeluaran, deskripsi, jumlah))
    conn.commit()
    conn.close()


# LIAT DATA
def get_total_penjualan_hari_ini():
    conn, cur = connectDB()

    query = """
    SELECT
        SUM(dt.kuantitas_pesanan) AS total_menu_terjual,
        SUM(dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi) AS total_pendapatan
    FROM transaksi t
    JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
    WHERE (t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta')::DATE = (CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')::DATE;
    """

    with conn.cursor() as cur:
        cur.execute(query)
        hasil = cur.fetchone()
        total_terjual = hasil[0] if hasil[0] is not None else 0
        total_pendapatan = hasil[1] if hasil[1] is not None else 0
        return total_terjual, total_pendapatan


def list_menu():
    conn, cur = connectDB()
    query = """SELECT id_menu, nama_menu, deskripsi, harga_menu
        FROM menu
        WHERE status_tersedia = 'true'
        ORDER BY id_menu ASC"""
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    return data


def list_data(tabel, urutan):
    conn, cur = connectDB()
    query = f"Select * from {tabel} order by {urutan}"
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


def get_pengeluaran(periode):
    conn, cur = connectDB()

    if periode == "tahun":
        query = """
        SELECT tanggal_pengeluaran, deskripsi, jumlah
        FROM pengeluaran
        WHERE EXTRACT(YEAR FROM tanggal_pengeluaran) = EXTRACT(YEAR FROM CURRENT_DATE)
        ORDER BY tanggal_pengeluaran;
        """
        params = ()
    elif periode == "bulan":
        query = """
        SELECT tanggal_pengeluaran, deskripsi, jumlah
        FROM pengeluaran
        WHERE EXTRACT(YEAR FROM tanggal_pengeluaran) = EXTRACT(YEAR FROM CURRENT_DATE)
          AND EXTRACT(MONTH FROM tanggal_pengeluaran) = EXTRACT(MONTH FROM CURRENT_DATE)
        ORDER BY tanggal_pengeluaran;
        """
        params = ()
    elif periode == "minggu":
        query = """
        SELECT tanggal_pengeluaran, deskripsi, jumlah
        FROM pengeluaran
        WHERE EXTRACT(YEAR FROM tanggal_pengeluaran) = EXTRACT(YEAR FROM CURRENT_DATE)
          AND EXTRACT(WEEK FROM tanggal_pengeluaran) = EXTRACT(WEEK FROM CURRENT_DATE)
        ORDER BY tanggal_pengeluaran;
        """
        params = ()
    else:
        raise ValueError("Periode harus 'minggu', 'bulan', atau 'tahun'")

    with conn.cursor() as cur:
        cur.execute(query, params)
        return cur.fetchall()

def get_bahan_baku_kritis():
    conn, cur = connectDB()
    query = """
    SELECT 
        bb.id_bahan_baku, 
        bb.nama_bahan, 
        bb.stok_saat_ini, 
        bb.stok_minimal 
    FROM bahan_baku bb
    WHERE bb.stok_saat_ini <= bb.stok_minimal
    ORDER BY bb.stok_saat_ini ASC;
    """
    cur.execute(query)
    data = cur.fetchall()
    jumlah = len(data)
    cur.close()
    conn.close()

    return jumlah, data

def get_detail_riwayat_transaksi(periode=None):
    conn, cur = connectDB()

    if periode == "tahun":
        query = """
        SELECT
            t.tanggal_transaksi,
            t.id_transaksi,
            m.nama_menu,
            dt.kuantitas_pesanan,
            dt.harga_jual_saat_transaksi,
            (dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi) AS subtotal_item,
            totals.total_bayar_transaksi
        FROM transaksi t
        JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
        JOIN menu m ON dt.menu_id_menu = m.id_menu
        JOIN (
            SELECT 
                transaksi_id_transaksi,
                SUM(kuantitas_pesanan * harga_jual_saat_transaksi) AS total_bayar_transaksi
            FROM detail_transaksi
            GROUP BY transaksi_id_transaksi
        ) totals ON t.id_transaksi = totals.transaksi_id_transaksi
        WHERE EXTRACT(YEAR FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(YEAR FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
        ORDER BY t.tanggal_transaksi DESC, t.id_transaksi, m.nama_menu;
        """
        params = ()
    elif periode == "bulan":
        query = """
        SELECT
            t.tanggal_transaksi,
            t.id_transaksi,
            m.nama_menu,
            dt.kuantitas_pesanan,
            dt.harga_jual_saat_transaksi,
            (dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi) AS subtotal_item,
            totals.total_bayar_transaksi
        FROM transaksi t
        JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
        JOIN menu m ON dt.menu_id_menu = m.id_menu
        JOIN (
            SELECT 
                transaksi_id_transaksi,
                SUM(kuantitas_pesanan * harga_jual_saat_transaksi) AS total_bayar_transaksi
            FROM detail_transaksi
            GROUP BY transaksi_id_transaksi
        ) totals ON t.id_transaksi = totals.transaksi_id_transaksi
        WHERE EXTRACT(YEAR FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(YEAR FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
          AND EXTRACT(MONTH FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(MONTH FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
        ORDER BY t.tanggal_transaksi DESC, t.id_transaksi, m.nama_menu;
        """
        params = ()
    elif periode == "minggu":
        query = """
        SELECT
            t.tanggal_transaksi,
            t.id_transaksi,
            m.nama_menu,
            dt.kuantitas_pesanan,
            dt.harga_jual_saat_transaksi,
            (dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi) AS subtotal_item,
            totals.total_bayar_transaksi
        FROM transaksi t
        JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
        JOIN menu m ON dt.menu_id_menu = m.id_menu
        JOIN (
            SELECT 
                transaksi_id_transaksi,
                SUM(kuantitas_pesanan * harga_jual_saat_transaksi) AS total_bayar_transaksi
            FROM detail_transaksi
            GROUP BY transaksi_id_transaksi
        ) totals ON t.id_transaksi = totals.transaksi_id_transaksi
        WHERE EXTRACT(YEAR FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(YEAR FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
          AND EXTRACT(WEEK FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(WEEK FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
        ORDER BY t.tanggal_transaksi DESC, t.id_transaksi, m.nama_menu;
        """
        params = ()
    elif periode is None:
        query = """
        SELECT
            t.tanggal_transaksi,
            t.id_transaksi,
            m.nama_menu,
            dt.kuantitas_pesanan,
            dt.harga_jual_saat_transaksi,
            (dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi) AS subtotal_item,
            totals.total_bayar_transaksi
        FROM transaksi t
        JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
        JOIN menu m ON dt.menu_id_menu = m.id_menu
        JOIN (
            SELECT 
                transaksi_id_transaksi,
                SUM(kuantitas_pesanan * harga_jual_saat_transaksi) AS total_bayar_transaksi
            FROM detail_transaksi
            GROUP BY transaksi_id_transaksi
        ) totals ON t.id_transaksi = totals.transaksi_id_transaksi
        ORDER BY t.tanggal_transaksi DESC, t.id_transaksi, m.nama_menu;
        """
        params = ()
    else:
        raise ValueError("Periode harus 'minggu', 'bulan', 'tahun', atau None")

    with conn.cursor() as cur:
        cur.execute(query, params)
        return cur.fetchall()


def get_laporan_penjualan_per_menu(periode=None):
    conn, cur = connectDB()

    filter_clause = ""
    if periode == "minggu":
        filter_clause = """
        WHERE EXTRACT(YEAR FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(YEAR FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
          AND EXTRACT(WEEK FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(WEEK FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
        """
    elif periode == "bulan":
        filter_clause = """
        WHERE EXTRACT(YEAR FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(YEAR FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
          AND EXTRACT(MONTH FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(MONTH FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
        """
    elif periode == "tahun":
        filter_clause = """
        WHERE EXTRACT(YEAR FROM t.tanggal_transaksi AT TIME ZONE 'Asia/Jakarta') = EXTRACT(YEAR FROM CURRENT_DATE AT TIME ZONE 'Asia/Jakarta')
        """
    elif periode is None:
        filter_clause = ""
    else:
        raise ValueError("Periode harus 'minggu', 'bulan', 'tahun', atau None")

    query = f"""
    SELECT 
        m.nama_menu,
        SUM(dt.kuantitas_pesanan) AS total_terjual,
        SUM(dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi) AS total_pendapatan
    FROM transaksi t
    JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
    JOIN menu m ON dt.menu_id_menu = m.id_menu
    {filter_clause}
    GROUP BY m.nama_menu
    ORDER BY total_terjual DESC;
    """

    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


# Logic kurang tambah bahan baku
def kurangi_kuantitas_bahan_baku(kuantitas, id_menu):
    conn, cur = connectDB()
    try:
        cek_query = """
        SELECT bb.nama_bahan, bb.stok_saat_ini, km.jumlah_digunakan
        FROM komposisi_menu km
        JOIN bahan_baku bb ON km.bahan_baku_id_bahan_baku = bb.id_bahan_baku
        WHERE km.menu_id_menu = %s
        """
        cur.execute(cek_query, (id_menu,))
        data = cur.fetchall()

        for nama_bahan, stok, jumlah in data:
            if stok < jumlah * kuantitas:
                print(f"[ERROR] Stok bahan '{nama_bahan}' tidak cukup.")
                return False

        update_query = """
        UPDATE bahan_baku
        SET stok_saat_ini = stok_saat_ini - (km.jumlah_digunakan * %s)
        FROM komposisi_menu km
        WHERE bahan_baku.id_bahan_baku = km.bahan_baku_id_bahan_baku
        AND km.menu_id_menu = %s
        """
        cur.execute(update_query, (kuantitas, id_menu))
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
        print(
            f"[INFO] Stok bahan baku untuk menu ID {id_menu} berhasil dikembalikan sebanyak {kuantitas} porsi."
        )
    except Exception as e:
        print(f"[ERROR] Gagal menambah kuantitas bahan baku: {e}")
    finally:
        conn.close()


def simpan_transaksi_dan_detail(keranjang):
    try:
        conn, cur = connectDB()
        if not conn or not cur:
            print("[ERROR] Koneksi database gagal.")
            return False

        cur.execute("BEGIN")

        cur.execute(
            "INSERT INTO transaksi (tanggal_transaksi) VALUES (DEFAULT) RETURNING id_transaksi"
        )
        id_transaksi_baru = cur.fetchone()[0]
        print(f"[INFO] Transaksi baru dibuat dengan ID: {id_transaksi_baru}")

        insert_detail_query = """
            INSERT INTO detail_transaksi 
                (transaksi_id_transaksi, menu_id_menu, kuantitas_pesanan, harga_jual_saat_transaksi)
            VALUES (%s, %s, %s, %s)
        """

        update_stok_query = """
            UPDATE bahan_baku 
            SET stok_saat_ini = stok_saat_ini - (km.jumlah_digunakan * %s)
            FROM komposisi_menu km
            WHERE bahan_baku.id_bahan_baku = km.bahan_baku_id_bahan_baku
              AND km.menu_id_menu = %s
        """

        for item in keranjang:
            cur.execute(
                insert_detail_query,
                (id_transaksi_baru, item["id_menu"], item["kuantitas"], item["harga"]),
            )

            cur.execute(update_stok_query, (item["kuantitas"], item["id_menu"]))

        conn.commit()
        cur.close()
        conn.close()
        return True

    except Exception as e:
        if conn:
            conn.rollback()
            cur.close()
            conn.close()
        print(f"[ERROR] Terjadi kesalahan saat menyimpan transaksi: {e}")
        return False


# PENGECEKAN UPDATE STATUS MENU
def periksa_dan_update_status_menu():
    conn, cur = connectDB()

    cur.execute("SELECT id_menu FROM menu")
    semua_menu = cur.fetchall()

    for (id_menu,) in semua_menu:
        query = """
            SELECT bb.stok_saat_ini, bb.stok_minimal
            FROM komposisi_menu km
            JOIN bahan_baku bb ON km.bahan_baku_id_bahan_baku = bb.id_bahan_baku
            WHERE km.menu_id_menu = %s
        """
        cur.execute(query, (id_menu,))
        bahan_baku = cur.fetchall()

        status_tersedia = True
        for stok_saat_ini, stok_minimal in bahan_baku:
            if stok_saat_ini <= stok_minimal:
                status_tersedia = False
                break

        update_query = """
            UPDATE menu SET status_tersedia = %s WHERE id_menu = %s
        """
        cur.execute(update_query, (status_tersedia, id_menu))

    conn.commit()
    conn.close()
