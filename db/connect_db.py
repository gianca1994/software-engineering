import sqlite3

from constants.constants_db import DB_FILE


def connect():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
    except OSError as e:
        print(e)
    return conn
