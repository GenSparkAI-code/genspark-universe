import json
import re


def extract_json(text: str):

    text = text.strip()

    #
    # Direct JSON
    #

    try:
        return json.loads(text)

    except Exception:
        pass

    #
    # Extract first JSON object
    #

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL,
    )

    if match:

        return json.loads(
            match.group(0)
        )

    raise ValueError(
        "No valid JSON found."
    )