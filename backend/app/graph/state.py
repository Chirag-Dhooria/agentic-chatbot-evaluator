from typing import TypedDict

from app.models.evaluation import (
    FinalReport,
    Message,
    ScenarioEvaluation,
    TargetConfig,
    TestPlan,
    TestScenario,
    TurnEvaluation,
)

class EvaluationState(TypedDict):

    run_id: str 
    status: str

    target_config: TargetConfig

    objective: str

    test_plan: TestPlan | None
    current_scenario_index: int

    current_scenario: TestScenario | None
    scenario_status: str

    conversation: list[Message]
    turn_count: int
    max_turns: int

    turn_evaluation: TurnEvaluation | None
    scenario_evaluation: ScenarioEvaluation | None

    scenario_results: list[ScenarioEvaluation]

    final_report: FinalReport | None