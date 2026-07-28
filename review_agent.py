import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def review_and_refine_output(original_query: str, raw_output: str, agent_type: str) -> str:
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = f"""You are a QA Lead Reviewer.
Review and polish the following AI-generated output for quality, accuracy, professional tone, and readability.

User Query: "{original_query}"
Agent Type: {agent_type}

Raw Output:
{raw_output}

Task:
1. Ensure formatting (Markdown tables/bullet points) is perfectly structured.
2. Fix any formatting errors, duplicate points, or logical inconsistencies.
3. Keep the refined response highly useful and professional for software testers.
4. Output ONLY the polished final response.
"""
    response = llm.invoke(prompt)
    return response.content
