import json

from domain import ModelSpec, Task, TrialResult


class TaskRepo:
    def __init__(self, path: str):
        self.path = path

    def load_tasks(self) -> list[Task]:
        with open(self.path, "r") as f:
            raw = json.load(f)
        return [Task(**item) for item in raw]


class ModelClient:
    def __init__(self, spec: ModelSpec):
        self.spec = spec

    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class TrialRunner:
    def __init__(self, client, scorer):
        self.client = client
        self.scorer = scorer

    def run_task(self, task: Task) -> TrialResult:
        generation = self.client.generate(task.prompt)
        passed = self.scorer.score(generation.text, task.reference_answer)

        return TrialResult(
            task_id=task.task_id,
            model_name=generation.model_name,
            response_text=generation.model_name,
            passed=passed,
        )
