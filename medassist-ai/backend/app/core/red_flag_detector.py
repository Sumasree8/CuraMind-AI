RED_FLAG_SYMPTOMS = [
    "chest pain",
    "difficulty breathing",
    "severe bleeding",
    "stroke",
    "unconscious",
    "heart attack"
]

def detect_red_flag(query: str):

    query = query.lower()

    for symptom in RED_FLAG_SYMPTOMS:
        if symptom in query:
            return True

    return False
