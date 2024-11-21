from sqlalchemy import Column,String,Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config import Base
import uuid

class Todo(Base):
    __tablename__ = 'todos'

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    completed: bool = Column(Boolean, nullable=False)

    users = relationship("User", back_populates="todos")

    def __repr__(self) -> str:
        return f"Todo: {self.title}"