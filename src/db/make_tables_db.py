import sqlite3
from src.db.connect_db import connect
from src.service.constants import Database, Map
from src.service.mapper import mapping


def create_db_tables():
    conn = connect()

    try:
        for i in Database.DICT_MAKE_TABLES:
            conn.execute(i)

        insert_data(1, Database.DICT_SECOND_DIRS)
        insert_data(2, Database.DICT_FILES)
        insert_data(3, Database.DICT_REQ)
        insert_data(4, Database.DICT_INSTALL)
        insert_data(5, Database.DICT_BOOT)
        insert_data(6, Database.DICT_PYVENV)
        insert_data(7, Database.DICT_DB)

    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def insert_data(number, dictionary):
    for i in dictionary:
        set_data_db(number, i)


def set_data_db(opt, content_inset):
    table_insert = mapping(Map.DB_MAP, opt)
    conn = connect()
    conn.execute(table_insert, (content_inset,))
    conn.commit()
    conn.close()
