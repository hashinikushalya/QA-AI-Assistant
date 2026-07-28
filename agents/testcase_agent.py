import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def generate_test_cases(requirement: str) -> str:
    

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = f"""You are an Expert QA Automation & Manual Test Engineer.
Generate comprehensive test cases for the following feature/requirement:

Requirement:
"{requirement}"

Provide the test cases in a clear Markdown table or structured format including:
- Test Case ID
- Test Scenario
- Test Steps
- Test Data
- Expected Result
- Category (Positive / Negative / Boundary)

Include Positive Cases, Negative Cases, and Edge/Boundary Cases.
"""
    response = llm.invoke(prompt)
    return response.content