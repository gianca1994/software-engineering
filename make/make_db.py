from constants import SELECT_DB, NAME_DB, TYPE_DB, DB_SWITCH
from make.make_dirs import make_database_dir
from make.make_files import create_file


def set_db(repo_name):
    try:
        opt = str(input(SELECT_DB))
        if opt == "y" or opt == "Y":
            set_name_db(repo_name)
    except OSError as error:
        print(error)


def set_name_db(repo_name):
    try:
        name_db = str(input(NAME_DB))
        set_type_db(repo_name, name_db)
    except OSError as error:
        print(error)


def set_type_db(repo_name, name_db):
    try:
        type_db = int(input(TYPE_DB))
        if DB_SWITCH.get(type_db, ) is not None:
            type_db = DB_SWITCH.get(type_db, )
            make_db(repo_name, name_db + type_db)
    except OSError as error:
        print(error)


def make_db(repo_name, name_db):
    name_db_py = "database.py"
    make_database_dir(repo_name)
    create_file(repo_name + "/app/main/database", name_db_py)
    create_file(repo_name + "/app/main/data", name_db)
