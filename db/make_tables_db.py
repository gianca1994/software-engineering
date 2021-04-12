from db.connect_db import connect
from constants.constants_db import *
import sqlite3


def create_db_tables():
    conn = connect()

    try:
        for i in DICT_MAKE_TABLES:
            conn.execute(i)

        insert_data(1, DICT_SECOND_DIRS)
        insert_data(2, DICT_FILES)
        insert_data(3, DICT_REQ)
        insert_data(4, DICT_INSTALL)
        insert_data(5, DICT_BOOT)
        insert_data(6, DICT_PYVENV)
        insert_data(7, DICT_DB)

    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def set_data_db(opt, name2):
    name1 = map_set_db(opt)
    conn = connect()
    conn.execute(name1, (name2,))
    conn.commit()
    conn.close()


def insert_data(number, dictionary):
    for i in dictionary:
        set_data_db(number, i)


def map_set_db(opt):
    return MAP_DB.get(opt, "nothing")
