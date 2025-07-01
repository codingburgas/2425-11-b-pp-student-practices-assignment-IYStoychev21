from fastapi import APIRouter, HTTPException
from schemas import user_schema, auth_schema
from services import auth_service

router = APIRouter()

@router.post("/register", response_model=user_schema.UserOut)
async def register_user(user: auth_schema.UserCreate):
    """
    Register a new user account.
    
    Args:
        user (auth_schema.UserCreate): User registration data including username,
                                      password, first_name, and last_name
    
    Returns:
        user_schema.UserOut: The created user information (without password)
        
    Raises:
        HTTPException: 400 if validation fails or username already exists
    """
    try:
        new_user = await auth_service.register_user(user)
        return new_user
    except HTTPException as e:
        raise e

@router.post("/login")
async def login_user(login_data: auth_schema.Login):
    """
    Authenticate a user and return a JWT token.
    
    Args:
        login_data (auth_schema.Login): User login credentials
    
    Returns:
        dict: Dictionary containing the JWT access token
        
    Raises:
        HTTPException: 400 if credentials are invalid
    """
    try:
        token = await auth_service.login_user(login_data)
        return token
    except HTTPException as e:
        raise e
