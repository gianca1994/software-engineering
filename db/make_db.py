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
        insert_data(6, DICT_FILES)

        print("Se creo la Base de datos con todas las tablas!!")
    except sqlite3.OperationalError:
        print("La Base de datos ya existe...")
    connection.close()


def set_data_db(opt, name2):
    name1 = map_set_db(opt)
    connection = connect()
    connection.execute(name1, (name2,))
    connection.commit()
    connection.close()


def insert_data(number, dictionary):
    for i in dictionary:
        set_data_db(number, i)


switch = {
    1: "insert into requeriments(name) values (?)",
    2: "insert into dirs(name) values (?)",
    3: "insert into installsh(name) values (?)",
    4: "insert into bootsh(name) values (?)",
    5: "insert into pyvenv(name) values (?)",
    6: "insert into files(name) values (?)",
}


def map_set_db(opt):
    return switch.get(opt, "nothing")
