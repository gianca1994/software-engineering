main_route = "app"
app_main = "app/main/"

dict_inits = {app_main + "__init__.py", app_main + "models/__init__.py", app_main + "repository/__init__.py",
              app_main + "resources/__init__.py", app_main + "services/__init__.py"}

dict_init_auth = {"from .routes import auth as auth_blueprint",
                  "from .decorators import admin_login_required"}


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
