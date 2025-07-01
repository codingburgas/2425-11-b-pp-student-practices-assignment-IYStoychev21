from pydantic import BaseModel

class RoleOut(BaseModel):
    """
    Schema for role output data (response model).
    
    Used when returning role information in API responses.
    
    Attributes:
        id (int): Role's unique identifier
        role_name (str): Role name (e.g., 'user', 'admin')
    """
    id: int
    role_name: str
