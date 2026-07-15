from app.agents.planning_agent import PlanningAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.chat_agent import ChatAgent

planner = PlanningAgent()
retriever = RetrievalAgent()
chat = ChatAgent()


async def planning_node(state):

    state["plan"] = await planner.run(state["query"])

    return state


async def retrieval_node(state):

    state["documents"] = await retriever.run(
        state["query"]
    )

    return state


async def generation_node(state):

    state["answer"] = await chat.run(
        state["query"]
    )

    return state
