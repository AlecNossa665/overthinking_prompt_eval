from google import genai

from domain import ModelSpec, Task
from loader import TaskRepo, TrialRunner
from model import GoogleModelClient
from scorer import Scorer

test_model = ModelSpec(provider="google", name="gemini-2.5-flash-lite")
test_client = GoogleModelClient(spec=test_model, sdk_client=genai.Client())
test_scorer = Scorer()
test_runner = TrialRunner(client=test_client, scorer=test_scorer)


task_repo = TaskRepo("tasks.json")
