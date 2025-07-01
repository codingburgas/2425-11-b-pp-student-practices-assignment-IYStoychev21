from pydantic import BaseModel

class Login(BaseModel):
    """
    Schema for user login credentials.
    
    Attributes:
        username (str): User's unique username
        password (str): User's password (plain text, will be hashed)
    """
    username: str
    password: str

class UserCreate(BaseModel):
    """
    Schema for user registration data.
    
    Attributes:
        username (str): User's unique username
        first_name (str): User's first name
        last_name (str): User's last name
        password (str): User's password (plain text, will be hashed)
    """
    username: str
    first_name: str
    last_name: str
    password: str
