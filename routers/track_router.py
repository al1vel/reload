import sqlite3
from fastapi import APIRouter

connection = sqlite3.connect('reload_database.db', check_same_thread=False)
cursor = connection.cursor()

track_router = APIRouter(
    prefix="/track",
    tags=["Tracks"]
)


@track_router.post("/add_timetrack")
def add_timetrack(username: str, track_name: str):
    cursor.execute(f'SELECT id FROM All_Tracks WHERE track_name = "{track_name}" AND owner = "{username}"')
    ids = cursor.fetchall()
    if len(ids) > 0:
        return f'{username} already has such track as {track_name}'
    cursor.execute(f'INSERT INTO All_Tracks (owner, type, track_name) VALUES ("{username}", "TIME", "{track_name}")')

    cursor.execute(f'SELECT id FROM All_Tracks WHERE track_name = "{track_name}" AND owner = "{username}"')
    track_id = cursor.fetchall()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS Track{track_id} (   
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        occupation TEXT NOT NULL)''')
