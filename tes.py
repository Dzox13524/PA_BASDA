awal = 0
akhir = 50
halaman = 1
while True:
        print(awal, akhir, halaman)
        inputan = input("Pilihan Anda: ").strip().lower()
        if inputan == 'n':
            awal = akhir
            akhir += 50
            halaman += 1
            continue
        elif inputan == 'p':
            akhir = awal
            awal = akhir - 50
            halaman -= 1
            continue
        elif inputan == '':
            break