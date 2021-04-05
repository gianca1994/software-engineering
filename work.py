from dict_and_codes import *
from operations import *


def create_project_dir():
    create_dir("", main_route)


def create_main_dir():
    name_dir = "main"
    route = main_route
    create_dir(route, name_dir)


def create_secondary_dirs():
    route = main_route + "/" + "main"
    for seconds_dir in dict_dirs:
        create_dir(route, seconds_dir)


def create_app_file():
    name_file = main_route + "/" + "app.py"
    create_file(name_file, app_code, False)


def create_boot():
    name_file = main_route + "/" + "boot.sh"
    create_file(name_file, dict_boot, True)


def create_install():
    name_file = main_route + "/" + "install.sh"
    create_file(name_file, dict_install, True)


def create_requeriments():
    name_file = main_route + "/" + "requeriments.txt"
    create_file(name_file, dict_requeri, True)


def create_readme():
    name_file = main_route + "/" + "README.md"
    create_file(name_file, "flask", False)


def create_pyvenv():
    name_file = main_route + "/" + "pyvenv.cfg"
    create_file(name_file, dict_pyvenv, True)


def create_inits():
    for inits in dict_inits:
        create_file(inits, "", False)

    name_init_auth = main_route + "/main/authentication/__init__.py"
    create_file(name_init_auth, dict_init_auth, True)


def create_decorators_file():
    name_file = main_route + "/main/authentication/" + "decorators.py"
    create_file(name_file, decorators_code, False)


def create_routes_file():
    name_file = main_route + "/main/authentication/" + "routes.py"
    create_file(name_file, routes_code, False)
