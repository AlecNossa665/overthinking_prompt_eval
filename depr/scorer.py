class Scorer:
    def score(self, response_text: str, reference_answer: str) -> int:
        raise NotImplementedError


class ExactMatchScorer(Scorer):
    def _normalize(self, text: str) -> str:
        return text.strip().lower()

    def score(self, response_text: str, reference_answer: str) -> int:
        return int(self._normalize(response_text) == self._normalize(reference_answer))
