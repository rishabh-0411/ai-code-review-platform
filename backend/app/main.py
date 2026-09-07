from fastapi import FastAPI
from app.core.logging_config import setup_logging
from app.api.repository import router as repository_router

setup_logging()

app = FastAPI(
    title="AI Code Review Platform",
    description="AI-powered code review backend",
    version="1.0.0",
)
app = FastAPI(
    title="AI Code Review Platform",
    description="AI-powered code review backend",
    version="1.0.0",
)

app.include_router(repository_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to AI Code Review Platform",
        "version": "1.0.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }