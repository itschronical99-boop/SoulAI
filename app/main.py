from fastapi import FastAPI

app = FastAPI(
    title="SoulAI API",
    version="1.0.0",
    description="Backend for SoulAI"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to SoulAI 🚀",
        "status": "Running Successfully"
    }