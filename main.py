from db.get_db import select_show_db
from service.translate import select_lenguage
from service.setting import check_db_created, delete_created_db
from make_git.make_repo import set_name_project


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

    check_db_created()
    language = select_lenguage()
    set_name_project(language)
    delete_created_db()


if __name__ == '__main__':
    main()
