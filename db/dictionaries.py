DICT_REQ = {"pylint",
            "pylint-flask",
            "flask",
            "python-dotenv",
            "flask_restful",
            "flask_jwt_extended",
            "flask_marshmallow",
            "Flask-Cors"}

DICT_DIRS = {"authentication",
             "models",
             "repository",
             "resources",
             "services",
             "templates"}

DICT_INSTALL = {"#!/bin/bash",
                "python3 -m venv .",
                "source bin/activate",
                "pip3 install -r requirements.txt"}

DICT_BOOT = {"#!/bin/bash",
             "python3 app.py"}

DICT_PYVENV = {"home = /usr/bin",
               "include-system-site-packages = false",
               "version = 3.8.5"}
