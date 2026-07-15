from fastapi import FastAPI

from app.api import router
from app.health import health_check

app = FastAPI(
    title="Enterprise AI Platform",
    version="0.1.0",
    description="Production AI Platform"
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "application": "Enterprise AI Platform",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    return health_check()
