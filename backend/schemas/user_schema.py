from typing_extensions import Optional
from pydantic import BaseModel
from schemas import role_schema

class UserOut(BaseModel):
    """
    Schema for user output data (response model).
    
    Used when returning user information in API responses.
    Excludes sensitive data like password hashes.
    
    Attributes:
        id (int): User's unique identifier
        username (str): User's unique username
        first_name (str): User's first name
        last_name (str): User's last name
        role (role_schema.RoleOut): User's role information
    """
    id: int
    username: str
    first_name: str
    last_name: str
    role: role_schema.RoleOut

class UserUpdate(BaseModel):
    """
    Schema for user update data.
    
    Used when updating user profile information.
    All fields are optional to allow partial updates.
    
    Attributes:
        first_name (Optional[str]): Updated first name
        last_name (Optional[str]): Updated last name
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
