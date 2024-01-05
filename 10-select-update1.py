# a table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3
koneksi = sqlite3.connect('DATABASE_FAUNA.DB')

# SELECT ALL FAUNA
kursor = koneksi.cursor()

# Ubah berdasarkan id_fauna
id_fauna = 10
jml_skrng = 2000

# Gunakan Query UPDATE SET
kursor.execute(f"DELETE FROM FAUNA WHERE id_fauna = ?", (id_fauna,))
koneksi.commit()

# Cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: #cek  berdasarkan adanya baris atau tidak
    print(f"Data dengan ID {id_fauna} berhasil Diubah!")
else: 
    print(f"Tidak ada data pegawai dengan ID{id_fauna}!")

# Putuskan koneksi
koneksi.close()