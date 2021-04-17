import os
import platform

from src.service.constants import Map, Messages, Venv
from src.service.mapper import mapping
from src.service.translate import translate


def make_venv(repository_path):
    try:
        command = mapping(Map.OS_COMMAND_MAP, platform.system())
        path_venv = repository_path + "/" + Venv.VENV_NAME
        print(translate(Messages.VENV_INSTALLING))
        os.system(command + " " + "-m venv" + " " + path_venv)
        print((translate(Messages.VENV_INSTALLED)) + "\n")
    except OSError as error:
        print(translate(error))
