from fastapi import FastAPI

from app.routers.auth import router as auth_router

app = FastAPI(
    title="Production Authentication API",
    description="Day 26 - Production Backend Structure",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Production Authentication API is running!"
    }