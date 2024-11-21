from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.getenv('DB_URL')

# Settings class to load environment variables
class Settings(BaseSettings):
    DB_URL: str = os.getenv('DB_URL')
    jwt_secret_key: str = os.getenv('JWT_SECRET')
    jwt_algorithm: str = os.getenv('JWT_ALGORITHM')
    jwt_expires_s: int = 1800

settings = Settings()

# Create the asynchronous engine
engine = (create_async_engine(settings.DB_URL, echo=True))

# Session maker for async sessions
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

# Dependency to get the db session
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Function to initialize the database and create tables asynchronously
async def init_db():
    # Using `run_sync` to run the sync method `create_all` on the AsyncEngine
    async with engine.begin() as conn:
        # The `run_sync` method allows us to run sync methods with async engines
        await conn.run_sync(Base.metadata.create_all)
