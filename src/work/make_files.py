from src.db.get_db import get_data_db


def make_files(project_name):
    for file in get_data_db(2):
        create_file(project_name, file, )


def create_file(name_dir, name_file):
    try:
        route = (name_dir + "/" + name_file)
        file = open(route, "w")
        file.close()
    except OSError as error:
        print(error)
