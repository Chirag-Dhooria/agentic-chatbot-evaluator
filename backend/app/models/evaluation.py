from datetime import datetime
from typing import Literal 

from pydantic import BaseModel 


class TargetConfig(BaseModel): 
    type: Literal["mock", "api"]
    endpoints: str | None = None
    model: str | None = None


class TestScenario(BaseModel): 
    id : str
    name: str 
    description: str

    persona: str
    goal: str

    constraints: list[str]
    expected_behaviour: list[str]

    evaluation_criteria: list[str]


class TestPlan(BaseModel): 
    objective: str
    scenarios: list[TestScenario]
    global_evaluation_criteria: list[str]
    max_turns_per_scenario: int


class Message(BaseModel): 
    role: Literal["system", "user", "assistant"]
    content: str
    timestamp: datetime | None = None


class TurnEvaluation(BaseModel):
    should_continue: bool 
    turn_progress: str 
    chatbot_behaviour: str
    detected_issues: list[str]
    next_user_strategy: str | None = None


class ScenarioEvaluation(BaseModel):
    passed: bool 
    scores: dict[str, float]
    failure_categories: list[str]
    severity: Literal["none", "low", "medium", "high", "critical"] 
    summary: str
    evidence: list[str]
    recommendation: list[str]


class FinalReport(BaseModel):
    overal_score: float
    pass_rate: float
    scenario_count: int
    passed_count: int
    failed_count: int
    failure_summary: dict[str, int]
    critical_findings: list[str]
    recommendations: list[str]
    

    
    