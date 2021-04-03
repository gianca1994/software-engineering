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

main_route = "app"

app_code = """from main import create_app
from main import db
from main.models import UserModel

import os


def create_admins_in_db():
    admins = db.session.query(UserModel.id_num).filter(UserModel.admin == True)
    admins_list = [admin for admin, in admins]
    if len(admins_list) == 0:
        print("Creando admin")
        user = UserModel(
            email=os.getenv('ADMIN_MAIL'),
            plain_password=os.getenv('ADMIN_PLAIN_PASSWORD'),
            admin=bool(os.getenv('ADMIN_BOOL'))
        )
        db.session.add(user)
        db.session.commit()

    else:
        pass


# Creating Flask app instance
app = create_app()

# Loading app context
app.app_context().push()

# If this script is run, the db is created if not; and the app is run in an specific port
if __name__ == '__main__':
    db.create_all()
    create_admins_in_db()
    app.run(debug=True, port=os.getenv('PORT'))
"""

decorators_code = """from main import jwt
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims


# We declare here the attribute that will be used for the user identification
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id_num


# We declare here the claims that the JWT will store
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {
        'id_num': user.id_num,
        'admin': user.admin
    }


# We define this decorator in order to restrict the methods that are only accessed by the administrators
def admin_login_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()  # We verify if the entered token is valid
        claims = get_jwt_claims()  # We fetch the JWT claims

        if claims['admin']:
            return method(*args, **kwargs)  # If the logged user is an admin, we execute the method
        else:
            return 'You are not allowed to access to this information', 403

    return wrapper
"""

routes_code = """from main.models import UserModel
from main import db

from flask import request, Blueprint
from flask_jwt_extended import create_access_token


# The auth blueprint 
auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    entered_email = str(request.get_json().get('email'))
    entered_password = str(request.get_json().get('password'))
    print(entered_password)
    user = db.session.query(UserModel).filter(UserModel.email == entered_email).first_or_404()

    passwords_match = user.validate_password(entered_password)
    # True value if both passwords match

    if passwords_match:
        access_token = create_access_token(identity=user)
        data = {"id": user.id_num,
                "email": user.email,
                "token": access_token
                }
        return data, 200
    else:
        return 'You have entered wrong credentials.', 401
"""
