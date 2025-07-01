from fastapi.exceptions import HTTPException
from repositories import user_repository
from core.security import create_access_token
from schemas import auth_schema
import bcrypt

async def login_user(login_data: auth_schema.Login):
    """
    Authenticate a user and return a JWT token.
    
    Args:
        login_data (auth_schema.Login): User login credentials containing username and password
        
    Returns:
        dict: Dictionary containing the JWT access token
        
    Raises:
        HTTPException: 400 if credentials are invalid or empty
    """
    if not login_data.password.strip():
        raise HTTPException(status_code=400, detail="Password can't be empty")

    if not login_data.username.strip():
        raise HTTPException(status_code=400, detail="Username can't be empty")

    user = await user_repository.get_user_by_username(login_data.username.strip())
    if user == None:
        raise HTTPException(status_code=400, detail="Wrong username or password")

    if not bcrypt.checkpw(login_data.password.encode("utf-8"), user.password_hash.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Wrong username or password")

    token = create_access_token({"id": user.id})
    return {"token": token}

async def register_user(user_data: auth_schema.UserCreate):
    """
    Register a new user in the system.
    
    Args:
        user_data (auth_schema.UserCreate): User registration data containing username,
                                          password, first_name, and last_name
        
    Returns:
        User: The newly created user object
        
    Raises:
        HTTPException: 400 if validation fails or username already exists
    """
    if not user_data.username.strip():
        raise HTTPException(status_code=400, detail="Username can't be empty")

    if not user_data.first_name.strip() or not user_data.last_name.strip():
        raise HTTPException(status_code=400, detail="Fist or Last name can't be empty")

    if not user_data.password.strip():
        raise HTTPException(status_code=400, detail="Password can't be empty")

    existing_user = await user_repository.get_user_by_username(user_data.username.strip())
    if existing_user != None:
        raise HTTPException(status_code=400, detail="Username already exists")

    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), salt)

    new_user = await user_repository.create_user(username=user_data.username.strip(), first_name=user_data.first_name.strip(), last_name=user_data.last_name.strip(), password_hash=hashed_password.decode("utf-8"))
    return new_user
