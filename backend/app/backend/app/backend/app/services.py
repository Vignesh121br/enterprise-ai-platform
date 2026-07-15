from app.logger import logger
from app.utils import generate_session_id


class AIService:

    async def chat(self, message: str, session_id: str | None = None):

        if session_id is None:
            session_id = generate_session_id()

        logger.info(f"Incoming message: {message}")

        return {
            "response": f"You said: {message}",
            "session_id": session_id,
            "model": "demo-model"
        }


ai_service = AIService()
