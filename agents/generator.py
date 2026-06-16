from gemini_service import GeminiService
from schemas import JobAnalysis, SkillMatchResult, RetrievedProject
from core.config import settings

class ProposalGeneratorAgent:
    def __init__(self, gemini: GeminiService):
        self.gemini = gemini
        
    def generate(self, analysis: JobAnalysis, match: SkillMatchResult, projects: list[RetrievedProject]) -> str:
        projects_text = "\n".join([f"- {p.project_name}: {p.project_url}" for p in projects])
        prompt = f"""
You are an expert freelance proposal writer. Generate a personalized proposal of 150-250 words.
Structure the proposal logically:
1. Hook
2. Understanding
3. Relevant experience
4. Proposed approach
5. CTA

Do not use generic AI language or clichés like "I hope this finds you well" or "As an AI".
Reference the retrieved projects implicitly if relevant to the proposed approach or experience.

Job Summary: {analysis.summary}
Deliverables: {', '.join(analysis.deliverables)}
Required Skills matching: {', '.join(match.matching_skills)}

Retrieved Case Studies:
{projects_text}

Output the proposal text only.
"""
        return self.gemini.generate_text(prompt, model_name=settings.GEMINI_GENERATOR_MODEL)
