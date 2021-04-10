import os

from git import Repo

from constants import ENTER_PROYECT_NAME, EMPTY_PATH, ERR_SPACE
from operations import create_dir

COMMIT_MESSAGE = 'Initial commit'


def create_repo(user_git, name_git):
    repo_name = make_project()

    repo = Repo.init(repo_name, mkdir=True)
    # ACA AGREGAMOS TODAS LAS CARPETAS Y ARCHIVOS AL REPO
    repo.git.execute("git add *")
    repo.index.commit(COMMIT_MESSAGE)
    repo.git.execute(("git remote add origin https://" + name_git + ".com/" + user_git + "/" + repo_name + ".git"))
    origin = repo.create_remote(repo_name, repo.remotes.origin.url)
    origin.push()
    return repo_name


def make_project():
    try:
        name_repo = str(input(ENTER_PROYECT_NAME))
        while not " " in name_repo:
            return name_repo
        else:
            os.system("cls")
            print(ERR_SPACE)
            make_project()
    except OSError as error:
        print(error)
        make_project()


def set_user_git():


def set_git_type():
# Github o gitlab
