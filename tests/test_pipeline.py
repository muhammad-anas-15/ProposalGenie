import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from gemini_service import GeminiService
from api.pipeline import PipelineOrchestrator

class MockVectorStore:
    def __init__(self):
        pass
    def search_projects(self, query, top_k=3):
        return [
            {
                "content": "Client needed a microservices migration.",
                "metadata": {"project_name": "Retail APIs", "project_url": "https://example.com/api"}
            }
        ]

class MockGeminiService(GeminiService):
    def __init__(self):
        pass
        
    def generate_structured(self, prompt, schema, model_name):
        return schema.model_validate({
            "project_category": "Backend Engineering",
            "required_skills": ["Python", "FastAPI", "SQLAlchemy"],
            "technologies": ["Docker", "PostgreSQL"],
            "deliverables": ["API endpoints", "Database Schema"],
            "constraints": ["Must use Python 3.10+"],
            "budget_signals": ["Fixed budget $2000"],
            "experience_level": "Expert / Senior",
            "summary": "Building a fast, scalable API for a retail backend."
        })
        
    def generate_text(self, prompt, model_name):
        if "Review and refine" in prompt:
            return "Hi there, I can build your Fast retail API. I have relevant experience from my Retail APIs project. Let's chat."
        return "Generic Draft: I can do this using FastAPI. Reference: Retail APIs."

def test_pipeline():
    gemini = MockGeminiService()
    vs = MockVectorStore()
    
    # We bypass strict instantiation checks and rely on duck-typing
    pipeline = PipelineOrchestrator(gemini, vs) 
    
    result = pipeline.run(
        job_title="Need Senior Python Developer for Retail APIs",
        job_text="We need to build a FastAPI backed python app using SQLAlchemy and Docker.",
        profile_skills=["Python", "Java", "Docker", "FastAPI"]
    )
    
    print("-----------------------------------------")
    print("PIPELINE TEST RESULT")
    print("-----------------------------------------")
    print(f"Project Category: {result.analysis.project_category}")
    print(f"Matched Skills:   {result.match_result.matching_skills}")
    print(f"Match Score:      {result.match_result.match_score}%")
    print(f"Missing Skills:   {result.match_result.missing_skills}")
    print(f"Projects Retrieved: {len(result.retrieved_projects)}")
    print(f"Final Proposal:\n{result.proposal}")

if __name__ == "__main__":
    test_pipeline()
