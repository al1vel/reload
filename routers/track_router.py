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
        return f'User {username} has already created such track as {track_name}'
    cursor.execute(f'INSERT INTO All_Tracks (owner, type, track_name) VALUES ("{username}", "TIME", "{track_name}")')
    return f'User {username} successfully added a new track "{track_name}"'


@track_router.get("/all_tracks")
def get_all_tracks():
    cursor.execute(f'SELECT * FROM All_Tracks')
    all_tracks = cursor.fetchall()
    return all_tracks


@track_router.post("/add_time")
def add_time(username: str, track_name: str, date: str, time: str, occupation=""):
    amount_of_time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
    cursor.execute(f'INSERT INTO Timetrack_Operations (owner, track_name, date, amount_of_time, occupation) '
                   f'VALUES ("{username}", "{track_name}", "{date}", "{amount_of_time}", "{occupation}")')
    return f'User {username} successfully added {time} to track {track_name}'


@track_router.get("/get_track")
def get_track(track_name: str, username: str):
    cursor.execute(f'SELECT * FROM Timetrack_Operations WHERE track_name = "{track_name}" AND owner = "{username}"')
    track = cursor.fetchall()
    return track
