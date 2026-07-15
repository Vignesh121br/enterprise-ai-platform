from typing import TypedDict, List


class AgentState(TypedDict):
    query: str
    plan: dict
    documents: dict
    answer: dict
    history: List[dict]
