from pydantic import BaseModel,EmailStr
import uuid

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr

    class config:
        from_attributs = True
