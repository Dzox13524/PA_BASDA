import pandas as pd

def login():
    email = input('Masukkan Email: ')
    password = input('Masukkan Password: ')
    database = pd.read_csv('database/Akun.csv')
    print(database)
    if email in database['Email'].values:
        data = database[database['Email'] == email]
        if data['Password'].values[0] == password:
            role = data['Role'].values[0]
        elif data['Password'].values[0] != password:
            input('Password salah!')
            return None, None, None, None, None
    else: 
        input('Email tidak ada!. Harap registrasi terlebih dahulu!')
        return None, None, None, None, None
    return data['Email'].values[0], data['Name'].values[0], data['Kecamatan'].values[0],data['Desa'].values[0], role