from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.chat_services import generate_reply

router = APIRouter()

@router.post("/chat")
def chat(data: ChatRequest):
    return generate_reply(data.message)