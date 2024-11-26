from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from config import get_db
from .schemas import EmailModel, UserCreate, UserLogin, UserResponse
from .service import UserService
from tasks import send_email
from mail import create_message, mail


router = APIRouter()
service = UserService()

@router.post('/send-email')
async def send_email(email: EmailModel):
    email = email.address
    html = "<h1>Test Email</h1>"
    subject = "Test Email"
    message = create_message(recipient=email,subject=subject,body=html)
    mail.send_message(message)

    return {"message": "Email sent"}



@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    if await service.user_exits(user.email, db):
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = await service.create_user(user, db)
    return new_user

@router.post("/login", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    if await service.user_exits(user.email, db):
        user = await service.login_user(user.email, user.password, db)
        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")