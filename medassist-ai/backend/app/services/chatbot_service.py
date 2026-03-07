import json
from app.utils.vector_search import keyword_search
from app.core.safety_filter import is_safe, doctor_prep_list
from app.core.red_flag_detector import detect_red_flag
from app.core.conversation_manager import get_next_question
from app.core.symptom_mapper import detect_symptom


# Load knowledge base
with open("app/data/medical_knowledge.json") as f:
    knowledge_base = json.load(f)


def get_response(user_query: str):

    # Safety check
    if not is_safe(user_query):
        return doctor_prep_list()

    # Emergency detection
    if detect_red_flag(user_query):
        return {
            "type": "emergency",
            "message": "This symptom may require immediate medical attention. Please contact emergency services or seek urgent care."
        }

    # Conversational follow-up
    symptom=detect_symptom(user_query)
    if symptom:
        question = get_next_question("default_user", symptom)
        if question:
            return {
                "type":"Followup_question",
                "question":question
            }

    # Search knowledge base
    result = keyword_search(user_query, knowledge_base)

    if result:
        return result

    return {
        "message": "I’m sorry, I don’t have information about that. Please consult a healthcare professional."
    }
