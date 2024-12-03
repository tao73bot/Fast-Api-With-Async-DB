from pydantic import BaseModel,EmailStr
import uuid
from typing import List

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    hash_password: str

class UserLogin(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr

    class config:
        from_attributs = True

class UserList(BaseModel):
    users: List[UserResponse]

class UserUpdate(BaseModel):
    username: str
    email: EmailStr

class UserPasswordUpdate(BaseModel):
    password: str
    new_password: str

class EmailModel(BaseModel):
    address: List[str]


class TokenResponse(BaseModel):
    access_token: str
    token_type: str