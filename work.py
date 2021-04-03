from operations import *

dict_requeriments = {"pylint", "pylint-flask", "flask", "python-dotenv", 
                    "flask_restful", "flask_jwt_extended", 
                    "flask_marshmallow", "Flask-Cors"}

dicc_dirs = {"authentication", "models", "repository", "resources", "services", "templates"}

def create_main_dir():
    name_dir = "main"
    route = ""
    create_dir(route, name_dir)

def create_seconds_directories():
    route = "main"
    for seconds_dir in dicc_dirs:
        create_dir(route, seconds_dir)

def create_requeriments():
    name_file = "requeriments.txt"
    create_file(name_file, dict_requeriments, True)

def create_readme():
    name_file = "README.md"
    create_file(name_file, "flask", False)