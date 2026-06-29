from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message:str

@app.get("/")
def home():
    return {
        "message": "Welcome to SoulAI 🚀"
    }
@app.post("/chat")
def chat(data:ChatRequest):
    return{
        "user_message":data.message,
        "reply":f"You said:{data.message}"
    }