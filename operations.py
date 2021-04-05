import os
import errno


def create_dir(route_dir, name_dir):
    try:
        if len(route_dir) > 0:
            os.mkdir(route_dir + "/" + name_dir)
        else:
            os.mkdir(name_dir)

    except OSError as error:
        if error.errno != errno.EEXIST:
            raise


def create_file(name_file, text, is_dict):
    try:
        file = open(name_file, "w")

        if not is_dict:
            create_text_files(file, text)
            file.close()
        else:
            for i in text:
                create_text_files(file, i)
            file.close()
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise


def create_text_files(file_name, text):
    try:
        file_name.write(text + "\n")
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
