from fastapi import APIRouter

from app.routes import router as api_router

router = APIRouter()

router.include_router(api_router)
