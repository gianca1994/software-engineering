import os
import sqlite3

from src.service.constants import Database

def connect():
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(Database.DB_PATH, Database.DB_FILE))
    except OSError as e:
        print(e)
    return conn
