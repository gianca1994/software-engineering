import os
import platform

from src.service.constants import Map, Messages, Venv, Gitignore
from src.service.mapper import mapping
from src.service.translate import translate
from src.work.make_text import make_text_file


def make_venv(repository_path):
    # TODO: Document
    try:
        command = mapping(Map.OS_COMMAND_MAP, platform.system())
        path_venv = repository_path + "/" + Venv.VENV_NAME
        print(translate(Messages.VENV_INSTALLING))
        os.system(command + " " + "-m venv" + " " + path_venv)
        make_gitignore(repository_path)
        print((translate(Messages.VENV_INSTALLED)) + "\n")
    except OSError as error:
        print(translate(error))


def make_gitignore(repository_path):
    # TODO: Document
    with open(repository_path + "/.gitignore", "r+") as file:
        make_text_file(file, Gitignore.PYTHON)
    file.close()
