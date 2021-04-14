def create_text_files(file_name, text):
    """
    This method receives as parameter the name of the file and text, the
    objective of this function is to write in each file the text assigned to it.
    """
    try:
        file_name.write(text + "\n")
    except OSError as error:
        print(error)
