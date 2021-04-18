from src.repository.make_repo import set_name_project
from src.service.constants import Config
from src.service.translate import select_language
from src.service.utilities import check_existence_repo_db, delete_created_db


def main():
    check_existence_repo_db()
    Config.LANGUAGE = select_language()
    set_name_project()
    delete_created_db()


if __name__ == '__main__':
    main()
