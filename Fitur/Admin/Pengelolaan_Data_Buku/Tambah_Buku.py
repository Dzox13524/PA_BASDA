
import pandas as pd
from datetime import datetime
import os

lokasiDB = 'database/'

def Fitur_Tambah_Buku():
    kolom_buku = [
        'ISBN', 'JudulBuku', 'Penulis', 'Penerbit',
        'JumlahHalaman', 'Genre', 'TahunTerbit', 'Stok',
        'Deskripsi', 'TanggalMasuk', 'Ketersediaan', 'TotalDipinjam'
    ]

    path_csv = lokasiDB + 'Buku.csv'
    if os.path.exists(path_csv):
        database = pd.read_csv(path_csv)
    else:
        database = pd.DataFrame(columns=kolom_buku)

    print("\n=== Tambah Buku Baru ===")
    isbn = input("ISBN                : ").strip()
    judul = input("Judul Buku          : ").strip().title()

    if isbn in database['ISBN'].values:
        judul_terdaftar = database.loc[database['ISBN'] == isbn, 'JudulBuku'].values[0]
        if judul != judul_terdaftar:
            print(f"⚠️  ISBN '{isbn}' sudah terdaftar untuk buku berjudul '{judul_terdaftar}'!")
            return

    if judul in database['JudulBuku'].values:
        isbn_terdaftar = database.loc[database['JudulBuku'] == judul, 'ISBN'].values[0]
        if isbn != isbn_terdaftar:
            print(f"⚠️  Judul buku '{judul}' sudah terdaftar dengan ISBN '{isbn_terdaftar}'!")
            return

    penulis = input("Penulis             : ").strip().title()
    penerbit = input("Penerbit            : ").strip().title()

    try:
        halaman = int(input("Jumlah Halaman      : "))
        tahun = int(input("Tahun Terbit        : "))
        stok = int(input("Stok Buku           : "))
    except ValueError:
        print("⚠️  Halaman, Tahun, dan Stok harus berupa angka!")
        return

    genre = input("Genre               : ").strip().title()
    deskripsi = input("Deskripsi Singkat   : ").strip()

    tanggal_masuk = datetime.now().strftime('%Y-%m-%d')
    ketersediaan = "Tersedia" if stok > 0 else "Kosong"
    total_dipinjam = 0

    data_baru = {
        'ISBN': isbn,
        'JudulBuku': judul,
        'Penulis': penulis,
        'Penerbit': penerbit,
        'JumlahHalaman': halaman,
        'Genre': genre,
        'TahunTerbit': tahun,
        'Stok': stok,
        'Deskripsi': deskripsi,
        'TanggalMasuk': tanggal_masuk,
        'Ketersediaan': ketersediaan,
        'TotalDipinjam': total_dipinjam
    }

    df_baru = pd.DataFrame([data_baru])
    df_baru.to_csv(path_csv, mode='a', header=not os.path.exists(path_csv), index=False)
    input(f"\n✅ Buku '{judul}' berhasil ditambahkan!")