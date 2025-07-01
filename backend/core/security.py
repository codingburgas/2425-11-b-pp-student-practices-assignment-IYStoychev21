from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

SECRET_KEY = os.environ["JWT_SECRET"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30  # 30 days

def create_access_token(data: dict):
    """
    Create a JWT access token with expiration time.
    
    Args:
        data (dict): Dictionary containing the payload data to encode in the token.
                    Typically contains user ID and other user information.
    
    Returns:
        str: Encoded JWT token string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """
    Decode and validate a JWT access token.
    
    Args:
        token (str): The JWT token string to decode
    
    Returns:
        int: The user ID extracted from the token payload
        
    Raises:
        JWTError: If the token is invalid, expired, or malformed
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("id")
        if not id:
            return None

        return int(id)
    except JWTError:
        raise JWTError
