from db.connect_db import connect


def select_show_db(opt):
    conn = connect()
    cur = conn.cursor()
    cur.execute(map_get_db(opt))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def get_dir_db():
    data = []
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name FROM dirs")
    rows = cur.fetchall()
    for dirs in rows:
        for dir in dirs:
            data.append(dir)
    return data


def get_file_db():
    data = []
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name FROM files")
    rows = cur.fetchall()
    for files in rows:
        for file in files:
            data.append(file)
    return data

def get_db_dict():
    data = []
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name FROM db")
    rows = cur.fetchall()
    for dbs in rows:
        for db in dbs:
            data.append(db)
    return data

MAP_GET_DB = {
    1: "SELECT * FROM requeriments",
    2: "SELECT * FROM dirs",
    3: "SELECT * FROM installsh",
    4: "SELECT * FROM bootsh",
    5: "SELECT * FROM pyvenv",
    6: "SELECT * FROM files",
    7: "SELECT * FROM db",
}


def map_get_db(opt):
    return MAP_GET_DB.get(opt, "nothing")
