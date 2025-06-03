import pandas as pd
lokasiDB = 'database/'
def Register():
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

    nama = input('Masukkan Nama        : ').capitalize()
    email = input('Masukkan Email       : ')
    NomorHp = input('Masukkan Nomor Hp       : ')
    password = input('Masukkan Password    : ')
    password2 = input('Konfirmasi Password  : ') 
    if password == password2:
            while True:
                try:
                    for index, data in enumerate(ListLokasi):
                        print(index+1, " ", data["kecamatan"])
                    Kecamatan = int(input('masukkan angka Kecamatan: ')) - 1
                    if  0 <= Kecamatan < len(ListLokasi):
                        data = ListLokasi[Kecamatan]
                        for index, data in enumerate(ListLokasi[Kecamatan]["desa"]):
                            print(index+1, " ", data)
                        Desa = int(input('masukkan angka Desa: ')) - 1
                        if  0 <= Desa < len(ListLokasi[Kecamatan]["desa"]):
                            database = pd.read_csv(lokasiDB + 'Akun.csv')
                            if (NomorHp.isdigit == False):
                                input('Masukkan Nomor Hp!')
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
                                'Role': 'user',
                                'Kecamatan': kecamatan,
                                'Desa': desa
                                }
                            datanew = pd.DataFrame(Newdata, index=[0])
                            datanew.to_csv(lokasiDB + "Akun.csv",mode='a',header=False ,index=False)
                            return ''
                        else:
                            input(f'hanya bisa memasukkan angka [1-{len(Kecamatan)}]')
                    else:
                        input(f'hanya bisa memasukkan angka [1-{len(ListLokasi)}]')
                except ValueError:
                    input('hanya bisa memasukkan angka!')
    else:
        input('password 1 dan 2 tidak sama')