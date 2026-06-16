from sqlalchemy import Column, Integer, String, Text, ARRAY, DateTime
from sqlalchemy.sql import func
from .base import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    title = Column(String(255))
    bio = Column(Text)
    skills = Column(ARRAY(String))
    achievements = Column(ARRAY(Text))
    portfolio_links = Column(ARRAY(String))
    testimonials = Column(ARRAY(Text))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
