import sqlite3
from db.dictionaries import DB_FILE

def connect():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
    except Error as e:
        print(e)
    return conn
