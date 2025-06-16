from fastapi import FastAPI
from backend.db.init import init_db
from backend.api.endpoints import auth_endpoints

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(auth_endpoints.router, prefix="/api/auth", tags=["Auth"])
