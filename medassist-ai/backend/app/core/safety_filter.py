blocked_words = [
    "dosage",
    "medicine",
    "prescription",
    "drug dose",
    "which medicine"
]

def is_safe(query: str) -> bool:
    query = query.lower()

    for word in blocked_words:
        if word in query:
            return False

    return True

def doctor_prep_list():
    return {
        "doctor_visit_prep": [
            "Bring previous medical reports",
            "List current medications",
            "Note symptoms duration",
            "Prepare questions for doctor"
        ]
    }
