# Agentic RAG for .NET Core and Microservices

This project is an Agentic RAG system built with LangGraph for answering technical questions about .NET Core, RabbitMQ, Clean Architecture, Domain-Driven Design, EF Core, and microservices.

## Objective

The goal of the project is to build a Retrieval-Augmented Generation system capable of:
- loading a local document base,
- preprocessing and vectorizing documents,
- retrieving relevant context,
- answering simple and complex questions,
- using a LangGraph workflow with state and memory.

## Tech Stack

- Python
- LangGraph
- LangChain
- FAISS
- Hugging Face Embeddings
- Sentence Transformers
- GitHub for source control

## Project Structure

```text
agentic-rag-dotnet-microservices/
├── app/
├── data/
│   ├── docs/
│   └── vectordb/
├── evaluation/
├── ingestion/
├── outputs/
├── bootstrap.py
├── README.md
└── requirements.txt
```

## How It Works

1. Documents are loaded from the local knowledge base.
2. The ingestion script splits documents into chunks.
3. Embeddings are generated and stored in a FAISS vector database.
4. A LangGraph workflow routes the question, retrieves context, and generates an answer.
5. A simple memory component stores previous interactions.

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## Ingestion

Run the ingestion script to build the vector database:

```bash
python ingestion/ingest.py
```

## Run the Application

```bash
python -m app.main
```

Type `exit` to stop the application.

## Example Questions

### Simple Questions
- What is ASP.NET Core?
- What is RabbitMQ used for?
- What is Clean Architecture?
- What is Domain-Driven Design?
- What is EF Core?

### Complex Questions
- What is the difference between Clean Architecture and DDD?
- When should microservices be used in an ERP system?
- How does EF Core fit into Clean Architecture?
- Why is asynchronous messaging important in distributed systems?

## Evaluation

The system was evaluated using:
- 10 simple questions,
- 10 complex questions,
- analysis of answer quality,
- response time,
- relevance of retrieved documents.

## Notes on Credentials

A GitHub token was configured during repository setup and experimentation. The final runnable version of the project relies on local embeddings and FAISS for the retrieval pipeline.

Sensitive credentials must be stored in environment variables and must not be committed to the repository.

## Deliverables

- Source code on GitHub
- Individual report PDF
- Evaluation questions and results

## Author

Abdellah