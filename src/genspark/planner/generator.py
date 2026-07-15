import json
from pathlib import Path

from genspark.models.concept import Concept
from genspark.planner.concept_planner import ConceptPlanner
from genspark.planner.video_planner import VideoPlanner


class Generator:

    def __init__(self):

        self.concept_planner = ConceptPlanner()
        self.video_planner = VideoPlanner()

    def generate(
        self,
        count: int,
    ):

        output_root = Path("generated")
        output_root.mkdir(
            parents=True,
            exist_ok=True,
        )

        for concept_index in range(
            1,
            count + 1,
        ):

            print()
            print("=" * 70)
            print(f"Concept {concept_index}")
            print("=" * 70)

            #
            # Generate Concept
            #

            concept_data = self.concept_planner.generate()

            concept = Concept(
                title=concept_data["title"],
            )

            print(
                f"Concept: {concept.title}"
            )

            #
            # Generate Videos
            #

            for video_number in range(
                1,
                6,
            ):

                print()
                print(
                    f"Generating Video {video_number}/5..."
                )

                video = self.video_planner.generate(
                    concept.title,
                    video_number,
                )

                concept.videos.append(
                    video
                )

            #
            # Save
            #

            concept_dir = (
                output_root
                / f"concept_{concept_index:03d}"
            )

            concept_dir.mkdir(
                parents=True,
                exist_ok=True,
            )

            output_file = (
                concept_dir
                / "concept.json"
            )

            output = {
                "title": concept.title,
                "videos": [],
            }

            for video in concept.videos:

                video_json = {
                    "title": video.title,
                    "clips": [],
                }

                for clip in video.clips:

                    video_json["clips"].append(
                        {
                            "title": clip.title,
                            "narrative": clip.narrative,
                            "camera": clip.camera,
                            "hook": clip.hook,
                            "image_prompt": clip.image_prompt,
                            "video_prompt": clip.video_prompt,
                        }
                    )

                output["videos"].append(
                    video_json
                )

            output_file.write_text(
                json.dumps(
                    output,
                    indent=4,
                )
            )

            print()
            print(
                f"Saved {output_file}"
            )