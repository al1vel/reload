import sqlite3


def initialize_database():
    connection = sqlite3.connect('reload_database.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL)''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS All_Tracks (
    id INTEGER PRIMARY KEY,
    owner TEXT NOT NULL,
    type TEXT NOT NULL,
    track_name TEXT NOT NULL
    )
    ''')
