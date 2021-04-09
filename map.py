import os
from operations import create_dir
from constants import EMPTY_PATH, ENTER_PROYECT_NAME, ERR_SPACE


def make_project():
    try:
        name_proyect = str(input(ENTER_PROYECT_NAME))
        while not " " in name_proyect:
            create_dir(EMPTY_PATH, name_proyect)
            break
        else:
            os.system("cls")
            print(ERR_SPACE)
            make_project()
    except OSError as error:
        print(error)
        make_project()


switch = {
    1: make_project()
}


def map_opt(argument):
    return switch.get(argument, "nothing")
