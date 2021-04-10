import os


def create_dir(route_dir, name_dir):
    try:
        if len(route_dir) > 0:
            os.mkdir(route_dir + "/" + name_dir)
        else:
            os.mkdir(name_dir)
    except OSError as error:
        print(error)


def create_file(name_file, text_file):
    try:
        file = open(name_file, "w")
        for i in text_file:
            create_text_files(file, i)
        file.close()
    except OSError as error:
        print(error)


def create_text_files(file_name, text):
    try:
        file_name.write(text + "\n")
    except OSError as error:
        print(error)
