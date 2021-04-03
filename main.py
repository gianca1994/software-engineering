from work import *


def main():
    # Creamos la carpeta del proyecto
    create_project_dir()
    # Creamos el app.py
    create_app_file()
    # Creamos el directorio main
    create_main_dir()
    # Creamos los directorios secundarios dentro del main
    create_secondary_dirs()
    # Creamos el readme
    create_readme()
    # Creamos el requeriments
    create_requeriments()
    # Creamos el pyvenv
    create_pyvenv()
    # Creamos los __init__ en las carpetas
    create_inits()
    # Creamos el install.sh
    create_install()
    # Creamos el boot.sh
    create_boot()
    # Creamos el decorators.py de la carpeta autenticacion
    create_decorators_file()
    # Creamos el routes.py de la carpeta autenticacion
    create_routes_file()


if __name__ == '__main__':
    main()
