from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Enterprise Proposal Engine"
    API_V1_STR: str = "/api/v1"
    
    # Database
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "proposal_engine_db"
    
    @property
    def sqlalchemy_database_uri(self) -> str:
        return f"postgresql+psycopg_async://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    @property
    def sync_sqlalchemy_database_uri(self) -> str:
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # LLM config
    GOOGLE_API_KEY: str = ""
    GEMINI_DEFAULT_MODEL: str = "gemini-2.5-flash"
    GEMINI_ANALYZER_MODEL: str = "gemini-2.5-flash"
    GEMINI_GENERATOR_MODEL: str = "gemini-2.5-flash"
    GEMINI_REVIEWER_MODEL: str = "gemini-2.5-flash"
    
    # Vector base
    FAISS_INDEX_PATH: str = "faiss_index"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

settings = Settings()
