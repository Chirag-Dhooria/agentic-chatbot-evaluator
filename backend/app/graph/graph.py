
from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    initialize_run,
    initialize_conversation,
    plan_tests,
    select_scenario,
    validate_plan,
    generate_user_message,
    call_target_chatbot,
)

from app.graph.state import EvaluationState


def build_graph():
    graph = StateGraph(EvaluationState)

    graph.add_node("initialize_run", initialize_run)
    graph.add_node("plan_tests", plan_tests)
    graph.add_node("validate_plan", validate_plan)
    graph.add_node("select_scenario", select_scenario)
    graph.add_node("initialize_conversation", initialize_conversation)
    graph.add_node("generate_user_message", generate_user_message)
    graph.add_node("call_target_chatbot", call_target_chatbot)

    graph.add_edge(START, "initialize_run")
    graph.add_edge("initialize_run", "plan_tests")
    graph.add_edge("plan_tests", "validate_plan")
    graph.add_edge("validate_plan", "select_scenario")
    graph.add_edge("select_scenario", "initialize_conversation")
    graph.add_edge("initialize_conversation", "generate_user_message")
    graph.add_edge("generate_user_message", "call_target_chatbot")
    graph.add_edge("call_target_chatbot", END)

    return graph.compile()