from sqlalchemy import Column,String,Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config import Base
import uuid

class User(Base):
    __tablename__ = 'users'

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False)
    hash_password: str = Column(String, nullable=False)
    is_verified: bool = Column(Boolean, nullable=False)

    todos = relationship("Todo", back_populates="users")

    def __repr__(self) -> str:
        return f"User: {self.username}"