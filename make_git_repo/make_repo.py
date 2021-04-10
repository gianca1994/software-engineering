from git import Repo

from make.make_db import set_db
from make.make_dirs import make_seconds_dirs
from constants import COMMIT_MESSAGE
from make.make_files import make_files
from make_git_repo.setters_git import *
from translate import txt_print

def make_repository(repo_name, language):
    repo = Repo.init(repo_name, mkdir=True)

    make_seconds_dirs(repo_name)
    make_files(repo_name)

    set_db(repo_name, language)

    if set_confirm_push(language):
        user_git = set_user_git(language)
        type_git = set_git_type(language)
        repo.git.add(all=True)
        repo.index.commit(print(txt_print(language, COMMIT_MESSAGE)))
        repo.git.execute(("git remote add origin https://" + type_git + ".com/" + user_git + "/" + repo_name + ".git"))
        origin = repo.create_remote(repo_name, repo.remotes.origin.url)
        origin.push()
    return repo_name
