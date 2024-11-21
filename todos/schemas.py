import uuid
from typing import List
from pydantic import BaseModel

class TodoModel(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    completed: bool

class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool

class TodoUpdate(BaseModel):
    title: str
    description: str
    completed: bool

class TodoList(BaseModel):
    todos: List[TodoModel]
# The Todo class is a Pydantic model that represents the Todo table in the database. It has the following fields:
