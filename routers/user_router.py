import sqlite3
from fastapi import APIRouter

connection = sqlite3.connect('reload_database.db', check_same_thread=False)
cursor = connection.cursor()

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@user_router.post("/add")
def add_user(username: str, email: str, password: str):
    cursor.execute(f'INSERT INTO Users (username, email, password) VALUES ("{username}", "{email}", "{password}")')


@user_router.get("/all_users")
def get_all_users():
    cursor.execute(f'SELECT * FROM Users')
    all_users = cursor.fetchall()
    return all_users
