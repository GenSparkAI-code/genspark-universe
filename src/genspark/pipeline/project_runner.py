import json
from pathlib import Path

from genspark.pipeline.video_runner import VideoRunner


class ProjectRunner:

    def __init__(self):

        self.video_runner = VideoRunner()

    def run(
        self,
        concept_dir: Path,
    ):

        concept_file = concept_dir / "concept.json"

        data = json.loads(
            concept_file.read_text()
        )

        print()
        print("=" * 70)
        print(data["title"])
        print("=" * 70)

        videos = data["videos"]

        for video_index, video in enumerate(
            videos,
            start=1,
        ):

            self.video_runner.run(
                concept=data,
                video=video,
                video_index=video_index,
                total_videos=len(videos),
                concept_dir=concept_dir,
            )