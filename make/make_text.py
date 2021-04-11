def create_text_files(file_name, text):
    try:

        file_name.write(text + "\n")
    except OSError as error:
        print(error)
