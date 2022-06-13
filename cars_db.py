import sqlite3

with sqlite3.connect("car.db") as db:
    curs = db.cursor()

    comand = """CREATE TABLE IF NOT EXISTS cars_store (
        seller text,
        make text,
        model text,
        year integer,
        price integer,
        discount integer
    )"""
    curs.execute(comand)
    # curs.execute("DROP TABLE IF EXISTS cars_store")
    db.commit()

