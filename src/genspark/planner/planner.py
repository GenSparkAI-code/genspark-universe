from genspark.ai import get_ai
from genspark.models.concept import Clip
from genspark.models.concept import Concept
from genspark.models.concept import Video
from genspark.planner.prompts import SYSTEM_PROMPT
from genspark.planner.user_prompt import build_prompt
from genspark.planner.validator import PlannerValidator
from genspark.utils.json_utils import extract_json


class Planner:

    def __init__(self):

        self.ai = get_ai()

    def generate(self):

        last_error = None

        for attempt in range(5):

            print(f"Planner attempt {attempt + 1}/5")

            response = ""

            try:

                response = self.ai.generate(
                    SYSTEM_PROMPT,
                    build_prompt(),
                )

                data = extract_json(
                    response
                )

                PlannerValidator.validate(
                    data
                )

                concept = Concept(
                    title=data["title"]
                )

                for video_index, video_data in enumerate(
                    data["videos"],
                    start=1,
                ):

                    video = Video(
                        id=video_index,
                        title=video_data["title"],
                    )

                    for clip_index, clip_data in enumerate(
                        video_data["clips"],
                        start=1,
                    ):

                        video.clips.append(
                            Clip(
                                id=clip_index,
                                title=clip_data["title"],
                                narrative=clip_data["narrative"],
                                camera=clip_data["camera"],
                                hook=clip_data["hook"],
                                image_prompt=clip_data["image_prompt"],
                                video_prompt=clip_data["video_prompt"],
                            )
                        )

                    concept.videos.append(
                        video
                    )

                return concept

            except Exception as e:

                print("=" * 80)
                print(response)
                print("=" * 80)
                print(e)

                last_error = e

        raise RuntimeError(
            f"Planner failed after 5 attempts: {last_error}"
        )