from genspark.ai import get_ai
from genspark.planner.prompts import SYSTEM_PROMPT
from genspark.utils.json_utils import extract_json


USER_PROMPT = """
Generate ONE completely original viral AI video concept.

Rules:

- Return ONLY valid JSON.
- No markdown.
- No explanations.
- No notes.

Format:

{
    "title": "Concept title"
}
"""


class ConceptPlanner:

    def __init__(self):

        self.ai = get_ai()

    def generate(self):

        last_error = None

        for attempt in range(5):

            print(
                f"Concept attempt {attempt + 1}/5"
            )

            response = ""

            try:

                response = self.ai.generate(
                    SYSTEM_PROMPT,
                    USER_PROMPT,
                )

                data = extract_json(
                    response
                )

                if "title" not in data:
                    raise ValueError(
                        "Concept title missing."
                    )

                return data

            except Exception as e:

                print("=" * 80)
                print(response)
                print("=" * 80)
                print(e)

                last_error = e

        raise RuntimeError(
            f"Concept generation failed: {last_error}"
        )