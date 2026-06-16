from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from core.config import settings
from api.pipeline import PipelineOrchestrator
from gemini_service import GeminiService
from faiss_store import LocalFAISSVectorStore
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global singleton services 
gemini_service = GeminiService()
vector_store = LocalFAISSVectorStore(settings.FAISS_INDEX_PATH)
orchestrator = PipelineOrchestrator(gemini_service, vector_store)

class AnalyzeRequest(BaseModel):
    job_title: str
    job_text: str
    profile_skills: List[str]

@app.post(settings.API_V1_STR + "/analyze")
async def analyze_job(request: AnalyzeRequest):
    result = orchestrator.run(
        job_title=request.job_title,
        job_text=request.job_text,
        profile_skills=request.profile_skills
    )
    return result.model_dump()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
