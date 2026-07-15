from app.agents.base_agent import BaseAgent
from app.retriever import retriever


class RetrievalAgent(BaseAgent):

    def __init__(self):
        super().__init__("RetrievalAgent")

    async def run(self, query: str):
        return retriever.search(query)
