from app.agents.base_agent import BaseAgent


class PlanningAgent(BaseAgent):

    def __init__(self):
        super().__init__("PlanningAgent")

    async def run(self, query: str):

        return {
            "goal": query,
            "steps": [
                "Understand request",
                "Retrieve information",
                "Generate response",
                "Validate answer"
            ]
        }
