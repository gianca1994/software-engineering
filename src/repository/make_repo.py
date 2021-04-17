import os

from git import Repo

from src.service.constants import Messages, Map, Repository
from src.service.mapper import mapping
from src.service.translate import translate
from src.service.utilities import clear_os
from src.work.make_db import set_db
from src.work.make_dirs import make_seconds_dirs
from src.work.make_files import make_files
from src.work.make_venv import make_venv


def make_repository(repo_name):
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
    try:
        path = Repository.REPOSITORY_PATH
        repository = path + repo_name

        if not os.path.isdir(repository):
            repo = init_repository(repository)

            if set_confirm_push():
                user_git, type_git = set_user_git(), set_git_type()

                repo.git.add(all=True)
                repo.index.commit(Messages.COMMIT_MESSAGE)

                repo.git.execute(
                    "git remote add origin https://" + type_git + ".com/"
                    + user_git + "/" + repo_name + ".git")

                origin = repo.create_remote(repository, repo.remotes.origin.url)
                origin.push()
                print("\n")
                print(translate(Messages.PUSH_OK) + f' User: {user_git} | '
                                                    f'Link: https://{type_git}.com/{user_git}/{repo_name}')
        else:
            print(translate(Messages.EXIST_REPO))
            set_name_project()
    except OSError as error:
        print(translate(error))


def init_repository(repository):
    try:
        repo = Repo.init(repository, mkdir=True)
        make_seconds_dirs(repository)
        make_files(repository)
        set_db(repository)
        set_include_venv(repository)
        return repo
    except OSError as error:
        print(translate(error))


def set_name_project():
    """
    This method will ask for the repository name, then a while condition is raised
    to verify that the repository does not contain spaces,if it does not contain
    spaces the repository name will be saved, if it contains spaces an error message
    will be printed and the repository name without spaces will be asked again.
    """
    try:
        name_repo = str(input(translate(Messages.PROJECT_NAME)))

        while not " " in name_repo:
            make_repository(name_repo, )
            break
        else:
            clear_os()
            print(translate(Messages.ERR_SPACE))
            set_name_project()
    except OSError as error:
        print(translate(error))


def set_confirm_push():
    """
    This method will ask the user if he/she wants to upload the repository to the cloud.
    """
    try:
        confirm = str(input(translate(Messages.GIT_PUSH) + Messages.CHECK_YES_NO))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        print(translate(error))


def set_user_git():
    """
    This method will ask for the user name, in case it is correct it will return
    the user name and in case it is not correct it will print an error message.
    """
    try:
        user_git = input(translate(Messages.USER_GIT))
        if str(user_git):
            return user_git
        else:
            clear_os()
            print(translate(Messages.ERR_USER_NOT_STR))
    except OSError as error:
        print(translate(error))


def set_git_type():
    """
    This method will ask the user to enter the desired cloud server option, once
    the option is entered it will be verified with a condition which will use the
    mapping function to see if the option entered is correct, if not an error will
    be printed saying that the option entered is not valid.
    """
    opt = int(input(translate(Messages.GIT_OPTION)))
    try:
        if mapping(Map.GIT_MAP, opt) is not None:
            return mapping(Map.GIT_MAP, opt)
        else:
            print(translate(Messages.ERR_OPTION))
    except OSError as error:
        print(translate(error))


def set_include_venv(repository):
    try:
        include = str(input(translate(Messages.ADD_VENV) + Messages.CHECK_YES_NO))
        if include == "y" or include == "Y":
            make_venv(repository)
    except OSError as error:
        print(translate(error))
