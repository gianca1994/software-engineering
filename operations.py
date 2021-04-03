import os
import errno


def create_dir(route_dir, name_dir):
    try:
        if len(route_dir) > 0:
            create_seconds_dir(route_dir, name_dir)
        else:
            os.mkdir(name_dir)

    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

def create_seconds_dir(main_route, name_dir):
    os.mkdir(main_route + "/" + name_dir)

def create_file(name_file, text, is_dict):
    file = open(name_file, "w")
    
    if not is_dict:
        create_text_files(file, text)
        file.close()
    else:
        for i in text:
            create_text_files(file, i)    
        file.close()

def create_text_files(file_name, text):
    file_name.write(text + "\n")
