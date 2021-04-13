from src.db.connect_db import connect
from src.service.constants import Map
from src.service.mapper import mapping


"""def select_show_db(opt):
    conn = connect()
    cur = conn.cursor()
    cur.execute(mapping(Map.MAP_GET_NAMES_DB, opt))
    rows = cur.fetchall()
    for row in rows:
        print(row)"""


def get_data_db(opt):
    data = []
    conn = connect()
    cur = conn.cursor()
    cur.execute(mapping(Map.NAMES_DB_MAP, opt))
    rows = cur.fetchall()
    for row in rows:
        for dat in row:
            data.append(dat)
    return data
