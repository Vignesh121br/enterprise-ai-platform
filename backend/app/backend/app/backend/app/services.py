from app.logger import logger
from app.prompts import SYSTEM_PROMPT
from app.utils import generate_session_id
from app.openai_client import client


class AIService:

    async def chat(self, message: str, session_id: str | None = None):

        if session_id is None:
            session_id = generate_session_id()

        logger.info(message)

        if client:

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

            answer = response.choices[0].message.content

        else:
            answer = "OpenAI API Key not configured."

        return {
            "response": answer,
            "session_id": session_id,
            "model": "gpt-4.1-mini"
        }


ai_service = AIService()
