from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
