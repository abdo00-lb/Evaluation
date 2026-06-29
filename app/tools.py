from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def load_vectorstore(path="data/vectordb"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)


def retrieve_docs(vectorstore, query, k=2):
    docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]


def format_context(docs):
    return "\n\n".join([f"- {doc}" for doc in docs])