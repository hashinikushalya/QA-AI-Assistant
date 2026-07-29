#  Agentic QA AI Assistant

A **Multi-Agent AI System** for **Quality Assurance Engineers** and **Software Testers**, built using **Streamlit, LangChain, ChromaDB, Groq LLM, PyTorch, and Transformers**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-success)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Live Demo

**Streamlit App**

https://app-ai-assistant-wx36xz3jwwezqyjizxu8sz.streamlit.app/

---

#  Project Overview

**Agentic QA AI Assistant** is an AI-powered assistant designed to help **QA Engineers, Software Testers, and Test Automation Engineers** perform testing-related tasks efficiently.

The application combines a **Multi-Agent Architecture** with **Retrieval-Augmented Generation (RAG)** to generate intelligent, structured, and context-aware responses for software testing activities.

Users can:

- Generate professional test cases
- Ask QA concepts and ISTQB questions
- Search testing documentation using AI
- Receive polished and structured answers
- Get source references from the knowledge base

---

#  Features

- Smart Intent Routing
- Automated Test Case Generation
- RAG-based QA Knowledge Search
- AI Review & Response Polishing
- Modern Streamlit Dark UI
- Source Attribution from PDFs
- Fast Responses using Groq LLM

---

# Multi-Agent Architecture

```
                    User
                      │
                Streamlit UI
                      │
                Router Agent
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
 Test Case Agent              QA Knowledge Agent
 (Generate Test Cases)        (RAG + ChromaDB Search)
      │                               │
      └───────────────┬───────────────┘
                      ▼
                Review Agent
        (Validate & Format Response)
                      │
                      ▼
              Final AI Response
```

---

#  Agent Responsibilities

| Agent | Responsibility |
|-------|----------------|
| Router Agent | Detects user intent and routes the query |
| Test Case Agent | Generates professional software test cases |
| QA Knowledge Agent | Retrieves relevant information from the QA knowledge base using RAG |
| Review Agent | Reviews, validates, and formats the final response |

---

# Knowledge Base

The assistant uses a ChromaDB vector database containing software testing documentation.

Included references:

- ISTQB CTFL Syllabus v4.0.1
- ISTQB Advanced Level Test Analyst
- ISTQB Technical Test Analyst
- ISTQB Test Automation Engineer
- ISTQB Test Manager
- Software Testing Techniques
- Agile Testing Guide
- Scrum Testing Guide
- OWASP Web Security Testing Guide
- PyTest Documentation

---

# Technologies Used

## Frontend

- Streamlit

## Backend

- Python 3.10+

## AI Framework

- LangChain
- Custom Multi-Agent Pipeline

## Large Language Model

- Groq (Llama 3)

## Vector Database

- ChromaDB

## Embeddings

- HuggingFace Transformers
- PyTorch

## Document Processing

- PyPDF
- LangChain Document Loaders

---

#  Project Structure

```text
qa-ai-assistant/
│
├── agents/
│   ├── router.py
│   ├── testcase_agent.py
│   ├── rag_agent.py
│   └── review_agent.py
│
├── data/
│   └── pdfs/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/hashinikushalya/QA-AI-assistant.git
```

## 2. Navigate to the Project

```bash
cd QA-AI-assistant
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If required:

```bash
pip install torch torchvision
```

---

#  Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

#  Run the Application

```bash
streamlit run app.py
```

---

#  Example Prompts

## QA Concepts

```
What is Boundary Value Analysis?

Explain Severity vs Priority.

What are the 7 Testing Principles?

Explain Smoke Testing.
```

## Test Case Generation

```
Generate test cases for a Login Page.

Generate test cases for User Registration.

Generate test cases for File Upload
(Max file size 5MB, PDF only).

Generate test cases for Forgot Password.
```

---

#  Screenshots

> Add screenshots of your application here.

Example:

```
screenshots/
    home.png

    testcase.png
    rag_search.png
```

---

#  Developer

**Hashini Kushalya**

GitHub:
https://github.com/hashinikushalya

---

#  License

This project is licensed under the **MIT License**.

Developed for educational, research, and portfolio purposes.

---

 If you found this project useful, consider giving it a **Star** on GitHub.
