from app.agents.supervisor import supervisor


class AgentWorkflow:

    async def execute(self, query):

        return await supervisor.execute(query)


workflow = AgentWorkflow()
