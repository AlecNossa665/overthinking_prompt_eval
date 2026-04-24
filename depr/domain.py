from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    task_id: str
    prompt: str
    reference_answer: str


@dataclass(frozen=True)
class TrialResult:
    task_id: str
    model_name: str
    response_text: str
    passed: int


@dataclass(frozen=True)
class ModelSpec:
    provider: str
    name: str


@dataclass(frozen=True)
class GenerationResult:
    text: str
    model_name: str
