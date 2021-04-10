import os

from git import Repo

from constants import COMMIT_MESSAGE, ENTER_PROYECT_NAME, EMPTY_PATH, ERR_SPACE, USER_GIT, ERR_USER_NOT_STR, ERR_OPTION, ENTER_NAME_GIT_OPTION
from operations import create_dir


def create_repo():
    repo_name = make_project()
    user_git = set_user_git()
    name_git = set_git_type()

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
    try:
        user_git = input(USER_GIT)
        while str in user_git:
            return user_git
        else:
            os.system("cls")
            print(ERR_USER_NOT_STR)
            set_user_git()
    except OSError as error:
        print(error)
        set_user_git()


GIT_SWITCH ={
    1: "gitlab",
    2: "github"
}


def set_git_type():
    opt = int(input(ENTER_NAME_GIT_OPTION))
    try:
        if GIT_SWITCH.get(opt,) is not None:
            return GIT_SWITCH.get(opt,)
        else:
            print(ERR_OPTION)
            set_git_type()        
    except OSError as error:
        print(error)
        set_git_type()

