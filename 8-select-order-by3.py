import sqlite3
koneksi = sqlite3.connect('DATABASE_FAUNA.DB')

# SELECT ALL FAUNA 
kursor = koneksi.cursor()

# Mengambi semua data dalam tabel dan tampilkan
kursor.execute("SELECT * FROM FAUNA ORDER BY thn_ditemukan ASC")

# Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

# Membuat format table dengan method 
print("Tabel Fauna")
print("="*120)
print("{:<10} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("="*80)

# Tampilkan data sesuai format tabel dg perulangan
for baris in baris_tabel:
    print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()