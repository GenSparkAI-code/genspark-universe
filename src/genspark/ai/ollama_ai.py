import os
import requests


class OllamaAI:

    def __init__(
        self,
        model: str | None = None,
        url: str = "http://localhost:11434/api/chat",
    ):
        self.model = model or os.getenv(
            "OLLAMA_MODEL",
            "qwen3:8b",
        )
        self.url = url

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "stream": False,
                "think": False,
                "options": {
                    "temperature": 0.2,
                    "top_p": 0.9,
                },
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
            },
            timeout=600,
        )

        response.raise_for_status()

        return response.json()["message"]["content"]