from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    PROJECT_NAME: str = "Enterprise AI Platform"
    VERSION: str = "0.1.0"

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/enterprise_ai"
    )

    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379"
    )


settings = Settings()
