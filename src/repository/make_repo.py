import os

from git import Repo

from src.service.constants import Messages, Map
from src.service.mapper import mapping
from src.service.translate import txt_print
from src.service.utilities import clear_os
from src.work.make_db import set_db
from src.work.make_dirs import make_seconds_dirs
from src.work.make_files import make_files


def make_repository(repo_name, language):
    """
    Method used to create the repository, receives as parameters the name of the repository
    and the language used.

    With the "if not os.path.isdir (path + repo_name)", we verify if the repository with the
    name we want to use exists, if it exists, nothing is executed and it asks for the name
    again, if not, the repository is initialized, the secondary folders "make_seconds_dirs"
    are created, the files "make_files" are created and the function "set_db" <- is called,
    which will ask us whether or not we want to add a database.

    Then we go to "if set_confirm_push (language)", with which we ask the user if they want
    to upload the repository to the cloud, if the answer is yes, we ask the user and the type
    of repository to be used in our case "github or gitlab". We add all the initialized repository
    to the stage, commit it, link the initialized repository with the existing one in the cloud
    and finally push it to the cloud.
    """

    path = Messages.REPOSITORY_PATH

    if not os.path.isdir(path + repo_name):
        repo = Repo.init(path + repo_name, mkdir=True)
        make_seconds_dirs(path + repo_name)
        make_files(path + repo_name)
        set_db(path + repo_name, language)

        if set_confirm_push(language):
            user_git = set_user_git(language)
            type_git = set_git_type(language)
            repo.git.add(all=True)
            repo.index.commit(Messages.COMMIT_MESSAGE)
            repo.git.execute(
                "git remote add origin https://" + type_git + ".com/" + user_git + "/" + repo_name + ".git")
            origin = repo.create_remote(path + repo_name, repo.remotes.origin.url)
            origin.push()
            print('\n')
            print(txt_print(language, Messages.PUSH_OK,
                            True) + f' User: {user_git} | Link: https://{type_git}.com/{user_git}/{repo_name}')
        return repo_name
    else:
        txt_print(language, Messages.EXIST_REPO, False)
        set_name_project(language)


def set_name_project(language):
    """
    This method will ask for the repository name, then a while condition is raised
    to verify that the repository does not contain spaces,if it does not contain
    spaces the repository name will be saved, if it contains spaces an error message
    will be printed and the repository name without spaces will be asked again.
    """
    name_repo = str(input(txt_print(language, Messages.PROJECT_NAME, True)))

    while not " " in name_repo:
        make_repository(name_repo, language)
        break
    else:
        clear_os()
        txt_print(language, Messages.ERR_SPACE, False)
        set_name_project(language)


def set_confirm_push(language):
    """
    This method will ask the user if he/she wants to upload the repository to the cloud.
    """
    try:
        confirm = str(input(txt_print(language, Messages.GIT_PUSH, True) + Messages.CHECK_YES_NO))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        txt_print(language, error, False)


def set_user_git(language):
    """
    This method will ask for the user name, in case it is correct it will return
    the user name and in case it is not correct it will print an error message.
    """
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
    """
    This method will ask the user to enter the desired cloud server option, once
    the option is entered it will be verified with a condition which will use the
    mapping function to see if the option entered is correct, if not an error will
    be printed saying that the option entered is not valid.
    """
    opt = int(input(txt_print(language, Messages.GIT_OPTION, True)))
    try:
        if mapping(Map.GIT_MAP, opt) is not None:
            return mapping(Map.GIT_MAP, opt)
        else:
            txt_print(language, Messages.ERR_OPTION, False)
    except OSError as error:
        txt_print(language, error, False)
