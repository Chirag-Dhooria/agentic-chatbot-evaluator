from app.graph.graph import build_graph
from app.models.evaluation import TargetConfig


graph = build_graph()

initial_state = {
    "run_id": "",
    "status": "created",
    "target_config": TargetConfig(type="mock"),
    "objective": (
        "Evaluate whether a customer support chatbot handles "
        "refund requests correctly."
    ),
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

print("\nGraph execution successful")
print(f"Run ID: {result['run_id']}")
print(f"Status: {result['status']}")


assert result["status"] == "user_message_generated"
assert result["scenario_status"] == "in_progress"
assert result["current_scenario"] is not None
assert result["current_user_message"]
assert result["current_user_message"].strip()
assert result["conversation"] == []
assert result["turn_count"] == 0

print(f"Scenario: {result['current_scenario'].name}")
print(f"Status: {result['status']}")
print(f"Generated user message: {result['current_user_message']}")
print(f"Turn count: {result['turn_count']}")
