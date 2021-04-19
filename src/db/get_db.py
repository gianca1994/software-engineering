from src.db.connect_db import connect
from src.service.constants import Map
from src.service.mapper import mapping


def get_data_db(opt):
    """
    We bring from the database all the names of the table that is requested
    passed by parameter in the 'opt' function, we make a for of row in rows,
    then a for of the data in the row, we add the name to the list and we return.
    """
    data = []
    conn = connect()
    cur = conn.cursor()
    cur.execute(mapping(Map.NAMES_DB_MAP, opt))
    rows = cur.fetchall()
    for row in rows:
        for dat in row:
            data.append(dat)
    return data
