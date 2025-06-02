import os 
import importlib

path = "./fitur/Admin/Pengelolaan_Akun_Pengguna"
modul_base = "Fitur.Admin.Pengelolaan_Akun_Pengguna"

# Loop melalui semua file Python di folder tersebut
for i in os.listdir(path):
    if i.endswith(".py") and i != "__init__.py":
        nama = i.replace(".py", "")
        modul_nama = f"{modul_base}.{nama}"

        try:
            # Import modul secara dinamis
            mod = importlib.import_module(modul_nama)
            print(f"✅ Berhasil import: {modul_nama}")

            # Jika ada fungsi 'jalan', panggil
            if hasattr(mod, "jalan"):
                print(f"🔁 Memanggil fungsi 'jalan' dari {modul_nama}")
                getattr(mod, "jalan")()

            # Atau fungsi 'main'
            elif hasattr(mod, "main"):
                print(f"🔁 Memanggil fungsi 'main' dari {modul_nama}")
                getattr(mod, "main")()

            else:
                print(f"⚠️  Tidak ada fungsi 'jalan' atau 'main' di {modul_nama}")

        except Exception as e:
            print(f"❌ Gagal import {modul_nama}: {e}")
