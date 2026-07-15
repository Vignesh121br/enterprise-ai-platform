from fastapi import APIRouter

from app.langgraph.workflow import workflow
from app.models import ChatRequest

router = APIRouter(
    prefix="/langgraph",
    tags=["LangGraph"]
)


@router.post("/run")
async def execute(request: ChatRequest):

    result = await workflow.ainvoke(
        {
            "query": request.message,
            "history": []
        }
    )

    return result
