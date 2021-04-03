from operations import *

dict_requeriments = {"pylint", "pylint-flask", "flask", "python-dotenv", 
                    "flask_restful", "flask_jwt_extended", 
                    "flask_marshmallow", "Flask-Cors"}

dicc_dirs = {"authentication", "models", "repository", "resources", "services", "templates"}

dicc_pyvenv = {"home = /usr/bin", "include-system-site-packages = false", "version = 3.8.5"}

dicc_inits = {"app/main/__init__.py", "app/main/models/__init__.py", "app/main/repository/__init__.py",
            "app/main/resources/__init__.py", "app/main/services/__init__.py"}

dicc_init_auth = {"from .routes import auth as auth_blueprint", "from .decorators import admin_login_required"}

dicc_boot = {"#!/bin/bash", "python3 app.py"}

dicc_install = {"#!/bin/bash", "python3 -m venv .", "source bin/activate", "pip3 install -r requirements.txt"}

def create_main_dir():
    name_dir = "main"
    route = "app"
    create_dir(route, name_dir)

def create_seconds_directories():
    route = "app/main"
    for seconds_dir in dicc_dirs:
        create_dir(route, seconds_dir)

def create_boot():
    name_file = "app/boot.sh"
    create_file(name_file, dicc_boot, True)

def create_install():
    name_file = "app/install.sh"
    create_file(name_file, dicc_install, True)

def create_requeriments():
    name_file = "app/requeriments.txt"
    create_file(name_file, dict_requeriments, True)

def create_readme():
    name_file = "app/README.md"
    create_file(name_file, "flask", False)

def create_pyvenv():
    name_file = "app/pyvenv.cfg"
    create_file(name_file, dicc_pyvenv, True)

def create_inits():
    for inits in dicc_inits:
        create_file(inits, "", False)
    
    name_init_auth = "app/main/authentication/__init__.py"
    create_file(name_init_auth,dicc_init_auth,True)
