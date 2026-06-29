from langgraph.graph import StateGraph, END
from app.state import AgentState

def build_graph(vectorstore, memory, nodes_module):
    workflow = StateGraph(AgentState)

    workflow.add_node("route_question", lambda state: nodes_module.route_question(state))
    workflow.add_node("rewrite_question", lambda state: nodes_module.rewrite_question(state))
    workflow.add_node("retrieve_context", lambda state: nodes_module.retrieve_context(state, vectorstore))
    workflow.add_node("generate_answer", lambda state: nodes_module.generate_answer(state, memory))
    workflow.add_node("direct_answer", lambda state: nodes_module.direct_answer(state, memory))

    workflow.set_entry_point("route_question")

    workflow.add_conditional_edges(
        "route_question",
        lambda state: "rewrite_question" if state["need_retrieval"] else "direct_answer"
    )

    workflow.add_edge("rewrite_question", "retrieve_context")
    workflow.add_edge("retrieve_context", "generate_answer")
    workflow.add_edge("generate_answer", END)
    workflow.add_edge("direct_answer", END)

    return workflow.compile()