from pathlib import Path

from genspark.models.character import CharacterState


class PromptBuilder:
    def __init__(self):
        self.characters_dir = Path("assets") / "characters"

    #
    # Public
    #

    def build_image_prompt(self, clip: dict) -> str:
        return self._build_prompt(
            clip=clip,
            scene_key="image_prompt",
            render_template="image_template.txt",
        )

    def build_video_prompt(self, clip: dict) -> str:
        return self._build_prompt(
            clip=clip,
            scene_key="video_prompt",
            render_template="video_template.txt",
        )

    #
    # Internal
    #

    def _build_prompt(
        self,
        clip: dict,
        scene_key: str,
        render_template: str,
    ) -> str:

        scene = clip[scene_key]

        character_blocks = [
            self._build_character_block(
                character,
                render_template,
            )
            for character in clip.get("characters", [])
        ]

        characters_text = "\n\n".join(character_blocks)

        prompt = f"""SCENE

{scene}

CHARACTERS

{characters_text}

Keep every character identical to its supplied Redux reference image.
Never redesign a character.
Maintain perfect character consistency.
"""

        return prompt.strip()

    def _build_character_block(
        self,
        character: CharacterState,
        render_template: str,
    ) -> str:

        template = self._load_text(
            self.characters_dir
            / character.name
            / "render"
            / render_template
        )

        return (
            template
            .replace("{expression}", character.expression or "")
            .replace("{pose}", character.pose or "")
            .replace("{costume}", character.costume or "")
            .replace("{power}", character.power or "")
        ).strip()

    #
    # Helpers
    #

    def _load_text(
        self,
        path: Path,
    ) -> str:

        if not path.exists():
            return ""

        return path.read_text(
            encoding="utf-8",
        ).strip()