import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from rag.vectorstore import get_retriever

load_dotenv()

def answer_qa_question(question: str) -> tuple[str, list]:
    
    retriever = get_retriever()
    if not retriever:
        return "Vector Database is empty or not initialized properly.", []
    
    # Retrieve relevant document chunks
    docs = retriever.invoke(question)
    context_text = "\n\n---\n\n".join([doc.page_content for doc in docs])
    sources = [f"Source: {doc.metadata.get('source', 'Unknown')} (Page {doc.metadata.get('page', 0) + 1})" for doc in docs]
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = f"""You are an Expert ISTQB-certified Software Testing Tutor and QA Lead.
Answer the user's question accurately using ONLY the provided document context below.
If the context doesn't contain enough information, use your general QA knowledge but state that clearly.

Context from Documents:
{context_text}

Question: "{question}"

Provide a structured, easy-to-read explanation with points and examples where necessary.
"""
    response = llm.invoke(prompt)
    return response.content, list(set(sources))
