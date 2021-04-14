from src.service.constants import Messages, Map
from src.service.mapper import mapping
from src.work.make_dirs import make_database_dir
from src.work.make_files import create_file
from src.service.translate import txt_print

"""
This method will ask the user if he wants to create a database, it will pass as parameters the name 
of the repository and the language used, if the option entered is "yes" the function set_name_db will
be invoked, which will pass the parameters previously named.
"""
def set_db(repo_name, language):
    try:
        opt = str(input((txt_print(language, Messages.SELECT_DB, True) + Messages.CHECK_YES_NO)))
        if opt == "y" or opt == "Y":
            set_name_db(repo_name, language)
    except OSError as error:
        txt_print(language, error, False)

"""
This method will receive as parameters the repository name and the language, will ask the user the name 
he wants to give to the database and will invoke the function set_type_db passing it the following 
parameters -->(repository name, the database name and the language).
"""
def set_name_db(repo_name, language):
    try:
        name_db = str(input(txt_print(language, Messages.NAME_DB, True)))
        set_type_db(repo_name, name_db, language)
    except OSError as error:
        txt_print(language, error, False)

"""
This method will receive as parameters the repository name, database name and language.
The user will be asked what type of database he/she wants to use to verify this option, 
a condition will be set and the mapping function will be invoked to verify that the set 
option is among the options. If so, the function make_db will be invoked, which will receive
as parameters the repository name, database name and the type of database will be concatenated to the latter).
"""
def set_type_db(repo_name, name_db, language):
    try:
        type_db = int(input(txt_print(language, Messages.TYPE_DB, True)))
        if mapping(Map.DB_MAP, type_db) is not None:
            type_db = mapping(Map.DB_MAP, type_db)
            make_db(repo_name, name_db + type_db)
    except OSError as error:
        txt_print(language, error, False)

"""
This method receives as parameters the repository name and the database name.
The function that will create the database directory is invoked, which will receive the repository name as an argument,
and then the function that will create the files in the configured path with their respective database is invoked.
"""
def make_db(repo_name, name_db):
    make_database_dir(repo_name)
    create_file(repo_name + "/app/main/data", name_db)
