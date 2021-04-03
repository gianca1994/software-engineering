import os

from work import *

from operations import create_dir

def main():

    # Creamos el directorio main
    create_main_dir()
    # Creamos los directorios secundarios dentro del main
    create_seconds_directories()
    # Creamos el readme
    create_readme()
    # Creamos el requeriments
    create_requeriments()
    

    
if __name__ == '__main__':
    main()

