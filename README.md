<div align="center">

# 🧠 CuraMind AI

### A safety-first medical information assistant that informs without diagnosing.

*Turning "Dr. Google" anxiety into calm, structured, doctor-ready guidance.*

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.x-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validated-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-UI-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#-license)
[![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen.svg)](#-roadmap)

</div>

---

## 📖 Overview

**CuraMind AI** is a responsible health-information chatbot. Instead of guessing diagnoses, it routes every user message through a deliberate **multi-stage safety pipeline** before answering from a curated medical knowledge base.

The guiding principle is simple: **be helpful, but never replace a doctor.** Every layer of the architecture is built to protect the user — blocking medication advice, escalating emergencies, and always pointing back to a licensed professional.

> ⚠️ CuraMind AI is an **educator, not a doctor**. It is for general information only and is not a substitute for professional medical advice, diagnosis, or treatment.

---

## ✨ Key Features

| Feature | What it does |
| --- | --- |
| 🛡️ **Safety Filter** | Blocks requests for dosages, prescriptions, or specific medicines — the bot never tells you what to take. |
| 🚨 **Emergency Red-Flag Detection** | Recognizes critical symptoms (chest pain, difficulty breathing, stroke signs) and immediately advises urgent care. |
| 💬 **Conversational Follow-ups** | Asks intelligent clarifying questions (e.g. *"Is the pain sharp or dull?"*) to better understand the symptom. |
| 🗺️ **Symptom Mapping** | Normalizes natural language ("my head hurts", "migraine") to canonical symptoms. |
| 📚 **Curated Knowledge Base** | Answers from a structured, human-verified JSON library — facts, not hallucinations. |
| 📝 **Doctor-Visit Prep** | When it can't safely answer, it hands the user a checklist to prepare for a real appointment. |
| ⚡ **Lightweight & Fast** | Pure-Python FastAPI backend with zero heavyweight ML dependencies — runs anywhere. |

---

## 🏗️ Architecture

CuraMind processes every message through an ordered decision pipeline. **Safety always runs first.**

