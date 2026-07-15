from fastapi import APIRouter

from app.agents.workflow import workflow
from app.models import ChatRequest

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.post("/run")
async def run_agent(request: ChatRequest):

    return await workflow.execute(
        request.message
    )
