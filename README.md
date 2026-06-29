# Agentic RAG for .NET Core and Microservices Documentation

## Overview
This project implements an Agentic RAG system using LangGraph to answer technical questions about .NET Core and microservices architecture from an external knowledge base.

The system uses:
- document ingestion and chunking
- vector search with FAISS
- retrieval-augmented generation
- LangGraph-based agent workflow
- conversational memory
- graph visualization
- evaluation on simple and complex questions

## Project objective
The objective is to design and implement a complete Agentic RAG system instead of using a prebuilt agent loop. The system is built with LangGraph and follows a modular workflow with explicit state transitions.

## Domain
Technical documentation about:
- ASP.NET Core
- Clean Architecture
- Domain-Driven Design
- Entity Framework Core
- RabbitMQ
- API Gateway
- Microservices patterns

## Architecture
The graph contains the following nodes:
1. Route question
2. Rewrite question
3. Retrieve context
4. Generate answer
5. Direct answer

Decision flow:
- If the question requires retrieval, the agent rewrites the query, retrieves relevant chunks, then generates the final answer.
- Otherwise, it answers directly.

## Installation
```bash
git clone <your-repo-url>
cd agentic-rag-dotnet-microservices
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```env
OPENAI_API_KEY=your_key_here
```

## Run ingestion
```bash
python ingestion/ingest.py
```

## Run the application
```bash
python app/main.py
```

## Run evaluation
```bash
python evaluation/evaluate.py
```

## Evaluation protocol
The system is evaluated using:
- 10 simple questions
- 10 complex questions

The analysis considers:
- answer quality
- response time
- relevance of retrieved documents

## Strengths
- explicit graph control with LangGraph
- modular design
- retrieval + memory
- domain-specific knowledge base
- easy to extend with more tools

## Limitations
- depends on the quality of the document corpus
- simple memory strategy
- no reranking stage
- limited source diversity in the initial version

## Future improvements
- add reranking
- add source citation in answers
- support PDF and web loaders
- integrate hybrid search
- improve long-term memory