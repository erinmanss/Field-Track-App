from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from Backend.database import Base

class Observation(Base):
    __tablename__ = "observation" # table called observation
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.now)