import os

from src.db.get_db import get_data_db


"""def make_sec_dirs(project_name, map):
    print("HOLA")"""
    
"""
This method will be given the name of the project and will be in charge of creating the "secondary" directories. 
A for of "dir" of the get_data_db method will be carried out, passing it as an argument (1) where it will go through
the for creating the directories, receiving as parameters the name of the project and dir.
"""
def make_seconds_dirs(project_name):
    create_dir(project_name, "/app")
    create_dir(project_name, "/app/main")
    for dir in get_data_db(1):
        create_dir(project_name, dir)

"""
This method receives as argument the name of the project, a for "db" will be carried out in the function get_data_db 
passing it as argument "7", it will go through this for creating the directories of the database.
"""
def make_database_dir(project_name):
    for db in get_data_db(7):
        create_dir(project_name, db)

"""
This method will receive as argument the directory path and the directory name.
An "if" condition will be raised to see if the directory path contains a number of characters greater than zero. 
If this is the case, the directory will be created in the directory path and the directory name will be concatenated.
If the directory path contains zero characters the directory will be created, but it will only receive the directory name as parameter.
"""
def create_dir(route_dir, name_dir):
    try:
        if len(route_dir) > 0:
            os.mkdir(route_dir + name_dir)
        else:
            os.mkdir(name_dir)
    except OSError as error:
        print(error)
