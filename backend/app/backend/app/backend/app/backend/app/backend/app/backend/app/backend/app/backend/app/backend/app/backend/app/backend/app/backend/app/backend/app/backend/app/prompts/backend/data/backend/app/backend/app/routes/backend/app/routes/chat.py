from fastapi import APIRouter

from app.models import ChatRequest
from app.services import ai_service

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
async def chat(request: ChatRequest):

    return await ai_service.chat(
        request.message,
        request.session_id
    )
