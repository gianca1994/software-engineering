import os
import platform

from src.service.constants import Database, Map, Messages
from src.db.make_tables_db import create_db_tables
from src.service.mapper import mapping


def check_repo_dir_exist():
    if not os.path.isdir(Messages.REPOSITORY_PATH):
        os.mkdir(Messages.REPOSITORY_PATH)


def check_db_created():
    if not os.path.isfile(Database.DB_PATH + Database.DB_FILE):
        create_db_tables()


def delete_created_db():
    if os.path.isfile(Database.DB_PATH + Database.DB_FILE):
        os.remove(Database.DB_PATH + Database.DB_FILE)


def clear_os():
    os.system(mapping(Map.PLATAFORM_MAP, platform.system()))
