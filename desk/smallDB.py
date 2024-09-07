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


def add_time_to_db(date, amount_of_time, occupation):
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO Operations (date, amount_of_time, occupation) VALUES (?, ?, ?)', (date, amount_of_time, occupation))
    connection.commit()
    connection.close()


def get_all_regs():
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Operations')
    data = cursor.fetchall()
    print(data)

    connection.commit()
    connection.close()
