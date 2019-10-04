import sqlite3

conn = sqlite3.connect('med_data.db')
c = conn.cursor()


def make_script_sql(skrypt):
    with open(skrypt, encoding='utf-8') as f:
        query = f.read()
    c.executescript(query)


make_script_sql('db_init.sql')

conn.commit()

conn.close()
