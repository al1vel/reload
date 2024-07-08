from fastapi import FastAPI
from database import initialize_database
from routers.user_router import user_router
from routers.track_router import track_router

initialize_database()
# connection = sqlite3.connect('reload_database.db', check_same_thread=False)
# cursor = connection.cursor()

app = FastAPI()


@app.get("/")
async def home():
    return "Zaebis"


app.include_router(user_router)
app.include_router(track_router)
