from app.graph.graph import build_graph
from app.models.evaluation import TargetConfig


graph = build_graph()

initial_state = {
    "run_id": "",
    "status": "created",
    "target_config": TargetConfig(type="mock"),
    "objective": "Test whether a chatbot handles customer support requests correctly.",
    "test_plan": None,
    "current_scenario_index": 0,
    "current_scenario": None,
    "scenario_status": "not_started",
    "conversation": [],
    "turn_count": 0,
    "max_turns": 5,
    "current_user_message": None,
    "current_bot_response": None,
    "turn_evaluation": None,
    "scenario_evaluation": None,
    "scenario_results": [],
    "final_report": None,
}

result = graph.invoke(initial_state)

print("Graph execution successful")
print(f"Run ID: {result['run_id']}")
print(f"Status: {result['status']}")
