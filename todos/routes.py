from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from config import get_db
# from .models import Todo
from .schemas import TodoCreate, TodoUpdate, TodoList, TodoModel
from .service import TodoService, get_current_user

router = APIRouter()
service = TodoService()

@router.get("/", response_model=TodoList)
async def get_all_todos(db: AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    todos = await service.get_all_todos(db)
    return {"todos": todos}

@router.get("/{todo_id}", response_model=TodoModel)
async def get_todo_by_id(todo_id: str, db: AsyncSession = Depends(get_db)):
    todo = await service.get_todo_by_id(todo_id, db)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=TodoModel)
async def create_todo(
    todo: TodoCreate, 
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_todo = await service.create_todo(todo, db,current_user)
    return new_todo

@router.patch("/{todo_id}", response_model=TodoModel)
async def update_todo(todo_id: str, todo: TodoUpdate, db: AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    updated_todo = await service.update_todo(todo_id, todo, db, current_user)
    if updated_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str, db: AsyncSession = Depends(get_db),current_user = Depends(get_current_user)):
    deleted_todo = await service.delete_todo(todo_id, db,current_user)
    if deleted_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return {"message": "Todo deleted successfully"}