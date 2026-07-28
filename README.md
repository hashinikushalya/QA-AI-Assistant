#  Agentic QA AI Assistant

> A Multi-Agent AI System for Quality Assurance Engineers & Software Testers built using **Streamlit, Multi-Agent Architecture, RAG, ChromaDB, Groq LLM, PyTorch, and Transformers**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-success)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

#  Project Overview

**Agentic QA AI Assistant** is a specialized Multi-Agent AI application designed to help Quality Assurance (QA) engineers, test automation engineers, and software testers with automated test case generation, QA concepts explanation, defect identification, and intelligent documentation search using Retrieval-Augmented Generation (RAG).

Instead of manually crafting test scenarios or searching through endless ISTQB syllabi and testing guidelines, users can paste requirements or ask questions to receive structured, high-quality QA responses.

---

#  Features

-  **Smart Intent Routing:** Automatically directs queries to specialized QA agents.
-  **Automated Test Case Generation:** Generates comprehensive test cases (ID, Scenario, Steps, Test Data, Expected Results, Categories).
-  **QA Knowledge Base Search (RAG):** Context-aware searching over uploaded ISTQB and testing PDF documentation.
-  **AI Review & Polishing:** Validates and formats responses into clear, ready-to-use Markdown tables.
-  **Modern Dark UI:** Glassmorphism UI with seamless full-screen layout and live active agent execution tracking.
-  **Dynamic Source Attribution:** Shows precise PDF source references for answers derived from the knowledge base.

---

#  Multi-Agent Architecture
                   User
                    │
               Streamlit UI
                    │
               Router Agent
                    │
   ┌────────────────┴────────────────┐
   ▼                                 ▼
Test Case Agent               QA Knowledge Agent (RAG)
(Generates Scenarios)          (Searches ChromaDB Vector Store)
     │                                 │
     └────────────────┬────────────────┘
                      ▼
                 Review Agent
             (Refines & Formats Output)
                      │
                Final Response

---

# Agent Overview

| Agent | Responsibility |
| :--- | :--- |
| **Router Agent** | Analyzes user query intent (`TESTCASE` vs `QA_KNOWLEDGE`) |
| **Test Case Agent** | Generates detailed test scenarios, steps, test data, and expected results |
| **QA Knowledge Agent** | Performs vector search in ChromaDB using RAG over reference PDFs |
| **Review Agent** | Reviews, validates quality, and structures final output into clean tables |

---

# Knowledge Base

The assistant uses ChromaDB vector store containing foundational and advanced software testing documentation.

Loaded reference documents include:

- ISTQB CTFL Syllabus v4.0.1
- Software Testing Techniques & Methodologies
- ISTQB Advanced Level Test Analyst & Technical Test Analyst Syllabi
- ISTQB Test Automation Engineer & Test Manager Guides
- OWASP Web Security Testing Guide
- Agile Testing & Scrum Guidelines
- PyTest & Automation Documentation

---

#  Technologies Used

## Frontend
- Streamlit

## Backend
- Python 3.10+

## AI Framework & RAG
- Custom Multi-Agent Pipeline
- LangChain / Vector Store Integration

## Large Language Model
- Groq (Llama 3)

## Vector Database & Embeddings
- ChromaDB
- PyTorch & Torchvision
- HuggingFace / Transformers

## Document Loader
- PyPDF / LangChain Document Loaders

---

#  Project Structure

```text
qa-ai-assistant/
│
├── agents/
│   ├── router.py               # Intent classification agent
│   ├── testcase_agent.py       # Test case generation logic
│   ├── rag_agent.py            # RAG vector store query engine
│   └── review_agent.py         # Output refining & formatting agent
│
├── data/
│   └── pdfs/                   # Loaded PDF knowledge base for RAG
│
├── app.py                      # Main Streamlit UI application
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation

Installation
Clone the repository

Bash
git clone [https://github.com/hashinikushalya/QA-AI-assistant.git](https://github.com/hashinikushalya/QA-AI-assistant.git)
Navigate to project directory

Bash
cd QA-AI-assistant
Create virtual environment

Bash
python -m venv venv
Activate virtual environment

Windows:

Bash
venv\Scripts\activate
macOS / Linux:

Bash
source venv/bin/activate
Install dependencies

Bash
pip install -r requirements.txt
pip install torch torchvision

Environment Variables
Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=your_groq_api_key_here

Run the Project
Bash
streamlit run app.py

Example Prompts
Plaintext
# QA Concept Enquiries:
- "What is the difference between Severity and Priority?"
- "Explain Boundary Value Analysis according to ISTQB."
- "What are the 7 testing principles?"

# Test Case Generation Requests:
- "Generate test cases for a user login feature with email and password."
- "Generate test cases for a file upload component (Max size 5MB, PDF only)."

Developer
Hashini Kushalya

GitHub: https://github.com/hashinikushalya

License
This project is open-source and developed for educational and portfolio demonstration purposes under the MIT License.