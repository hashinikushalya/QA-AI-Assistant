from rag.vectorstore import initialize_vector_store

print("Starting Vector DB Initialization...")
vs = initialize_vector_store()

if vs:
    print("\nSUCCESS: PDFs loaded and Vector Database created successfully!")
else:
    print("\nFAILED: No PDFs found or error in loading.")