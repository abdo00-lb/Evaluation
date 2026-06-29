from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    question: str
    rewritten_question: str
    retrieved_docs: List[str]
    selected_tool: str
    answer: str
    memory: List[str]
    messages: List[Dict[str, Any]]
    need_retrieval: bool
    evaluation_note: str