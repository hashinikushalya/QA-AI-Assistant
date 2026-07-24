import os
from langchain_community.vectorstores import Chroma
from rag.loader import load_pdf_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model

PERSIST_DIR = "data/chroma_db"

def initialize_vector_store():
    embeddings = get_embedding_model()
    
    if os.path.exists(PERSIST_DIR) and len(os.listdir(PERSIST_DIR)) > 0:
        print("Loading existing Vector Database...")
        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embeddings
        )
        return vectorstore

    print("Creating new Vector Database from PDFs...")
    docs = load_pdf_documents()
    if not docs:
        print("No PDFs found in data/pdfs folder!")
        return None
        
    chunks = split_documents(docs)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    print("Vector Database created successfully!")
    return vectorstore

def get_retriever():
    vectorstore = initialize_vector_store()
    if vectorstore:
        return vectorstore.as_retriever(search_kwargs={"k": 3})
    return None