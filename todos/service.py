from datetime import datetime
from fastapi import Depends, HTTPException, status
from .models import Todo
from .schemas import TodoCreate, TodoUpdate, TodoList
from sqlalchemy.sql import select
import uuid
from sqlalchemy.ext.asyncio.session import AsyncSession
from config import get_db
from users.utils.auth_service import oauth2_scheme, verify_token
from users.models import User

async def get_current_user(token: str = Depends(oauth2_scheme),db: AsyncSession = Depends(get_db)):
    async with db as session:
        user = verify_token(token)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        username = user.get("sub")
        result = await session.execute(select(User).filter(User.username == username))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

class TodoService:
    async def get_all_todos(self,db: AsyncSession = get_db()):
        async with db as session:
            statement = select(Todo)
            result = await session.execute(statement)
            todos = result.scalars().all()
            return todos
        
    async def get_todo_by_id(self, todo_id: uuid.UUID, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(statement)
            todo = result.scalars().first()
            return todo
        
    async def create_todo(self, todo: TodoCreate,db: AsyncSession = get_db()):
        async with db as session:
            todo_data = todo.model_dump()
            new_todo = Todo(**todo_data)
            session.add(new_todo)
            await session.commit()
            await session.refresh(new_todo)
            return new_todo
        
    async def update_todo(self, todo_id: uuid.UUID, todo: TodoUpdate, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(statement)
            existing_todo = result.scalars().first()
            if existing_todo is not None:
                todo_data = todo.model_dump()
                for key, value in todo_data.items():
                    setattr(existing_todo, key, value)
                await session.commit()
                return existing_todo
            return None
    
    async def delete_todo(self, todo_id: uuid.UUID, db: AsyncSession = get_db()):
        async with db as session:
            statement = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(statement)
            todo = result.scalars().first()
            if todo is not None:
                await session.delete(todo)
                await session.commit()
                return todo
            return None
        
    


