import json
import logging
from typing import Type, TypeVar, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from google import genai
from google.genai import types
from pydantic import BaseModel
from core.config import settings

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)

class GeminiService:
    def __init__(self):
        self.api_key = settings.GOOGLE_API_KEY
        # If API key is empty, the Google GenAI SDK will fall back to os.environ["GEMINI_API_KEY"].
        self.client = genai.Client(api_key=self.api_key if self.api_key else None)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def generate_structured(self, prompt: str, schema: Type[T], model_name: str = settings.GEMINI_DEFAULT_MODEL) -> T:
        try:
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema.model_json_schema()
                )
            )
            return schema.model_validate_json(response.text)
        except Exception as e:
            logger.error(f"Error generating structured response from {model_name}: {e}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def generate_text(self, prompt: str, model_name: str = settings.GEMINI_DEFAULT_MODEL) -> str:
        try:
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"Error generating text response from {model_name}: {e}")
            raise
