from fastapi import APIRouter

from app.health import health_check

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
async def health():

    return health_check()
