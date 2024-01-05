import sqlite3
koneksi = sqlite3.connect('DATABASE_FAUNA.DB')

#CREATE_TABLE_FAUNA
koneksi.execute(''' 
              CREATE table FAUNA(
                id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                nama fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrng INT(10),
                thn_ditemukan INT(10)
              )
             ''')
koneksi.close()