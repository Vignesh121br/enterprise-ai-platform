from fastapi import APIRouter

from app.models import ChatRequest
from app.services import ai_service

router = APIRouter()


@router.get("/api/status")
async def status():
    return {
        "application": "Enterprise AI Platform",
        "status": "running",
        "version": "0.1.0"
    }


@router.post("/api/chat")
async def chat(request: ChatRequest):
    return await ai_service.chat(
        request.message,
        request.session_id
    )
