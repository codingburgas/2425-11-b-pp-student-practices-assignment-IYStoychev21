from pydantic import BaseModel

class RoleOut(BaseModel):
    id: int
    role_name: str
