from pathlib import Path

from genspark.pipeline.project_runner import ProjectRunner
from genspark.planner.generator import Generator


class Pipeline:

    def __init__(self):

        self.generator = Generator()
        self.project_runner = ProjectRunner()

    def run(
        self,
        concept_count: int,
    ):

        self.generator.generate(
            concept_count
        )

        output_root = Path("generated")

        for concept_index in range(
            1,
            concept_count + 1,
        ):

            concept_dir = (
                output_root
                / f"concept_{concept_index:03d}"
            )

            self.project_runner.run(
                concept_dir
            )