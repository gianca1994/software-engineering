from db.make_db import create_tables
from make_git_repo.make_repo import make_repository
from make_git_repo.setters_git import *
from translate import select_lenguage


def main():
    language = select_lenguage()

    #create_tables()
    name_project = set_name_project(language)
    make_repository(name_project, language)


if __name__ == '__main__':
    main()
