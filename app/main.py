from fastapi import FastAPI
from app.routes.chat import router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "SoulAI Backend Running"}

@app.get("/config")
def config():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }