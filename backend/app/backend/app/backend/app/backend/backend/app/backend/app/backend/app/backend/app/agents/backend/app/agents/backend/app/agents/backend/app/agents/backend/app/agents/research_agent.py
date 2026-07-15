from app.agents.base_agent import BaseAgent
from app.services import ai_service
from app.retriever import retriever


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("ResearchAgent")

    async def run(self, query: str):

        documents = retriever.search(query)

        answer = await ai_service.chat(query)

        return {
            "documents": documents,
            "answer": answer
        }
