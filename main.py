from db.make_db import create_tables
from make.make_repo import create_repo


def main():
    create_tables()
    create_repo()


if __name__ == '__main__':
    main()
