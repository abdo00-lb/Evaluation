from pathlib import Path

folders = [
    "app",
    "data/docs",
    "data/vectordb",
    "ingestion",
    "evaluation",
    "outputs"
]

files = [
    "requirements.txt",
    "README.md",
    "app/main.py",
    "app/graph.py",
    "app/state.py",
    "app/nodes.py",
    "app/tools.py",
    "app/prompts.py",
    "app/memory.py",
    "ingestion/ingest.py",
    "evaluation/evaluate.py",
    "evaluation/questions_simple.txt",
    "evaluation/questions_complex.txt"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("Project structure created successfully.")