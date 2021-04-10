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
    for i in range(11):
        dirs = cur.execute("SELECT name FROM dirs WHERE id=?", (i,))
        for index, dir in enumerate(dirs):
            data.append(dir[index])
    return data

MAP_GET_DB = {
    1: "SELECT * FROM requeriments",
    2: "SELECT * FROM dirs",
    3: "SELECT * FROM installsh",
    4: "SELECT * FROM bootsh",
    5: "SELECT * FROM pyvenv",
    6: "SELECT * FROM files",
}


def map_get_db(opt):
    return MAP_GET_DB.get(opt, "nothing")