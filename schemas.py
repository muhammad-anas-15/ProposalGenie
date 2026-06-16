from pydantic import BaseModel, Field
from typing import List, Optional

class JobAnalysis(BaseModel):
    project_category: str
    required_skills: List[str]
    technologies: List[str]
    deliverables: List[str]
    constraints: List[str]
    budget_signals: List[str]
    experience_level: str
    summary: str

class SkillMatchResult(BaseModel):
    match_score: int = Field(ge=0, le=100)
    matching_skills: List[str]
    missing_skills: List[str]
    reasoning: str
    
class RetrievedProject(BaseModel):
    project_name: str
    problem: str
    solution: str
    results: str
    skills: List[str]
    technologies: List[str]
    project_url: Optional[str] = None
    
class PipelineResult(BaseModel):
    analysis: JobAnalysis
    match_result: SkillMatchResult
    retrieved_projects: List[RetrievedProject]
    proposal: str
