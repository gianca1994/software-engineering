from constants import SELECT_DB, NAME_DB, TYPE_DB, DB_SWITCH
from make.make_dirs import make_database_dir
from make.make_files import create_file
from translate import txt_print


def set_db(repo_name, language):
    try:
        opt = str(input(txt_print(language, SELECT_DB)))
        if opt == "y" or opt == "Y":
            set_name_db(repo_name, language)
    except OSError as error:
        print(txt_print(language, error))


def set_name_db(repo_name, language):
    try:
        name_db = str(input(txt_print(language, NAME_DB)))
        set_type_db(repo_name, name_db, language)
    except OSError as error:
        print(txt_print(language, error))


def set_type_db(repo_name, name_db, language):
    try:
        type_db = int(input(txt_print(language, TYPE_DB)))
        if DB_SWITCH.get(type_db, ) is not None:
            type_db = DB_SWITCH.get(type_db, )
            make_db(repo_name, name_db + type_db)
    except OSError as error:
        print(txt_print(language, error))


def make_db(repo_name, name_db):
    make_database_dir(repo_name)
    create_file(repo_name + "/app/main/data", name_db)
