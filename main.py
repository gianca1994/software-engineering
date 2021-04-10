from db.make_db import create_tables
from make_git_repo.make_repo import make_repository
from make_git_repo.setters_git import *


def main():
    create_tables()
    make_repository(set_name_project())


if __name__ == '__main__':
    main()
