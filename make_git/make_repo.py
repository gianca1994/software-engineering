import os

from git import Repo

from make.make_db import set_db
from make.make_dirs import make_seconds_dirs
from constants.constants_globals import COMMIT_MESSAGE, PUSH_OK, EXIST_REPO, GIT_PUSH, CHECK_YES_NO, USER_GIT, \
    ERR_USER_NOT_STR, GIT_OPTION, GIT_SWITCH, ERR_OPTION, PROJECT_NAME, ERR_SPACE
from make.make_files import make_files
from service.setting import clear_os

from service.translate import txt_print


def make_repository(repo_name, language):
    if not os.path.isdir(repo_name):
        repo = Repo.init(repo_name, mkdir=True)
        make_seconds_dirs(repo_name)
        make_files(repo_name)
        set_db(repo_name, language)

        if set_confirm_push(language):
            user_git = set_user_git(language)
            type_git = set_git_type(language)
            repo.git.add(all=True)
            repo.index.commit(COMMIT_MESSAGE)
            repo.git.execute(
                "git remote add origin https://" + type_git + ".com/" + user_git + "/" + repo_name + ".git")
            origin = repo.create_remote(repo_name, repo.remotes.origin.url)
            origin.push()
            print('\n')
            print(txt_print(language, PUSH_OK,
                            True) + f' User: {user_git} | Link: https://{type_git}.com/{user_git}/{repo_name}')
        return repo_name
    else:
        txt_print(language, EXIST_REPO, False)
        set_name_project(language)


def set_name_project(language):
    name_repo = str(input(txt_print(language, PROJECT_NAME, True)))

    while not " " in name_repo:
        make_repository(name_repo, language)
        break
    else:
        clear_os()
        txt_print(language, ERR_SPACE, False)
        set_name_project(language)


def set_confirm_push(language):
    try:
        confirm = str(input(txt_print(language, GIT_PUSH, True) + CHECK_YES_NO))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        txt_print(language, error, False)


def set_user_git(language):
    try:
        user_git = input(txt_print(language, USER_GIT, True))
        if str(user_git):
            return user_git
        else:
            clear_os()
            txt_print(language, ERR_USER_NOT_STR, True)
    except OSError as error:
        txt_print(language, error, False)


def set_git_type(language):
    opt = int(input(txt_print(language, GIT_OPTION, True)))
    try:
        if GIT_SWITCH.get(opt, ) is not None:
            return GIT_SWITCH.get(opt, )
        else:
            txt_print(language, ERR_OPTION, False)
    except OSError as error:
        txt_print(language, error, False)
