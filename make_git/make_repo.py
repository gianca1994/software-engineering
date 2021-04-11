import os

from git import Repo

from make.make_db import set_db
from make.make_dirs import make_seconds_dirs
from constants.constants_globals import COMMIT_MESSAGE, PUSH_OK, EXIST_REPO
from make.make_files import make_files
from make_git.setters_git import set_confirm_push, set_user_git, set_git_type, set_name_project

from service.translate import txt_print


def make_repository(repo_name, language):
    if not os.path.isdir(repo_name):
        repo = Repo.init(repo_name, mkdir=True)
        make_seconds_dirs(repo_name)
        make_files(repo_name)
        set_db(repo_name, language)

        if set_confirm_push(language):
            print("Hola")
            user_git = set_user_git(language)
            type_git = set_git_type(language)
            repo.git.add(all=True)
            repo.index.commit(COMMIT_MESSAGE)
            repo.git.execute(
                "git remote add origin https://" + type_git + ".com/" + user_git + "/" + repo_name + ".git")
            origin = repo.create_remote(repo_name, repo.remotes.origin.url)
            origin.push()
            print("\n" + txt_print(language, PUSH_OK,
                                   True) + f' User: {user_git} | Link: https://{type_git}.com/{user_git}/{repo_name}')
        return repo_name
    else:
        txt_print(language, EXIST_REPO, False)
        set_name_project(language)
