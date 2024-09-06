import sqlite3


def db_init():
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Operations (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    amount_of_time INTEGER,
    occupation TEXT NOT NULL)''')
