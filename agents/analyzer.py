from gemini_service import GeminiService
from schemas import JobAnalysis
from core.config import settings
import os

class JobAnalyzerAgent:
    def __init__(self, gemini: GeminiService):
        self.gemini = gemini
        prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "job_analyzer.txt")
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.prompt_template = f.read()

    def analyze(self, job_title: str, job_text: str) -> JobAnalysis:
        full_text = f"Title: {job_title}\n\nDescription: {job_text}"
        prompt = self.prompt_template.replace("{{job_text}}", full_text)
        
        return self.gemini.generate_structured(
            prompt=prompt,
            schema=JobAnalysis,
            model_name=settings.GEMINI_ANALYZER_MODEL
        )
