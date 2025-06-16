from fastapi import FastAPI
from backend.db.init import init_db
from backend.api.endpoints import auth_endpoints, user_endpoints
from backend.middlewares import auth_middleware

app = FastAPI()

app.add_middleware(auth_middleware.AuthMiddleware)

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(auth_endpoints.router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_endpoints.router, prefix="/api/users", tags=["Users"])
