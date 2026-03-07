from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="MedAssist AI",
    description="Medical Information Chatbot API",
    version="1.0"
)
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "MedAssist AI API is running"
    }
