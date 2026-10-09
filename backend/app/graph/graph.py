from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    initialize_run,
    plan_tests,
    select_scenario,
    validate_plan,
)
from app.graph.state import EvaluationState


def build_graph():
    graph = StateGraph(EvaluationState)

    graph.add_node("initialize_run", initialize_run)
    graph.add_node("plan_tests", plan_tests)
    graph.add_node("validate_plan", validate_plan)
    graph.add_node("select_scenario", select_scenario)

    graph.add_edge(START, "initialize_run")
    graph.add_edge("initialize_run", "plan_tests")
    graph.add_edge("plan_tests", "validate_plan")
    graph.add_edge("validate_plan", "select_scenario")
    graph.add_edge("select_scenario", END)

    return graph.compile()