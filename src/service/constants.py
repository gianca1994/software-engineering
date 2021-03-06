class Config:
    LANGUAGE = None


class Venv:
    VENV_NAME = "venv"


class Gitignore:
    PYTHON = "venv/"


class Repository:
    REPOSITORY_PATH = "repositories/"


class Database:
    DB_FILE = "DataBase.db"
    DB_PATH = "src/db/"

    DICT_MAKE_TABLES = {
        "create table dirs (id integer primary key autoincrement, name text)",
        "create table files (id integer primary key autoincrement, name text)",
        "create table requeriments (id integer primary key autoincrement, name text)",
        "create table installsh (id integer primary key autoincrement, name text)",
        "create table bootsh (id integer primary key autoincrement, name text)",
        "create table db (id integer primary key autoincrement, name text)"
    }

    DICT_CONTENT_TABLES = {
        "SECOND_DIRS": (
            "/app/main/auth",
            "/app/main/models",
            "/app/main/repository",
            "/app/main/resources",
            "/app/main/services",
            "/app/main/templates"
        ),
        "FILES": (
            "app.py",
            "requirements.txt",
            ".gitignore",
            ".env",
            "install.sh",
            "boot.sh",
            "README.md",
            "/app/__init__.py",
            "/app/main/__init__.py",
            "/app/main/auth/__init__.py",
            "/app/main/models/__init__.py",
            "/app/main/repository/__init__.py",
            "/app/main/resources/__init__.py",
            "/app/main/resources/user.py",
            "/app/main/services/__init__.py",
            "/app/main/templates/index.html"
        ),
        "REQ": (
            "pylint",
            "pylint-flask",
            "flask",
            "python-dotenv",
            "flask_restful",
            "flask_jwt_extended",
            "flask_marshmallow",
            "Flask-Cors"
        ),
        "INSTALL": (
            "#!/bin/bash",
            "python3 app.py"
        ),
        "BOOT": (
            "#!/bin/bash",
            "python3 -m venv .",
            "source bin/activate",
            "pip3 install -r requirements.txt"
        ),
        "DB": (
            "/app/main/data",
            "/app/main/database"
        )
    }


class Messages:
    ################# REPOSITORIO #################
    COMMIT_MESSAGE = 'Initial commit'
    PROJECT_NAME = 'Enter the name of the project: '
    GIT_OPTION = 'Enter desired option 1. gitlab | 2. github: '
    USER_GIT = 'Enter the Git username: '
    GIT_PUSH = 'Upload the repository to the cloud'
    ERR_SPACE = 'Repository cannot contain spaces.'
    EXIST_REPO = 'There is already a repository created with that same name!'
    ERR_USER_NOT_STR = 'Invalid user type.'
    ERR_OPTION = 'Option entered invalid.'
    PUSH_OK = 'Repository uploaded successfully!!'
    ############### FIN REPOSITORIO ###############

    ############### DATABASE ###############
    SELECT_DB = 'Add database'
    NAME_DB = 'Database name: '
    TYPE_DB = 'Select the type of database | 1.SQlite | 2.MySQL : '
    ############### FIN DATABASE ###############

    ################# LANGUAGE #################
    SELECT_LANGUAGE = "Language [1-English | 2-Spanish | 3-French | 4-Japanese | 5-German " \
                      "| 6-Italian | 7-Portuguese | 8-Russian | 9-Chinese | 10-Dutch]: "
    CHECK_YES_NO = " [y/n]: "
    ############### FIN LANGUAGE ###############

    ############### VENV ###############
    ADD_VENV = 'Include the virtual environment in your project'
    VENV_INSTALLING = "Installing the virtual environment..."
    VENV_INSTALLED = "The virtual environment was created successfully!"
    ############### FIN VENV ###############

    ################# TERMINAR Y SALIR #################
    FINISH_AND_CLOSE = "Press a key to finish..."
    ############### FIN TERMINAR Y SALIR ###############

class Map:
    INSERT_DB_MAP = {
        "SECOND_DIRS": "insert into dirs(name) values (?)",
        "FILES": "insert into files(name) values (?)",
        "REQ": "insert into requeriments(name) values (?)",
        "INSTALL": "insert into installsh(name) values (?)",
        "BOOT": "insert into bootsh(name) values (?)",
        "DB": "insert into db(name) values (?)"
    }

    NAMES_DB_MAP = {
        1: "SELECT name FROM dirs",
        2: "SELECT name FROM files",
        6: "SELECT name FROM db"
    }

    ALL_DB_MAP = {
        1: "SELECT * FROM dirs",
        2: "SELECT * FROM files",
        3: "SELECT * FROM requeriments",
        4: "SELECT * FROM installsh",
        5: "SELECT * FROM bootsh",
        6: "SELECT * FROM db"
    }

    GIT_MAP = {
        1: 'gitlab',
        2: 'github'
    }

    DB_MAP = {
        1: '.db',
        2: '.sql'
    }

    LANGUAGE_MAP = {
        1: '',
        2: 'es',
        3: 'fr',
        4: 'ja',
        5: 'de',
        6: 'it',
        7: 'pt',
        8: 'ru',
        9: 'zh',
        10: 'nl'
    }

    OS_CLEAR_MAP = {
        "Linux": 'clear',
        "Windows": 'cls',
        "Darwin": 'clear'
    }

    OS_COMMAND_MAP = {
        "Linux": 'python3',
        "Windows": 'py',
        "Darwin": 'python3'
    }


class FileContent:
    ############# REPOSITORIO ##################
    DIC_ENV = """

    """
    DIC_GITIGNORE = """
    # -- Symfony2 -----------------------------------------
    app/bootstrap.php.cache
    app/bootstrap_cache.php.cache
    app/config/parameters.ini
    app/config/parameters.yml
    app/cache/*
    app/logs/*
    vendor/*
    web/bundles/*
    web/css/*
    web/js/*
    web/uploads/*
    """
    DIC_APP = """if __name__ == '__main__':
        app.run()
    """
    ############# FIN REPOSITORIO ##############

    ################# APP ######################
    APP_INIT = """from flask import Flask

    app = Flask(__name__)

    app.run(debug=True)
    """
    ################# FIN APP ##################

    ################# MAIN ##################
    MAIN_INIT = """from flask import Blueprint

    admin_bp = Blueprint('admin', __name__, template_folder='templates')

    from . import routes
    """
    ################# FIN MAIN ##############

    ############### AUTH ###################
    AUTH_INIT = """from flask import Blueprint

    auth_bp = Blueprint('auth', __name__, template_folder='templates')

    from . import routes
    """
    ############### FIN AUTH ###################

    ############### MODELS ###################
    MODELS_INIT = """
    """
    ############### FIN MODELS ###############

    ############### REPOSITORY ###################
    REPOSITORY_INIT = """
    """
    ############### FIN REPOSITORY ###############

    ############### RESOURCES ###################
    RESOURCES_INIT = """
    """
    RESOURCES_USER = """
    """
    ############### FIN RESOURCES ###############

    ############### SERVICES ###################
    SERVICES_INIT = """
    """
    ############### FIN SERVICES ###############

    ############### TEMPLATES###################
    TEMPLATES_INDEX = """<!DOCTYPE html>
    <html>
        <body>

            <h1>My First Heading</h1>
            <p>My first paragraph.</p>

        </body>
    </html>
    """
    ############### FIN TEMPLATES###############
