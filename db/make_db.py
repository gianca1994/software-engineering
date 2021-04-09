from db.set_db import *
from db.dictionaries import *
import sqlite3

def create_tables():
    connection = connect()

    try:
        for i in DICT_MAKE_TABLES:
            connection.execute(i)

        for i in DICT_REQ:
            set_data_db(1, i)

        for i in DICT_DIRS:
            set_data_db(2, i)

        for i in DICT_INSTALL:
            set_data_db(3, i)

        for i in DICT_BOOT:
            set_data_db(4, i)

        for i in DICT_PYVENV:
            set_data_db(5, i)

        print("Se creo la tabla requeriments")
    except sqlite3.OperationalError:
        print("La tabla requeriments ya existe...")
    connection.close()
