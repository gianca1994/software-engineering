from constants.constants_db import MAP_GET_DB, MAP_GET_NAMES_DB
from db.connect_db import connect


def map_get_db(opt, get_specific):
    if get_specific:
        return MAP_GET_NAMES_DB.get(opt, )
    else:
        return MAP_GET_DB.get(opt, )


def select_show_db(opt):
    conn = connect()
    cur = conn.cursor()
    cur.execute(map_get_db(opt, False))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def get_data_db(opt):
    data = []
    conn = connect()
    cur = conn.cursor()
    cur.execute(map_get_db(opt, True))
    rows = cur.fetchall()
    for row in rows:
        for dat in row:
            data.append(dat)
    return data
