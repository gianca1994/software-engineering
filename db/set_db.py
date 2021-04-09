from db.connect_db import connect

def set_data_db(opt, name2):
    name1 = map_set_db(opt)
    connection = connect()
    connection.execute(name1, (name2,))
    connection.commit()
    connection.close()

switch = {
    1: "insert into requeriments(name) values (?)",
    2: "insert into dirs(name) values (?)",
    3: "insert into installsh(name) values (?)",
    4: "insert into bootsh(name) values (?)",
    5: "insert into pyvenv(name) values (?)",
}

def map_set_db(opt):
    return switch.get(opt, "nothing")
