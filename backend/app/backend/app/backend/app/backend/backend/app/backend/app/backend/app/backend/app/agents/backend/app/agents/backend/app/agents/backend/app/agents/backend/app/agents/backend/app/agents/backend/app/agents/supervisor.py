from app.agents.chat_agent import ChatAgent
from app.agents.research_agent import ResearchAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.planning_agent import PlanningAgent


class SupervisorAgent:

    def __init__(self):

        self.chat = ChatAgent()
        self.research = ResearchAgent()
        self.retrieval = RetrievalAgent()
        self.planner = PlanningAgent()

    async def execute(self, query: str):

        plan = await self.planner.run(query)

        docs = await self.retrieval.run(query)

        answer = await self.chat.run(query)

        return {
            "plan": plan,
            "documents": docs,
            "answer": answer
        }


supervisor = SupervisorAgent()
