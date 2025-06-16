import pandas as pd
from controler import clear_terminal

lokasiDB = 'database/'
def Fitur_Tambah_Akun_Admin():
    database = pd.read_csv(lokasiDB + 'ListLokasi.csv')
    lokasi_dict = {}
    for idx in range(len(database)):
        kecamatan = database.iloc[idx]['Kecamatan']
        desa = database.iloc[idx]['Desa']

        if kecamatan not in lokasi_dict:
            lokasi_dict[kecamatan] = []

        lokasi_dict[kecamatan].append(desa)
    ListLokasi = []
    for kecamatan in lokasi_dict:
        dict = {}
        dict['kecamatan'] = kecamatan
        dict['desa'] = lokasi_dict[kecamatan]
        ListLokasi.append(dict)
    clear_terminal()
    print("───────────────────────────────────────────")
    print("            MENAMBAH AKUN ADMIN            ")
    print("───────────────────────────────────────────\n\n")
    nama = input('Masukkan Nama        : ').capitalize()
    email = input('Masukkan Email       : ')
    NomorHp = input('Masukkan Nomor Hp    : ')
    password = input('Masukkan Password    : ')
    password2 = input('Konfirmasi Password  : ') 
    if password == password2:
            while True:
                try:
                    for index, data in enumerate(ListLokasi):
                        print(index+1, " ", data["kecamatan"])
                    Kecamatan = int(input('Masukkan angka Kecamatan: ')) - 1
                    if  0 <= Kecamatan < len(ListLokasi):
                        data = ListLokasi[Kecamatan]
                        for index, data in enumerate(ListLokasi[Kecamatan]["desa"]):
                            print(index+1, " ", data)
                        Desa = int(input('Masukkan angka Desa: ')) - 1
                        if  0 <= Desa < len(ListLokasi[Kecamatan]["desa"]):
                            database = pd.read_csv(lokasiDB + 'Akun.csv')
                            if not NomorHp.isdigit():
                                input('Nomor hp Yang Anda Masukkan Tidak Falid!')
                                return ''
                            elif NomorHp in database["Nomor_Telepon"]:
                                input('Nomor hp Yang Anda Masukkan Sudah Digunakan!')
                                return ''
                            if '@gmail.com' not in email: 
                                input('Email Yang Anda Masukkan Tidak Falid!')
                                return ''
                            elif email in database['Email'].values:
                                input('Email Yang Anda Masukkan Sudah Digunakan!')
                                return ''
                            No = len(pd.DataFrame(database))
                            Newdata = {
                                'ID': No+1,
                                'Name':nama,
                                'Email':email,
                                'Nomor_Telepon':NomorHp,
                                'Password': password,
                                'Role': 'admin',
                                'Kecamatan': kecamatan,
                                'Desa': desa
                                }
                            datanew = pd.DataFrame(Newdata, index=[0])
                            datanew.to_csv(lokasiDB + "Akun.csv",mode='a',header=False ,index=False)
                            clear_terminal()
                            print("───────────────────────────────────────────")
                            print("          AKUN ADMIN TEKAH DIBUAT         ")
                            print("───────────────────────────────────────────")
                            print(f"    ID Akun    : {data.iloc[idx]['ID']}")
                            print(f"    Nama       : {data.iloc[idx]['Name']}")
                            print(f"    Email      : {data.iloc[idx]['Email']}")
                            print(f"    Kecamatan  : {data.iloc[idx]['Kecamatan']}")
                            print(f"    Desa       : {data.iloc[idx]['Desa']}")
                            input("Ketik enter untuk melanjutkan...")
                            return ''
                        else:
                            input(f'Hanya bisa memasukkan angka [1-{len(Kecamatan)}]')
                    else:
                        input(f'Hanya bisa memasukkan angka [1-{len(ListLokasi)}]')
                except ValueError:
                    input('Hanya bisa memasukkan angka!')
    else:
        input('Password 1 dan 2 tidak sama!')
    pass