import sqlite3
koneksi = sqlite3.connect('DATABASE_FAUNA.DB')

#insert data ke tabel
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Harimau Jawa', 'Mamalia', 'Jawa', '40', '2019')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Kuskus Beruang', 'Mamalia', 'Sulawesi', '30', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Beruang Madu', 'Mamalia', 'Sumatera', '1000', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Pesut Mahakam', 'Mamalia', 'Kalimantan', '100', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Burung Maleo', 'Burung', 'Sulawesi', '7000', '2023')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Macan Dahan', 'Mamalia', 'Sumatera', '400', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Kancil', 'Mamalia', 'Jawa', '60', '2022')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Elang Jawa', 'Mamalia', 'Jawa', '200', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama, jenis, asal,  jml_skrng, thn_ditemukan)
                VALUES('Katak Boneo', 'Mamalia', 'Kalimantan', '2000', '2023')
                ''')
koneksi.commit()
koneksi.close()