from uuid import uuid4



from app.graph.state import EvaluationState
from app.llm.gemini import get_gemini_provider
from app.models.evaluation import TestPlan
from app.prompts.planner import build_planner_prompt
from app.config import get_settings



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



def validate_plan(state: EvaluationState) -> dict:
    """Validate and normalize a generated test plan."""

    settings = get_settings()
    plan = state.get("test_plan")

    if plan is None:
        raise ValueError("Test plan is missing.")

    errors: list[str] = []

    if not plan.objective.strip():
        errors.append("The plan objective cannot be empty.")

    if not plan.scenarios:
        errors.append("The plan must contain at least one scenario.")

    if len(plan.scenarios) > settings.max_scenarios:
        errors.append(
            f"Plan contains {len(plan.scenarios)} scenarios; "
            f"maximum allowed is {settings.max_scenarios}."
        )

    scenario_ids = [scenario.id.strip() for scenario in plan.scenarios]

    if any(not scenario_id for scenario_id in scenario_ids):
        errors.append("Every scenario must have a non-empty ID.")

    if len(scenario_ids) != len(set(scenario_ids)):
        errors.append("Scenario IDs must be unique.")

    for scenario in plan.scenarios:
        if not scenario.name.strip():
            errors.append(f"{scenario.id}: name cannot be empty.")

        if not scenario.description.strip():
            errors.append(f"{scenario.id}: description cannot be empty.")

        if not scenario.persona.strip():
            errors.append(f"{scenario.id}: persona cannot be empty.")

        if not scenario.goal.strip():
            errors.append(f"{scenario.id}: goal cannot be empty.")

        if not scenario.expected_behaviour:
            errors.append(
                f"{scenario.id}: expected behaviour cannot be empty."
            )

        if not scenario.evaluation_criteria:
            errors.append(
                f"{scenario.id}: evaluation criteria cannot be empty."
            )

    if not plan.global_evaluation_criteria:
        errors.append("Global evaluation criteria cannot be empty.")

    if plan.max_turns_per_scenario < 1:
        errors.append("Maximum turns per scenario must be at least 1.")

    if errors:
        raise ValueError(
            "Test plan validation failed:\n- " + "\n- ".join(errors)
        )

    # Execution limits come from configuration, not the LLM.
    effective_max_turns = min(
        plan.max_turns_per_scenario,
        settings.max_turns_per_scenario,
    )

    if len(plan.scenarios) * effective_max_turns > settings.max_total_turns:
        raise ValueError(
            "The plan exceeds the configured total-turn budget."
        )

    # Normalize the plan to the enforced turn limit.
    validated_plan = plan.model_copy(
        update={"max_turns_per_scenario": effective_max_turns}
    )

    return {
        "test_plan": validated_plan,
        "max_turns": effective_max_turns,
        "status": "plan_validated",
    }
