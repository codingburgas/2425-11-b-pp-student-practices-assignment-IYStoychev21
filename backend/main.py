from fastapi import FastAPI
from backend.db.init import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}
