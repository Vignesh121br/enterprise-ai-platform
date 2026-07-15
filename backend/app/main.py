from fastapi import FastAPI

from app.api import router
from app.health import health_check
from app.middleware import request_timer

app = FastAPI(
    title="Enterprise AI Platform",
    version="0.1.0",
    description="Production Enterprise AI Platform"
)

app.middleware("http")(request_timer)

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
