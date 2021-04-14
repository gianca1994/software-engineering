"""
This method receives as parameter the name of the file and text, the 
objective of this function is to write in each file the text assigned to it.
"""
def create_text_files(file_name, text):
    try:
        file_name.write(text + "\n")
    except OSError as error:
        print(error)
