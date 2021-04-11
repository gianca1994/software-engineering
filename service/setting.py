import os
import platform

from constants.constants_db import DB_FILE
from db.make_tables_db import create_db_tables


def check_db_created():
    if not os.path.isfile(DB_FILE):
        create_db_tables()


def delete_created_db():
    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)


def clear_os():
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')
