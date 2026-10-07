from uuid import uuid4

from app.graph.state import EvaluationState

def initialize_run(state: EvaluationState) -> dict:
    """Initialize a new evaluation run."""
    return {
        "run_id": state.get("run_id") or str(uuid4()),
        "status": "initialized",
        "current_scenario_index": 0,
        "current_scenario": None,
        "scenario_status": "not_started",
        "conversation": [],
        "turn_count": 0,
        "current_user_message": None,
        "current_bot_response": None,
        "turn_evaluation": None,
        "scenario_evaluation": None,
        "scenario_results": [],
        "final_report": None,
    }