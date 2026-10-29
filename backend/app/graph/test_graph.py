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


assert result["status"] == "target_response_received"
assert result["current_user_message"]
assert result["current_bot_response"]
assert result["turn_count"] == 1
assert len(result["conversation"]) == 2

assert result["conversation"][0].role == "user"
assert result["conversation"][1].role == "assistant"

print(f"User: {result['conversation'][0].content}")
print(f"Chatbot: {result['conversation'][1].content}")
print(f"Turn count: {result['turn_count']}")
