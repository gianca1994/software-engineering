main_route = "app"

dict_requeri = {"pylint", "pylint-flask", "flask", "python-dotenv",
                "flask_restful", "flask_jwt_extended",
                "flask_marshmallow", "Flask-Cors"}

dict_dirs = {"authentication", "models", "repository", "resources", "services", "templates"}

dict_pyvenv = {"home = /usr/bin", "include-system-site-packages = false", "version = 3.8.5"}

dict_inits = {"app/main/__init__.py", "app/main/models/__init__.py", "app/main/repository/__init__.py",
              "app/main/resources/__init__.py", "app/main/services/__init__.py"}

dict_init_auth = {"from .routes import auth as auth_blueprint", "from .decorators import admin_login_required"}

dict_boot = {"#!/bin/bash", "python3 app.py"}

dict_install = {"#!/bin/bash", "python3 -m venv .", "source bin/activate", "pip3 install -r requirements.txt"}

app_code = """app.py code:
line 1
line 2
line 3
line ....
line n
"""

decorators_code = """decorators.py code:
line 1
line 2
line 3
line ....
line n
"""

routes_code = """routes.py code:
line 1
line 2
line 3
line ....
line n
"""
