from fastapi import APIRouter, HTTPException, Request, Depends
from backend.schemas import user_schema
from backend.services import  user_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.get("/get", response_model=user_schema.UserOut)
async def get_current_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.get_current_user(user_id)
        return user
    except HTTPException as e:
        raise e

@router.delete("/delete", response_model=user_schema.UserOut)
async def delete_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.delete_current_user(user_id)
        return user
    except HTTPException as e:
        raise e

@router.delete("/delete/{id}", response_model=user_schema.UserOut)
async def delete_user_admin(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.delete_user_admin(user_id, id)
        return user
    except HTTPException as e:
        raise e

@router.put("/update", response_model=user_schema.UserOut)
async def update_user(request: Request, user_data: user_schema.UserUpdate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.update_current_user(user_id, user_data)
        return user
    except HTTPException as e:
        raise e

@router.put("/update/{id}", response_model=user_schema.UserOut)
async def update_user_admin(request: Request, id: int, user_data: user_schema.UserUpdate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.update_user_admin(user_id, id, user_data)
        return user
    except HTTPException as e:
        raise e

@router.get("/get/all", response_model=list[user_schema.UserOut])
async def get_users_all(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.get_all_users(user_id)
        return user
    except HTTPException as e:
        raise e

@router.get("/get/{id}", response_model=user_schema.UserOut)
async def get_user(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        user = await user_service.get_user(user_id, id)
        return user
    except HTTPException as e:
        raise e

@router.put("/update/role/{id}/{role_id}", response_model=user_schema.UserOut)
async def update_user_role(request: Request, id: int, role_id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
         user = await user_service.change_user_role(user_id, id, role_id)
         return user
    except HTTPException as e:
         raise e
