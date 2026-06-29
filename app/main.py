from app.graph import build_graph
from app.memory import SimpleMemory
from app.tools import load_vectorstore
import app.nodes as nodes


def main():
    vectorstore = load_vectorstore()
    memory = SimpleMemory()

    app = build_graph(vectorstore, memory, nodes)

    print("Agentic RAG for .NET & Microservices")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Question: ")
        if question.lower() == "exit":
            break

        state = {
            "question": question,
            "rewritten_question": "",
            "retrieved_docs": [],
            "selected_tool": "",
            "answer": "",
            "memory": [],
            "messages": [],
            "need_retrieval": False,
            "evaluation_note": ""
        }

        result = app.invoke(state)
        print("\nAnswer:")
        print(result["answer"])
        print("\nRetrieved documents:", len(result["retrieved_docs"]))
        print("-" * 60)


if __name__ == "__main__":
    main()