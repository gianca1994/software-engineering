from db.connect_db import connect


def set_req_db(name_req):
    connection = connect()
    connection.execute(
        "insert into requeriments(name) values (?)", (name_req,))
    connection.commit()
    connection.close()


def set_dir_db(name_dir):
    connection = connect()
    connection.execute("insert into dirs(name) values (?)", (name_dir,))
    connection.commit()
    connection.close()


def set_installsh_db(name_installsh):
    connection = connect()
    connection.execute("insert into installsh(name) values (?)", (name_installsh,))
    connection.commit()
    connection.close()

def set_bootsh_db(name_booth):
    connection = connect()
    connection.execute("insert into bootsh(name) values (?)", (name_booth,))
    connection.commit()
    connection.close()

def set_pyvenv_db(name_pyvenv):
    connection = connect()
    connection.execute("insert into pyvenv(name) values (?)", (name_pyvenv,))
    connection.commit()
    connection.close()

