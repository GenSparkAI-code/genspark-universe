import json


class MockAI:

    def generate(self, prompt: str) -> str:

        return json.dumps(
            {
                "title": "The Antarctic Cave",
                "videos": [
                    {
                        "title": f"Video {i}",
                        "clips": [
                            {
                                "title": f"Scene {j}",
                                "narrative": f"Narrative {j}",
                                "camera": "Cinematic",
                                "hook": "Something shocking appears.",
                                "image_prompt": "Ultra realistic cinematic frame",
                                "video_prompt": "Realistic motion"
                            }
                            for j in range(1,5)
                        ]
                    }
                    for i in range(1,6)
                ]
            }
        )