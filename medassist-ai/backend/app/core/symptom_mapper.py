symptom_map = {
    "headache": [
        "headache",
        "head pain",
        "migraine",
        "my head hurts",
        "pain in head"
    ],
    "fever": [
        "fever",
        "high temperature",
        "body temperature",
        "feeling hot"
    ],
    "cough": [
        "cough",
        "dry cough",
        "continuous cough"
    ]
}


def detect_symptom(query: str):

    query = query.lower()

    for symptom, variations in symptom_map.items():
        for word in variations:
            if word in query:
                return symptom

    return None
