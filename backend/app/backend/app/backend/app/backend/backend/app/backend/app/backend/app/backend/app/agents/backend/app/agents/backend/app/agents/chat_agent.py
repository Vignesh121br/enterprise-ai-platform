from app.agents.base_agent import BaseAgent
from app.services import ai_service


class ChatAgent(BaseAgent):

    def __init__(self):
        super().__init__("ChatAgent")

    async def run(self, query: str):
        return await ai_service.chat(query)
