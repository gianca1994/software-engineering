from src.db.get_db import get_data_db


def make_files(project_name):
    """
    This function receives by parameter the name that was chosen for the project
    folder, a call is made to the function 'get_data_db' passing it as a parameter
    the number that will be used to bring the names of all the files, by executing
    the mapping. With the for we create as many files as the number of names returned
    from the 'get_data_db'
    """
    for file in get_data_db(2):
        create_file(project_name, file, )


def create_file(name_dir, name_file):
    """
    This function receives by parameter the name of the directory and the file,
    then concatenates them, putting in between '/' to indicate that this file
    is going to be created in the indicated path.
    """
    try:
        route = (name_dir + "/" + name_file)
        file = open(route, "w")
        file.close()
    except OSError as error:
        print(error)
