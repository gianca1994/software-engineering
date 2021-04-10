from constants import SELECT_DB, NAME_DB, TYPE_DB


def set_db():
    try:
        opt = input(SELECT_DB)
        if opt == "y" or opt == "Y":
            return True
        else:
            return False
    except OSError as error:
        print(error)


def set_name_db():
    try:
        input(NAME_DB)    
        if set_db():
            return True
        else:
            return False
    except OSError as error:
        print(error)


def set_type_db():
    try:
        if set_name_db():
            return int(input(TYPE_DB))
        else:
            return False
    except OSError as error:
        print(error)

