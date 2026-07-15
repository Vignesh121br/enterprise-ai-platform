from uuid import uuid4


class AIService:

    async def chat(self, message: str, session_id: str | None = None):
        if session_id is None:
            session_id = str(uuid4())

        return {
            "response": f"You said: {message}",
            "session_id": session_id
        }


ai_service = AIService()
