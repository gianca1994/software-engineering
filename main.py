from service.translate import select_lenguage
from service.setting import check_db_created, delete_created_db
from make_git.make_repo import set_name_project


def main():
    check_db_created()
    language = select_lenguage()
    set_name_project(language)
    delete_created_db()


if __name__ == '__main__':
    main()
