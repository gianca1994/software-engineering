from db.make_db import create_tables
from db.get_db import select_show_db, get_dir_db
from make_repo import create_repo
from work import *

def main():
    create_tables()
    create_project_dir(create_repo())


if __name__ == '__main__':
    main()
