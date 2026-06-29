import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DOCS_PATH = "data/docs"
DB_PATH = "data/vectordb"

def load_documents():
    docs = []
    for file in os.listdir(DOCS_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DOCS_PATH, file), encoding="utf-8")
            docs.extend(loader.load())
    return docs

def main():
    raw_docs = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_documents(raw_docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)

    print(f"Ingested {len(raw_docs)} documents and created {len(chunks)} chunks.")

if __name__ == "__main__":
    main()