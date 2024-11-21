from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.dialects.postgresql import UUID
from config import Base
import uuid

class User(Base):
    __tablename__ = 'users'

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False)
    hash_password: str = Column(String, nullable=False)
    is_verified: bool = Column(Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"User: {self.username}"