from genspark.ai import get_ai
from assets.characters.registry import CharacterRegistry
from genspark.models.character import CharacterState
from genspark.models.concept import Clip
from genspark.models.concept import Video
from genspark.planner.prompts import SYSTEM_PROMPT
from genspark.utils.json_utils import extract_json


class VideoPlanner:

    def __init__(self):

        self.ai = get_ai()

        self.registry = (
            CharacterRegistry()
        )

    def generate(
        self,
        concept_title: str,
        video_number: int,
    ) -> Video:

        prompt = f"""
Concept

{concept_title}

Generate ONLY Video {video_number}.

Return ONLY valid JSON.

Generate EXACTLY 4 clips.

Each clip is exactly 3 seconds.

Each clip must naturally continue from the previous clip.

Every clip MUST contain

title
narrative
camera
hook
image_prompt
video_prompt
characters

General Rules

- Only use existing characters.
- A character may disappear if not present in the scene.
- Every visible character MUST be listed.
- Never invent new expressions.
- Never invent new poses.
- Never invent new powers.
- Never invent new costumes.
- Use ONLY the values listed below.

==================================================
AVAILABLE CHARACTERS
==================================================

{self.registry.planner_description()}

==================================================
OUTPUT FORMAT
==================================================

{{
    "title":"...",
    "clips":[
        {{
            "title":"...",
            "narrative":"...",
            "camera":"...",
            "hook":"...",
            "image_prompt":"...",
            "video_prompt":"...",
            "characters":[
                {{
                    "name":"lena",
                    "expression":"determined",
                    "pose":"running",
                    "costume":"jungle",
                    "power":"energy_pulse"
                }},
                {{
                    "name":"kitti",
                    "expression":"scared",
                    "pose":"flying",
                    "power":"flame_spit"
                }}
            ]
        }}
    ]
}}
"""

        last_error = None

        for attempt in range(5):

            print(
                f"Video {video_number} attempt {attempt + 1}/5"
            )

            response = ""

            try:

                response = self.ai.generate(
                    SYSTEM_PROMPT,
                    prompt,
                )

                data = extract_json(
                    response
                )

                if len(
                    data["clips"]
                ) != 4:

                    raise ValueError(
                        f"Expected 4 clips, got {len(data['clips'])}"
                    )

                video = Video(
                    id=video_number,
                    title=data["title"],
                )

                for clip_index, clip_data in enumerate(
                    data["clips"],
                    start=1,
                ):

                    characters = []

                    for character in clip_data.get(
                        "characters",
                        [],
                    ):

                        characters.append(
                            CharacterState(
                                name=character["name"],
                                expression=character.get(
                                    "expression"
                                ),
                                pose=character.get(
                                    "pose"
                                ),
                                costume=character.get(
                                    "costume"
                                ),
                                power=character.get(
                                    "power"
                                ),
                            )
                        )

                    video.clips.append(
                        Clip(
                            id=clip_index,
                            title=clip_data["title"],
                            narrative=clip_data["narrative"],
                            camera=clip_data["camera"],
                            hook=clip_data["hook"],
                            image_prompt=clip_data["image_prompt"],
                            video_prompt=clip_data["video_prompt"],
                            characters=characters,
                        )
                    )

                return video

            except Exception as e:

                print("=" * 80)
                print(response)
                print("=" * 80)
                print(e)

                last_error = e

        raise RuntimeError(
            f"Video {video_number} generation failed: {last_error}"
        )