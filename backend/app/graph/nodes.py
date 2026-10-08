from uuid import uuid4

from app.graph.state import EvaluationState
from app.llm.gemini import get_gemini_provider
from app.models.evaluation import TestPlan
from app.prompts.planner import build_planner_prompt



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


def plan_tests(state: EvaluationState) -> dict:
    """Generate a structured test plan from the evaluation objective."""

    provider = get_gemini_provider()

    planner = provider.structured_output(TestPlan)

    test_plan = planner.invoke(
        build_planner_prompt(state["objective"])
    )

    return {
        "test_plan": test_plan,
        "max_turns": test_plan.max_turns_per_scenario,
        "status": "plan_generated",
    }