

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
DIC_APP = """
if __name__ == '__main__':
    app.run()
"""
############# FIN REPOSITORIO ##############


################# APP ######################
APP_INIT = """
from flask import Flask

app = Flask(__name__)

app.run(debug=True)
"""
################# FIN APP ##################


################# MAIN ##################
MAIN_INIT = """
from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

from . import routes
"""
################# FIN MAIN ##############


############### AUTH ###################
AUTH_INIT = """
from flask import Blueprint

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
TEMPLATES_INDEX = """
<!DOCTYPE html>
<html>
    <body>

        <h1>My First Heading</h1>
        <p>My first paragraph.</p>

    </body>
</html>
"""
############### FIN TEMPLATES###############