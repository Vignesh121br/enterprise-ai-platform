from fastapi import APIRouter

from app.routes.chat import router as chat_router
from app.routes.health import router as health_router
from app.routes.ingestion import router as ingestion_router
from app.routes.agents import router as agent_router

router = APIRouter()

router.include_router(chat_router)

router.include_router(agent_router)

router.include_router(ingestion_router)

router.include_router(health_router)
