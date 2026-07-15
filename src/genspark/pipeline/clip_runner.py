from pathlib import Path

from genspark.render.image_renderer import ImageRenderer
from genspark.render.image_request import ImageRequest
from genspark.render.prompt_builder import PromptBuilder


class ClipRunner:

    def __init__(self):

        self.renderer = ImageRenderer()

        self.prompt_builder = PromptBuilder()

    def run(
        self,
        concept_id: int,
        video,
        clip,
    ) -> Path:

        clip_dir = (
            Path("generated")
            / f"concept_{concept_id:03d}"
            / f"video_{video.id:03d}"
            / f"clip_{clip.id:03d}"
        )

        clip_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # Build prompt
        #

        image_prompt = self.prompt_builder.build_image_prompt(
            {
                "image_prompt": clip.image_prompt,
                "characters": clip.characters,
            }
        )

        image_path = (
            clip_dir / "frame.png"
        )

        #
        # Save generated prompts
        #

        (clip_dir / "image_prompt.txt").write_text(
            image_prompt,
            encoding="utf-8",
        )

        (clip_dir / "video_prompt.txt").write_text(
            clip.video_prompt,
            encoding="utf-8",
        )

        (clip_dir / "prompt.txt").write_text(
            clip.narrative,
            encoding="utf-8",
        )

        #
        # Render image
        #

        request = ImageRequest(
            prompt=image_prompt,
            output_path=str(image_path),
        )

        self.renderer.render(request)

        if not image_path.exists():

            raise RuntimeError(
                f"Image was not generated: {image_path}"
            )

        return image_path