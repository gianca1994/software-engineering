from db.set_db import insert_data
from db.connect_db import connect
from db.dictionaries import *
import sqlite3


def create_tables():
    connection = connect()

    try:
        for i in DICT_MAKE_TABLES:
            connection.execute(i)

        insert_data(1, DICT_REQ)
        insert_data(2, DICT_DIRS)
        insert_data(3, DICT_INSTALL)
        insert_data(4, DICT_BOOT)
        insert_data(5, DICT_PYVENV)

        print("Se creo la Base de datos con todas las tablas!!")
    except sqlite3.OperationalError:
        print("La Base de datos ya existe...")
    connection.close()
