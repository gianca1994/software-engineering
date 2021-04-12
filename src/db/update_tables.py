from src.db.connect_db import connect


def db_update():
    conn = connect()
    cursorObj = conn.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    conn.commit()
