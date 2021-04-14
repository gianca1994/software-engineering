import sqlite3

from src.db.connect_db import connect
from src.service.constants import Database, Map
from src.service.mapper import mapping


def create_db_tables():
    """
    We start the connection with the database, in the for we go through the dictionary
    creating all the tables one by one. Then with the 'insert_data', we pass the
    number of the mapping to be carried out and the dictionary that contains the list
    of the directories, files, requirements, etc.
    """
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


def insert_data(opt, dictionary):
    """
    A for to go through the dictionary and the 'opt' passed as a
    direct parameter to the next function.
    """
    for i in dictionary:
        set_data_db(opt, i)


def set_data_db(opt, content_inset):
    """
    We do mapping with 'INSERT_DB_MAP' and the section we are looking for goes through it
    parameter 'opt', then we insert in the table already created the content of the
    second parameter 'content_inset', we save and close the connection.
    """
    table_insert = mapping(Map.INSERT_DB_MAP, opt)
    conn = connect()
    conn.execute(table_insert, (content_inset,))
    conn.commit()
    conn.close()
