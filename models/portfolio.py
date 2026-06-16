from sqlalchemy import Column, Integer, String, Text, ARRAY, DateTime
from sqlalchemy.sql import func
from .base import Base

class PortfolioProject(Base):
    __tablename__ = "portfolio_projects"
    
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(255), nullable=False)
    industry = Column(String(255))
    skills = Column(ARRAY(String))
    technologies = Column(ARRAY(String))
    problem = Column(Text)
    solution = Column(Text)
    results = Column(Text)
    proposal_keywords = Column(ARRAY(String))
    project_url = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
