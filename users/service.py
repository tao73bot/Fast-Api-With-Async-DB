from datetime import timedelta

from fastapi.responses import JSONResponse
from passlib.hash import bcrypt
from .models import User
from .schemas import UserCreate
from sqlalchemy.sql import select
import uuid
from sqlalchemy.ext.asyncio.session import AsyncSession
from config import get_db
from .utils.auth_service import create_access_token, verify_token

def hash_password(password: str):
    return bcrypt.hash(password)

def verify_password(password: str, hash_password: str):
    return bcrypt.verify(password, hash_password)



class UserService:
    async def get_user_by_email(self, email:str, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(User).where(User.email == email)
            result = await session.execute(statement)
            user = result.scalars().first()
            return user
        
    async def get_user_by_id(self, user_id: uuid.UUID, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(User).where(User.id == user_id)
            result = await session.execute(statement)
            user = result.scalars().first()
            return user
        
    async def user_exits(self, email: str, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(User).where(User.email == email)
            result = await session.execute(statement)
            user = result.scalars().first()
            return user is not None
        
    async def create_user(self, user: UserCreate, db: AsyncSession = get_db()):
        async with db as session:
            user_data = user.model_dump()
            new_user = User(**user_data)
            new_user.hash_password = hash_password(user_data['hash_password'])
            session.add(new_user)
            await session.commit()
            return new_user
    
    async def login_user(self, email: str, password: str, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(User).where(User.email == email)
            result = await session.execute(statement)
            user = result.scalars().first()
            if user is not None:
                if verify_password(password, user.hash_password):
                    access_token = create_access_token(data={"sub": user.email, "id": str(user.id)})
                    refresh_token = create_access_token(data={"sub": user.email, "id": str(user.id)}, expires_delta=timedelta(days=1))
                    return JSONResponse(
                        content= {
                            "message": "Login successful",
                            "access_token": access_token,
                            "refresh_token": refresh_token,
                            "user": {"email": user.email, "id": str(user.id)}
                        }
                    )
                

    
    async def logout_user(self, token: str, db: AsyncSession = get_db()):
        async with db as session:
            user = verify_token(token)
            if user is None:
                return JSONResponse(content={"message": "Invalid token"})
            return JSONResponse(content={"message": "Logout successful"})
        