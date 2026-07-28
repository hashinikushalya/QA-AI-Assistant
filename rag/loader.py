import os
from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_pdf_documents(pdf_folder_path="data/pdfs"):
    if not os.path.exists(pdf_folder_path):
        os.makedirs(pdf_folder_path)
        
    loader = PyPDFDirectoryLoader(pdf_folder_path)
    documents = loader.load()
    print(f"Total pages loaded: {len(documents)}")
    return documents