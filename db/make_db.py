from db.connect_db import connect
from db.set_db import *
from db.dictionaries import *
import sqlite3

def create_tables():
    connection = connect()

    try:
        connection.execute("create table requeriments (\n"
                           "        id integer primary key autoincrement,\n"
                           "        name text)")

        connection.execute("create table dirs (\n"
                           "        id integer primary key autoincrement,\n"
                           "        name text)")
        
        connection.execute("create table installsh (\n"
                           "        id integer primary key autoincrement,\n"
                           "        name text)")

        connection.execute("create table bootsh (\n"
                           "        id integer primary key autoincrement,\n"
                           "        name text)")
        
        connection.execute("create table pyvenv (\n"
                           "        id integer primary key autoincrement,\n"
                           "        name text)")

        for i in DICT_REQ:
            set_req_db(i)

        for i in DICT_DIRS:
            set_dir_db(i)
        
        for i in DICT_INSTALL:
            set_installsh_db(i)

        for i in DICT_BOOT:
            set_bootsh_db(i)
        
        for i in DICT_PYVENV:
            set_pyvenv_db(i)

        print("Se creo la tabla requeriments")
    except sqlite3.OperationalError:
        print("La tabla requeriments ya existe...")
    connection.close()
