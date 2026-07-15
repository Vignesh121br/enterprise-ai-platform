from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api import router

app = FastAPI(
    title="Enterprise AI Platform",
    version="0.1.0",
    description="Enterprise AI Platform"
)

app.include_router(router)


@app.get("/")
async def home():
    return {
        "application": "Enterprise AI Platform",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    return JSONResponse(
        {
            "status": "healthy"
        }
    )
