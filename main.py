from make_git_repo.make_repo import make_repository
from make_git_repo.setters_git import *
from service.translate import select_lenguage
from service.setting import check_db_created

def main():
    check_db_created()

    language = select_lenguage()

    name_project = set_name_project(language)
    make_repository(name_project, language)

if __name__ == '__main__':
    main()
