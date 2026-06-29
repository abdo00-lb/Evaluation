import time
import csv
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.graph import build_graph
from app.memory import SimpleMemory
from app.tools import load_vectorstore
import app.nodes as nodes

load_dotenv()

def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    vectorstore = load_vectorstore()
    memory = SimpleMemory()
    app = build_graph(llm, vectorstore, memory, nodes)

    questions = load_questions("evaluation/questions_simple.txt") + load_questions("evaluation/questions_complex.txt")

    with open("outputs/evaluation_results.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["question", "response_time_sec", "retrieved_docs_count", "answer_preview"])

        for q in questions:
            state = {
                "question": q,
                "rewritten_question": "",
                "retrieved_docs": [],
                "selected_tool": "",
                "answer": "",
                "memory": [],
                "messages": [],
                "need_retrieval": False,
                "evaluation_note": ""
            }

            start = time.time()
            result = app.invoke(state)
            elapsed = round(time.time() - start, 2)

            writer.writerow([
                q,
                elapsed,
                len(result["retrieved_docs"]),
                result["answer"][:150]
            ])

if __name__ == "__main__":
    main()