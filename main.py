import sqlite3
from fastapi import FastAPI
from database import initialize_database
from user_router import user_router


initialize_database()
# connection = sqlite3.connect('reload_database.db', check_same_thread=False)
# cursor = connection.cursor()

app = FastAPI()


@app.get("/")
async def home():
    return "Zaebis"


app.include_router(user_router)
