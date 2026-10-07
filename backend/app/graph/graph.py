from langgraph.graph import END, START, StateGraph

from app.graph.nodes import initialize_run
from app.graph.state import EvaluationState


def build_graph():
    graph = StateGraph(EvaluationState)

    graph.add_node("initialize_run", initialize_run)

    graph.add_edge(START, "initialize_run")
    graph.add_edge("initialize_run", END)

    return graph.compile()