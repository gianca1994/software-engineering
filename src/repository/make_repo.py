import os

from git import Repo
from src.service.mapper import mapping

from src.work.make_db import set_db
from src.work.make_dirs import make_seconds_dirs
from src.service.constants import Messages, Map

from src.work.make_files import make_files
from src.service.utilities import clear_os

from src.service.translate import txt_print


def make_repository(repo_name, language):
    repo_path = "repositories/"
    if not os.path.isdir(repo_path + repo_name):
        repo = Repo.init(repo_path + repo_name, mkdir=True)
        make_seconds_dirs(repo_path + repo_name)
        make_files(repo_path + repo_name)
        set_db(repo_path + repo_name, language)

        if set_confirm_push(language):
            user_git = set_user_git(language)
            type_git = set_git_type(language)
            repo.git.add(all=True)
            repo.index.commit(Messages.COMMIT_MESSAGE)
            repo.git.execute(
                "git remote add origin https://" + type_git + ".com/" + user_git + "/" + repo_name + ".git")
            origin = repo.create_remote(repo_path + repo_name, repo.remotes.origin.url)
            origin.push()
            print('\n')
            print(txt_print(language, Messages.PUSH_OK,
                            True) + f' User: {user_git} | Link: https://{type_git}.com/{user_git}/{repo_name}')
        return repo_name
    else:
        txt_print(language, Messages.EXIST_REPO, False)
        set_name_project(language)


def set_name_project(language):
    name_repo = str(input(txt_print(language, Messages.PROJECT_NAME, True)))

    while not " " in name_repo:
        make_repository(name_repo, language)
        break
    else:
        clear_os()
        txt_print(language, Messages.ERR_SPACE, False)
        set_name_project(language)


def set_confirm_push(language):
    try:
        confirm = str(input(txt_print(language, Messages.GIT_PUSH, True) + Messages.CHECK_YES_NO))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        txt_print(language, error, False)


def set_user_git(language):
    try:
        user_git = input(txt_print(language, Messages.USER_GIT, True))
        if str(user_git):
            return user_git
        else:
            clear_os()
            txt_print(language, Messages.ERR_USER_NOT_STR, True)
    except OSError as error:
        txt_print(language, error, False)


def set_git_type(language):
    opt = int(input(txt_print(language, Messages.GIT_OPTION, True)))
    try:
        if mapping(Map.GIT_SWITCH, opt) is not None:
            return mapping(Map.GIT_SWITCH, opt)
        else:
            txt_print(language, Messages.ERR_OPTION, False)
    except OSError as error:
        txt_print(language, error, False)
