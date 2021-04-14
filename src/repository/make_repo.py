import os

from git import Repo
from src.service.mapper import mapping

from src.work.make_db import set_db
from src.work.make_dirs import make_seconds_dirs
from src.service.constants import Messages, Map

from src.work.make_files import make_files
from src.service.utilities import clear_os

from src.service.translate import txt_print


"""
Method used for the creation of the repository, it receives as parameters the name of the repository
and the language used.

"""

def make_repository(repo_name, language):
    path = Messages.REPOSITORY_PATH

    """
    This if condition which will receive the path and the repository name will be used to check if the
    specified path is an existing directory or not. This method follows a symbolic link, which means that
    if the specified path is a symbolic link pointing to a directory, the method will return true.
    """
    if not os.path.isdir(path + repo_name):
        repo = Repo.init(path + repo_name, mkdir=True)
        make_seconds_dirs(path + repo_name)
        make_files(path + repo_name)
        set_db(path + repo_name, language)

        """
        This condition will receive the call of the function set_confirm_push where it will be sent by argument the language used,
        in this condition will be asked the user name and hosting you want to use, once entered this data is performed an add to load
        the files and folders in the repository created, then a commit where a default message will be passed and finally a push will 
        be executed to upload all files and folders to the repository created in GitHub or GitLab. 
        At the end of the process it will return the URL where the files were uploaded.
        """
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

"""
This method will ask for the repository name, then a while condition is raised to verify that the repository does not contain spaces,
if it does not contain spaces the repository name will be saved, if it contains spaces an error message will be printed and the repository
name without spaces will be asked again.
"""
def set_name_project(language):
    name_repo = str(input(txt_print(language, Messages.PROJECT_NAME, True)))

    while not " " in name_repo:
        make_repository(name_repo, language)
        break
    else:
        clear_os()
        txt_print(language, Messages.ERR_SPACE, False)
        set_name_project(language)

"""
This method will ask the user if he/she wants to upload the repository to the cloud.
"""
def set_confirm_push(language):
    try:
        confirm = str(input(txt_print(language, Messages.GIT_PUSH, True) + Messages.CHECK_YES_NO))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        txt_print(language, error, False)

"""
This method will ask for the user name, in case it is correct it will return the user name and in case 
it is not correct it will print an error message.
"""
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

"""
This method will ask the user to enter the desired cloud server option, once the option is entered it will
be verified with a condition which will use the mapping function to see if the option entered is correct, 
if not an error will be printed saying that the option entered is not valid.
"""
def set_git_type(language):
    opt = int(input(txt_print(language, Messages.GIT_OPTION, True)))
    try:
        if mapping(Map.GIT_MAP, opt) is not None:
            return mapping(Map.GIT_MAP, opt)
        else:
            txt_print(language, Messages.ERR_OPTION, False)
    except OSError as error:
        txt_print(language, error, False)
