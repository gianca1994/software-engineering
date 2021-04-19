from src.repository.make_repo import set_name_project
from src.service.translate import select_language
from src.service.utilities import check_existence_repo_db, delete_created_db


def main():
    check_existence_repo_db()
    select_language()
    set_name_project()


if __name__ == '__main__':
    main()
