from openai import OpenAI

from app.config import settings

client = None

if settings.OPENAI_API_KEY:
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
