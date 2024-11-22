# from sqlalchemy import Column,String,Boolean,ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from config import Base
# import uuid
# from users.models import User

# class Todo(Base):
#     __tablename__ = 'todos'

#     id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     user_id: uuid.UUID = Column(UUID(as_uuid=True),ForeignKey('users.id'),nullable=False),
#     title: str = Column(String, nullable=False)
#     description: str = Column(String, nullable=False)
#     completed: bool = Column(Boolean, nullable=False)

#     users = relationship("User", back_populates="todos")

#     def __repr__(self) -> str:
#         return f"Todo: {self.title}"

from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config import Base
import uuid

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)  # Correct foreign key
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False)

    # Correct relationship to User
    user = relationship("User", back_populates="todos")  # Relationship to the User model

    def __repr__(self) -> str:
        return f"Todo: {self.title}"