import pandas as pd

data = pd.read_csv("database/Akun.csv")
data_user = data.to_dict(orient='records')

def buat_tabel_bad_character(pola):
    tabel = {}
    panjang = len(pola)
    for i in range(panjang - 1):
        tabel[pola[i]] = panjang - 1 - i
    return tabel

def boyer_moore_cocok(teks, pola):
    panjang_teks = len(teks)
    panjang_pola = len(pola)

    if panjang_pola == 0:
        return True

    tabel = buat_tabel_bad_character(pola)
    posisi = 0

    while posisi <= panjang_teks - panjang_pola:
        indeks = panjang_pola - 1

        while indeks >= 0 and pola[indeks] == teks[posisi + indeks]:
            indeks -= 1

        if indeks < 0:
            return True
        else:
            karakter = teks[posisi + indeks]
            if karakter in tabel:
                lompat = tabel[karakter]
            else:
                lompat = panjang_pola
            posisi += max(1, lompat)
    return False

def pencarian(data, berdasarkan, dicari):
    data_list = data[berdasarkan].tolist()
    hasil = {}
    hasil["rekomendasi"] = []
    hasil["cocok"] = []
    data_dicari = dicari.split(" ")
    for i in data_dicari:
        data_dicari = i.lower()

        for idx, item in enumerate(data_list):
            if boyer_moore_cocok(item.lower(), data_dicari):
                
                if item.lower() == dicari.lower():
                    hasil["cocok"].append({"ditemukan":item, "index":idx})
                else:
                    hasil["rekomendasi"].append({"ditemukan":item, "index":idx})

    return hasil

print(pencarian(data, "Desa", "Sumbersari"))