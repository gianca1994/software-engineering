import os

from db.make_db import create_db_tables


def check_db_created():
    if not os.path.isfile('db/DataBase.db'):
        create_db_tables()
