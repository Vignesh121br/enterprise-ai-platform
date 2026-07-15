from langgraph.graph import StateGraph

from app.langgraph.state import AgentState
from app.langgraph.nodes import (
    planning_node,
    retrieval_node,
    generation_node
)

builder = StateGraph(AgentState)

builder.add_node("planner", planning_node)

builder.add_node("retriever", retrieval_node)

builder.add_node("generator", generation_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "retriever")

builder.add_edge("retriever", "generator")

builder.set_finish_point("generator")

workflow = builder.compile()
