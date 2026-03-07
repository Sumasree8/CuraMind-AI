import os

# Root project name
PROJECT_NAME = "medassist-ai"

# Folder structure
folders = [
    f"{PROJECT_NAME}/backend/app/api",
    f"{PROJECT_NAME}/backend/app/services",
    f"{PROJECT_NAME}/backend/app/models",
    f"{PROJECT_NAME}/backend/app/core",
    f"{PROJECT_NAME}/backend/app/utils",
    f"{PROJECT_NAME}/backend/app/data",
    f"{PROJECT_NAME}/frontend/js",
    f"{PROJECT_NAME}/frontend/css",
    f"{PROJECT_NAME}/docs"
]

# Files to create
files = {
    f"{PROJECT_NAME}/backend/app/main.py": "",
    f"{PROJECT_NAME}/backend/app/api/routes.py": "",
    f"{PROJECT_NAME}/backend/app/services/chatbot_service.py": "",
    f"{PROJECT_NAME}/backend/app/models/schemas.py": "",
    f"{PROJECT_NAME}/backend/app/core/config.py": "",
    f"{PROJECT_NAME}/backend/app/core/safety_filter.py": "",
    f"{PROJECT_NAME}/backend/app/utils/vector_search.py": "",
    f"{PROJECT_NAME}/backend/app/data/medical_knowledge.json": "[]",
    f"{PROJECT_NAME}/frontend/index.html": "",
    f"{PROJECT_NAME}/frontend/js/chat.js": "",
    f"{PROJECT_NAME}/frontend/css/style.css": "",
    f"{PROJECT_NAME}/backend/requirements.txt": "",
    f"{PROJECT_NAME}/README.md": "# MedAssist AI\n",
    f"{PROJECT_NAME}/docs/architecture.md": "# Architecture Documentation\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)

print("✅ MedAssist AI project structure created successfully!")
