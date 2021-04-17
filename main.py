"""from db.get_db import select_show_db"""
from src.repository.make_repo import set_name_project
from src.service.constants import Config
from src.service.translate import select_language
from src.service.utilities import check_existence_repo_db, delete_created_db


def main():
    """ #TESTEO, TODAVIA NO IMPLEMENTAR...
        opt = int(input("1. Create project | 2. View/Edit DataBase: "))
        if opt == 1:
            set_name_project(language)
            delete_created_db()
        elif opt == 2:
            opt = int(input(""
    Enter the number of the table you want to see:
    1. View the directories to be created
    2. View the files to be created
    3. See the requirements that 'requisiments.txt' will carry
    ""))
            if 3 >= opt > 0:
                select_show_db(opt)
    """

    check_existence_repo_db()
    Config.LANGUAGE = select_language()
    set_name_project()
    delete_created_db()


if __name__ == '__main__':
    main()
