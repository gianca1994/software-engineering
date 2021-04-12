DB_FILE = "db/DataBase.db"

DICT_MAKE_TABLES = {
    "create table dirs (id integer primary key autoincrement, name text)",
    "create table files (id integer primary key autoincrement, name text)",
    "create table requeriments (id integer primary key autoincrement, name text)",
    "create table installsh (id integer primary key autoincrement, name text)",
    "create table bootsh (id integer primary key autoincrement, name text)",
    "create table pyvenv (id integer primary key autoincrement, name text)",
    "create table db (id integer primary key autoincrement, name text)"
}

MAP_DB = {
    1: "insert into dirs(name) values (?)",
    2: "insert into files(name) values (?)",
    3: "insert into requeriments(name) values (?)",
    4: "insert into installsh(name) values (?)",
    5: "insert into bootsh(name) values (?)",
    6: "insert into pyvenv(name) values (?)",
    7: "insert into db(name) values (?)"
}

MAP_GET_NAMES_DB = {
    1: "SELECT name FROM dirs",
    2: "SELECT name FROM files",
    7: "SELECT name FROM db"
}

MAP_GET_DB = {
    1: "SELECT * FROM dirs",
    2: "SELECT * FROM files",
    3: "SELECT * FROM requeriments",
    4: "SELECT * FROM installsh",
    5: "SELECT * FROM bootsh",
    6: "SELECT * FROM pyvenv",
    7: "SELECT * FROM db"
}

DICT_REQ = {"pylint",
            "pylint-flask",
            "flask",
            "python-dotenv",
            "flask_restful",
            "flask_jwt_extended",
            "flask_marshmallow",
            "Flask-Cors"}

DICT_FILES = {"app.py",
              "requirements.txt",
              ".gitignore",
              ".env",
              "install.sh",
              "boot.sh",
              "pyvenv.cfg",
              "README.md",
              "/app/__init__.py",
              "/app/main/__init__.py",
              "/app/main/auth/__init__.py",
              "/app/main/models/__init__.py",
              "/app/main/repository/__init__.py",
              "/app/main/resources/__init__.py",
              "/app/main/resources/user.py",
              "/app/main/services/__init__.py",
              "/app/main/templates/index.html"}

DICT_SECOND_DIRS = {"/app/main/auth",
                    "/app/main/models",
                    "/app/main/repository",
                    "/app/main/resources",
                    "/app/main/services",
                    "/app/main/templates"}

DICT_DB = {"/app/main/database",
           "/app/main/data"}

DICT_INSTALL = {"#!/bin/bash",
                "python3 -m venv .",
                "source bin/activate",
                "pip3 install -r requirements.txt"}

DICT_BOOT = {"#!/bin/bash",
             "python3 app.py"}

DICT_PYVENV = {"home = /usr/bin",
               "include-system-site-packages = false",
               "version = 3.8.5"}
