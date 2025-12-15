import sqlite3 as sq
import os 
from os import system
system("cls")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "library.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

def get_db_connection():
    conn = sq.connect(DB_PATH)
    conn.row_factory = sq.Row
    
    return conn

def initialize_database():
    if not os.path.exists(SCHEMA_PATH):
        print(f"HATA: '{SCHEMA_PATH}' bulunamadı!")
        return

    conn = get_db_connection()
    try:
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            schema_script = f.read()
            conn.executescript(schema_script)
            print(f"Veritabanı başarıyla başlatıldı: {DB_PATH}")
    except Exception as e:
        print(f"Veritabanı oluşturulurken hata: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()