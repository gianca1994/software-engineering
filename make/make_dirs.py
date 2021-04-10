from db.get_db import get_dir_db

import os


def make_seconds_dirs(project_name):
    create_dir(project_name, "/app")
    create_dir(project_name, "/app/main")
    for dir in get_dir_db():
        create_dir(project_name, dir)


def create_dir(route_dir, name_dir):
    try:
        if len(route_dir) > 0:
            os.mkdir(route_dir + name_dir)
        else:
            os.mkdir(name_dir)
    except OSError as error:
        print(error)
