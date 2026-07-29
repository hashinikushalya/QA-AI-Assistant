import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from rag.vectorstore import get_retriever

load_dotenv()

def answer_qa_question(question: str) -> tuple[str, list]:
    """
    RAG Agent to search ChromaDB vector store and answer QA queries using Groq LLM.
    Returns a tuple of (response_text, unique_sources_list).
    """
    
    retriever = get_retriever()
    if not retriever:
        return "Vector Database is empty or not initialized properly. Please check your data/pdfs folder.", []

    
    try:
        if hasattr(retriever, "invoke"):
            docs = retriever.invoke(question)
        else:
            docs = retriever.get_relevant_documents(question)
    except Exception as e:
        return f"Error retrieving documents from Vector Store: {str(e)}", []

    if not docs:
        context_text = "No relevant context found in uploaded documents."
        sources = []
    else:
        context_text = "\n\n---\n\n".join([doc.page_content for doc in docs])
        
        # Build clean source references
        sources = []
        for doc in docs:
            src_name = doc.metadata.get('source') or doc.metadata.get('file_path') or 'PDF Document'
            page_num = doc.metadata.get('page', 0) + 1
            # Clean path to only keep filename
            file_name = os.path.basename(src_name)
            sources.append(f"{file_name} (Page {page_num})")

    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "GROQ_API_KEY is missing in your environment variables/secrets.", []

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        groq_api_key=api_key
    )

    
    prompt = f"""You are an Expert ISTQB-certified Software Testing Tutor and QA Lead.
Answer the user's question accurately using the provided document context below.
If the context contains the answer, base your response strictly on it. 
If the context doesn't contain enough information, use your general QA knowledge but state that clearly.

Context from Documents:
{context_text}

Question: "{question}"

Provide a structured, professional, and easy-to-read explanation with points and examples where necessary.
"""

    
    try:
        response = llm.invoke(prompt)
        unique_sources = list(set(sources))
        return response.content, unique_sources
    except Exception as e:
        return f"Error generating response from Groq LLM: {str(e)}", []
