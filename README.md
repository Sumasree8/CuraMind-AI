🧠 CuraMind AI
Your Safe Guide to Health Awareness
"Is it a common cold or something more?" > CuraMind AI helps you understand your symptoms using verified medical data, while ensuring you stay safe by always putting professional medical advice first.

🌟 Why CuraMind AI?
In a world of "Dr. Google," it's easy to get scared by inaccurate health info (this is called Cyberchondria). CuraMind AI solves this by being a Responsible Assistant. It doesn't guess; it uses a structured knowledge base to give you facts, not fears.

🛡️ The "Safety First" Promise
Unlike general AI, CuraMind has "Guardrails":

No Prescriptions: It will never tell you what pills to take.

No Diagnosis: It explains symptoms but never "labels" you with a disease.

Emergency Detection: If you describe a life-threatening symptom (like chest pain), it stops the chat and tells you to call emergency services immediately.

🚀 How It Works (The Simple View)
You Talk: Type your symptoms in the clean, blue-themed chat box.

It Checks: The system runs your words through a Safety Filter.

It Searches: It looks into a curated Medical Knowledge Base (JSON).

It Guides: It gives you an easy-to-read explanation and suggests the next best steps for talking to a real doctor.

🛠️ Tech Stack (The Engine)
We kept it lightweight and fast so it can run anywhere:

Backend: FastAPI (Python 3.11) — The "Brain" that handles logic.

Frontend: HTML5 & Tailwind CSS — A calm, professional look.

Data: JSON — A structured library of medical facts.

💻 Quick Start for Developers
Want to run this on your machine? It takes less than 2 minutes.

1. Get the Code
Bash
git clone https://github.com/Sumasree8/CuraMind-AI.git
cd CuraMind-AI
2. Set Up Your Space
Bash
py -3.11 -m venv venv
.\venv\Scripts\activate
pip install -r backend/requirements.txt
3. Launch
Bash
uvicorn backend.app.main:app --reload
Now open frontend/index.html in your browser and start chatting!

🗺️ What's Next?
Smart Search: Moving from "Keyword matching" to "AI Meanings" (Vector DB).

Multilingual: Making health info accessible in every language.

Voice Mode: Just speak your symptoms out loud.

⚠️ A Friendly Reminder
CuraMind AI is an educator, not a doctor. This tool is for information only. If you are feeling unwell, please see a licensed medical professional.

🤝 Want to help?
I'm looking for help with:

Expanding the medical knowledge file.

Improving the "Emergency Detection" logic.

Making the UI even more accessible for elderly users.
