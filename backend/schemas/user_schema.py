from typing_extensions import Optional
from pydantic import BaseModel
from schemas import role_schema

class UserOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    role: role_schema.RoleOut

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
