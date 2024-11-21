from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.dialects.postgresql import UUID
from config import Base
import uuid

class Todo(Base):
    __tablename__ = 'todos'

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    completed: bool = Column(Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"Todo: {self.title}"
    
