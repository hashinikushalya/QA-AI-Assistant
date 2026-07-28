import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def route_user_query(user_query: str) -> str:
   
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = f"""You are a smart classifier for a QA AI Assistant.
Analyze the user request and classify it into EXACTLY one of these two categories:
1. "TESTCASE" - If the user is asking to generate test cases, write test scenarios, or analyze requirements for test cases.
2. "QA_KNOWLEDGE" - If the user is asking general QA/Software Testing questions, definitions, concepts (e.g., STLC, SDLC, BVA, Smoke testing, Selenium, ISTQB).

User Request: "{user_query}"

Respond with ONLY one word: either "TESTCASE" or "QA_KNOWLEDGE". Do not add any punctuation or other text.
"""
    response = llm.invoke(prompt)
    intent = response.content.strip().upper()
    
    if "TESTCASE" in intent:
        return "TESTCASE"
    return "QA_KNOWLEDGE"