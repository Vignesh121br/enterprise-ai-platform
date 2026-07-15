from fastapi import APIRouter

router = APIRouter()


@router.get("/api/status")
async def status():
    return {
        "application": "Enterprise AI Platform",
        "status": "running",
        "version": "0.1.0"
    }


@router.get("/api/version")
async def version():
    return {
        "version": "0.1.0"
    }
