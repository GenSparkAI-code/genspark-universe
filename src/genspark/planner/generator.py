import json
from pathlib import Path

from genspark.planner.planner import Planner


class Generator:

    def __init__(self):
        self.planner = Planner()

    def generate(self, count: int):

        output_root = Path("generated")
        output_root.mkdir(exist_ok=True)

        for i in range(1, count + 1):

            concept = self.planner.generate()

            concept_dir = output_root / f"concept_{i:03d}"
            concept_dir.mkdir(parents=True, exist_ok=True)

            data = {
                "title": concept.title,
                "videos": [],
            }

            for video in concept.videos:

                data["videos"].append(
                    {
                        "id": video.id,
                        "title": video.title,
                        "clips": [
                            {
                                "id": clip.id,
                                "title": clip.title,
                            }
                            for clip in video.clips
                        ],
                    }
                )

            with open(
                concept_dir / "concept.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    data,
                    f,
                    indent=4,
                )

            print(f"Generated {concept_dir}")