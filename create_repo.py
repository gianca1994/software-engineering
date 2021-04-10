from git import Repo

COMMIT_MESSAGE = 'Initial commit'

def create_repo(repo_name, user_git, name_git):
    repo = Repo.init(repo_name, mkdir=True)
    # ACA AGREGAMOS TODAS LAS CARPETAS Y ARCHIVOS AL REPO
    repo.git.execute("git add *")
    repo.index.commit(COMMIT_MESSAGE)
    repo.git.execute(("git remote add origin https://" + name_git + ".com/" + user_git + "/" + repo_name + ".git"))
    origin = repo.create_remote(repo_name, repo.remotes.origin.url)
    origin.push()
    return repo_name


def main():
    create_test_repo('name_repo', 'User_name', 'type_git')


if __name__ == '__main__':
    main()
