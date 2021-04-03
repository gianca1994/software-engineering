import os

from work import *

from operations import create_dir

def main():

    # Creamos la carpeta del proyecto
    create_project_dir()
    # Creamos el directorio main
    create_main_dir()
    # Creamos los directorios secundarios dentro del main
    create_seconds_directories()
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
    
    
if __name__ == '__main__':
    main()

