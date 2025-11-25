from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Memory(Base):
    __tablename__ = "memories"
    id = Column(Integer, primary_key=True, index=True)
    conversation = Column(Text, nullable=False)
    summary = Column(String, nullable=True)