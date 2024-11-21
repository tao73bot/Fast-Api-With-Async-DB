from fastapi import FastAPI
from config import Base, engine, init_db
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
from todos.routes import router as todos_router

# Initialize the database
async def lifespan(app: FastAPI):
    # Run the database initialization on startup
    await init_db()
    print("Server is running")
    yield  # This ensures that FastAPI will continue running after the startup code is executed
    # Optional: Add shutdown logic here if needed (e.g., closing DB connections)
    print("Server is shutting down")


app = FastAPI(lifespan=lifespan)

app.include_router(todos_router, prefix="/todos", tags=["todos"])