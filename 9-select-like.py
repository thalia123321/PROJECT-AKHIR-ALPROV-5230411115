# QUERY LIKE
import sqlite3
koneksi = sqlite3.connect('DATABASE_FAUNA.DB')
kursor = koneksi.cursor()

# Menjalankan Query SELECT dengan LIKE
# misalkan kita ingin mencari nama dengan awalan huruf B 
nama = 'B%'
kursor.execute(f"SELECT * FROM FAUNA WHERE nama LIKE ?" ,(nama,))
baris_table = kursor.fetchall()

# Membuat format table dengan method 
print("Tabel Fauna")
print("="*120)
print("{:<10} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("="*80)

# Tampilkan data sesuai format tabel dg perulangan
for baris in baris_table:
    print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()