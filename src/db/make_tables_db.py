import sqlite3

from src.db.connect_db import connect
from src.service.constants import Database, Map
from src.service.mapper import mapping


def create_db_tables():
    """
    We start the connection with the database, in the for we go through the dictionary
    creating all the tables one by one. Then with the 'set_data_db', we pass the
    number of the mapping to be carried out and the dictionary that contains the list
    of the directories, files, requirements, etc.
    """
    conn = connect()

    try:
        for i in Database.DICT_MAKE_TABLES:
            conn.execute(i)

        for key, values in Database.DICT_CONTENT_TABLES.items():
            set_data_db(key, values)

    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def set_data_db(key, values):
    """
    We do mapping with 'INSERT_DB_MAP' and the section we are looking for goes through it
    parameter 'opt', then we insert in the table already created the content of the
    second parameter 'content_inset', we save and close the connection.
    """
    table_insert = mapping(Map.INSERT_DB_MAP, key)
    conn = connect()
    for value in values:
        conn.execute(table_insert, (value,))
    conn.commit()
    conn.close()
