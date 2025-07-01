from fastapi import APIRouter, HTTPException, Request, Depends
from schemas import user_schema
from services import  user_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.get("/get", response_model=user_schema.UserOut)
async def get_current_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current authenticated user's profile information.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: Current user's profile information
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user_id = request.state.user_id
    try:
        user = await user_service.get_current_user(user_id)
        return user
    except HTTPException as e:
        raise e

@router.delete("/delete", response_model=user_schema.UserOut)
async def delete_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Delete the current authenticated user's account.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: Information of the deleted user
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user_id = request.state.user_id
    try:
        user = await user_service.delete_current_user(user_id)
        return user
    except HTTPException as e:
        raise e

@router.delete("/delete/{id}", response_model=user_schema.UserOut)
async def delete_user_admin(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Delete another user's account (admin only operation).
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the user to delete
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: Information of the deleted user
        
    Raises:
        HTTPException: 404 if user does not exist, 403 if not admin
    """
    user_id = request.state.user_id
    try:
        user = await user_service.delete_user_admin(user_id, id)
        return user
    except HTTPException as e:
        raise e

@router.put("/update", response_model=user_schema.UserOut)
async def update_user(request: Request, user_data: user_schema.UserUpdate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Update the current authenticated user's profile information.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        user_data (user_schema.UserUpdate): Updated user information
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: Updated user information
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user_id = request.state.user_id
    try:
        user = await user_service.update_current_user(user_id, user_data)
        return user
    except HTTPException as e:
        raise e

@router.put("/update/{id}", response_model=user_schema.UserOut)
async def update_user_admin(request: Request, id: int, user_data: user_schema.UserUpdate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Update another user's profile information (admin only operation).
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the user to update
        user_data (user_schema.UserUpdate): Updated user information
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: Updated user information
        
    Raises:
        HTTPException: 404 if user does not exist, 403 if not admin
    """
    user_id = request.state.user_id
    try:
        user = await user_service.update_user_admin(user_id, id, user_data)
        return user
    except HTTPException as e:
        raise e

@router.get("/get/all", response_model=list[user_schema.UserOut])
async def get_users_all(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get all users in the system.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        credentials: JWT bearer token for authentication
    
    Returns:
        list[user_schema.UserOut]: List of all users in the system
        
    Raises:
        HTTPException: 404 if requesting user does not exist
    """
    user_id = request.state.user_id
    try:
        user = await user_service.get_all_users(user_id)
        return user
    except HTTPException as e:
        raise e

@router.get("/get/{id}", response_model=user_schema.UserOut)
async def get_user(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get a specific user by their ID.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the user to retrieve
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: The requested user's information
        
    Raises:
        HTTPException: 404 if either user does not exist
    """
    user_id = request.state.user_id
    try:
        user = await user_service.get_user(user_id, id)
        return user
    except HTTPException as e:
        raise e

@router.put("/update/role/{id}/{role_id}", response_model=user_schema.UserOut)
async def update_user_role(request: Request, id: int, role_id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Update a user's role (admin only operation).
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the user whose role to update
        role_id (int): ID of the new role to assign
        credentials: JWT bearer token for authentication
    
    Returns:
        user_schema.UserOut: User information with updated role
        
    Raises:
        HTTPException: 404 if user does not exist, 403 if not admin
    """
    user_id = request.state.user_id
    try:
         user = await user_service.change_user_role(user_id, id, role_id)
         return user
    except HTTPException as e:
         raise e
