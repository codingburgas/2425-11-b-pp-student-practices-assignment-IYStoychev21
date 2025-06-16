from fastapi import APIRouter, HTTPException
from backend.schemas import user_schema, auth_schema
from backend.services import auth_service

router = APIRouter()

@router.post("/register", response_model=user_schema.UserOut)
async def register_user(user: auth_schema.UserCreate):
    try:
        new_user = await auth_service.register_user(user)
        return new_user
    except HTTPException as e:
        raise e

@router.post("/login")
async def login_user(login_data: auth_schema.Login):
    try:
        token = await auth_service.login_user(login_data)
        return token
    except HTTPException as e:
        raise e
