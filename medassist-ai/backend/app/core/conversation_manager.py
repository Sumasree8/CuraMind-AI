conversation_state = {}

def get_next_question(user_id, symptom):

    questions = {
        "headache": [
            "Is the pain sharp or dull?",
            "Is it on one side or both sides of your head?",
            "How long have you had the headache?"
        ]
    }

    if user_id not in conversation_state:
        conversation_state[user_id] = 0

    step = conversation_state[user_id]

    if step < len(questions[symptom]):
        question = questions[symptom][step]
        conversation_state[user_id] += 1
        return question

    return None
