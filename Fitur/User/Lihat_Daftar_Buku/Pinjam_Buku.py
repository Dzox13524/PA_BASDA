import config
import pandas as pd
from controler import clear_terminal, buttons,Pencarian_String

def Pinjam_Buku(ISBN, Waktu):
    data = pd.read_csv("./database/Buku.csv")
    pinjam = pd.read_csv("./database/Peminjaman.csv")
    hasil_idx = Pencarian_String(data, "ISBN", ISBN)
    if hasil_idx is None:
        input(f"[ERROR] Buku dengan ISBN '{ISBN}' tidak ditemukan.")
        return
    clear_terminal()
    No = len(pd.DataFrame(pinjam))
    Newdata = {
        'ID': f"P{No:03d}",
        'ID_User': config.ID_Akun,
        'ISBN':ISBN,
        'Durasi_Peminjaman':Waktu,
        'Tanggal_Meminjam':None,
        'Status_Pengembalian':"Permintaan_Peminjaman",
        'Tanggal_Kembali':None
            }
    datanew = pd.DataFrame([Newdata])
    datanew.to_csv("./database/Peminjaman.csv",mode='a',header=False ,index=False)
    data.loc[hasil_idx, "Stok"] -= 1
    data.to_csv("database/Buku.csv", index=False)
    input(f"Berhasil Meminjam Buku {data.loc[hasil_idx, "JudulBuku"]} Selama {Waktu} Hari!")


def Fitur_Pinjam_Buku(ISBN):
    data = pd.read_csv("./database/Buku.csv")
    hasil_idx = Pencarian_String(data, "ISBN", ISBN)
    clear_terminal()
    print(f"Kamu Ingin Meminjam {data.loc[hasil_idx, "JudulBuku"]} Berapa Hari ?")
    buttons_parameter = []
    waktu = [3,5,7]
    for i,data in enumerate(waktu):
        buttons_parameter.append({"Nama": f"{data} Hari", "command":str(i+1), "function":lambda x = data:Pinjam_Buku(ISBN, x)})
    buttons(buttons_parameter)