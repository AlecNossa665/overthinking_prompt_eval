from google import genai
from google.genai import types

from domain import GenerationResult, ModelSpec, TrialResult


class ModelClient:
    def __init__(self, spec: ModelSpec):
        self.spec = spec

    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class GoogleModelClient(ModelClient):
    def __init__(self, spec: ModelSpec, sdk_client: genai.Client):
        super().__init__(spec)
        self.sdk_client = sdk_client

        def generate(self, prompt: str) -> GenerationResult:
            config = types.GenerateContentConfig(
                temperature=self.spec.temperature,
                max_output_tokens=self.spec.max_output_tokens,
            )

            response = self.sdk_cient.models.generate_content(
                model=self.spec.model_name,
                contents=prompt,
                config=config,
            )

            return GenerationResult(text=response.text, model_name=self.spec.model_name)
