from gemini_service import GeminiService
from core.config import settings

class ProposalReviewerAgent:
    def __init__(self, gemini: GeminiService):
        self.gemini = gemini

    def review(self, draft: str) -> str:
        prompt = f"""
Review and refine the following proposal draft.
1. Remove all AI clichés ("in today's fast-paced world", "delve into").
2. Ensure it is highly personalized, punchy, and under 250 words.
3. Improve readability.

Draft:
{draft}

Output the final reviewed text only.
"""
        return self.gemini.generate_text(prompt, model_name=settings.GEMINI_REVIEWER_MODEL)
