"""from db.get_db import select_show_db"""
from src.service.translate import select_language
from src.service.utilities import check_repo_dir_exist, check_db_created, delete_created_db
from src.repository.make_repo import set_name_project


def main():
    """ #TEXTEO, TODAVIA NO IMPLEMENTAR...
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
    check_repo_dir_exist()
    check_db_created()
    language = select_language()
    set_name_project(language)
    delete_created_db()


if __name__ == '__main__':
    main()
