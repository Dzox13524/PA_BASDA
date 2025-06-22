from database.connection import connectDB
from controler import clear_terminal


def Fitur_Lihat_Laba():
    def get_filter_query(periode):
        if periode == "hari":
            return "WHERE t.tanggal_transaksi::DATE = CURRENT_DATE"
        elif periode == "bulan":
            return """WHERE EXTRACT(MONTH FROM t.tanggal_transaksi) = EXTRACT(MONTH FROM CURRENT_DATE)
                      AND EXTRACT(YEAR FROM t.tanggal_transaksi) = EXTRACT(YEAR FROM CURRENT_DATE)"""
        elif periode == "tahun":
            return "WHERE EXTRACT(YEAR FROM t.tanggal_transaksi) = EXTRACT(YEAR FROM CURRENT_DATE)"
        else:
            return ""

    while True:
        clear_terminal()
        print("=== LIHAT KEUNTUNGAN ===")
        print("1. Hari Ini")
        print("2. Bulan Ini")
        print("3. Tahun Ini")
        print("4. Semua Waktu")
        print("5. Kembali")

        pilihan = input("Pilih opsi (1-5): ").strip()
        if pilihan == "5":
            break

        periode_map = {
            "1": ("hari", "Hari Ini"),
            "2": ("bulan", "Bulan Ini"),
            "3": ("tahun", "Tahun Ini"),
            "4": ("semua", "Semua Waktu"),
        }

        if pilihan not in periode_map:
            input("[WARN] Pilihan tidak valid.")
            continue

        periode_filter, label = periode_map[pilihan]
        filter_query = get_filter_query(periode_filter)

        conn, cur = connectDB()
        query = f"""
        SELECT
            (
                SELECT SUM(dt.kuantitas_pesanan * dt.harga_jual_saat_transaksi)
                FROM transaksi t
                JOIN detail_transaksi dt ON t.id_transaksi = dt.transaksi_id_transaksi
                {filter_query}
            )
            -
            (
                SELECT SUM(bb.jumlah_beli * bb.harga_per_satuan)
                FROM pembelian_bahan_baku bb
                -- PENTING: Penyesuaian filter untuk tanggal_pembelian
                {filter_query.replace("t.tanggal_transaksi", "bb.tanggal_pembelian")}
            ) AS total_keuntungan;
        """

        try:
            cur.execute(query)
            hasil = cur.fetchone()
            keuntungan = hasil[0]

            if keuntungan is None:
                print(
                    f"\n[INFO] Tidak ada data transaksi atau pembelian bahan baku pada periode {label}."
                )
            else:
                print(f"\n[INFO] Total Keuntungan {label}: Rp {keuntungan:,.0f}")

        except Exception as e:
            print(f"\n[ERROR] Terjadi kesalahan saat mengambil data: {e}")
        finally:
            if conn:
                conn.close()

        input("\nTekan Enter untuk kembali...")
