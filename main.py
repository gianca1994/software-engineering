from service.translate import select_lenguage
from service.setting import check_db_created
from make_git.make_repo import set_name_project


def main():
    check_db_created()
    language = select_lenguage()
    set_name_project(language)


if __name__ == '__main__':
    main()
