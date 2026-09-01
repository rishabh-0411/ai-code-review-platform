from fastapi import FastAPI

app = FastAPI(
    title="AI Code Review Platform",
    description="AI-powered code review backend",
    version="1.0.0",
)


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