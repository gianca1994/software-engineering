import os
import platform

from src.db.make_tables_db import create_db_tables
from src.service.constants import Database, Map, Repository
from src.service.mapper import mapping


def check_existence_repo_db():
    """
    Function to check if the 'repositories' folder exists in which all
    the repositories that we initialize will be created, if not,
    we create it. It is the first method executed in the main.
    And function to check if the database exists, if it does not exist,
    we create it.
    """
    if not os.path.isdir(Repository.REPOSITORY_PATH):
        os.mkdir(Repository.REPOSITORY_PATH)

    if not os.path.isfile(Database.DB_PATH + Database.DB_FILE):
        create_db_tables()


def delete_created_db():
    """
    We check if the database exists, if it exists, we delete it.
    This method is used at the end of the main.
    """
    if os.path.isfile(Database.DB_PATH + Database.DB_FILE):
        os.remove(Database.DB_PATH + Database.DB_FILE)


def clear_os():
    """
    Function to erase the console, mapping was used to make it functional
    both in windows, linux and mac, with the method 'platform.system ()' you
    we tell the mapping function if it should bring 'clear' or 'cls'.
    """
    os.system(mapping(Map.OS_CLEAR_MAP, platform.system()))
