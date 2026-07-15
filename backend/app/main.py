from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Enterprise AI Platform",
    description="Production-ready AI Platform",
    version="0.1.0"
)


@app.get("/")
async def home():
    return JSONResponse(
        {
            "project": "Enterprise AI Platform",
            "version": "0.1.0",
            "status": "running"
        }
    )


@app.get("/health")
async def health():
    return JSONResponse(
        {
            "status": "healthy"
        }
    )
