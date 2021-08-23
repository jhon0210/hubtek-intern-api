from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from .database import Base


class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    picture = Column(String(255), nullable=False)
    is_adopted = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)

