from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import get_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    reply = get_response(request.message)

    return ChatResponse(response=reply)
