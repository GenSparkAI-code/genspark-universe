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
            template_name="image_template.txt",
            scene_key="image_prompt",
        )

    def build_video_prompt(self, clip: dict) -> str:
        return self._build_prompt(
            clip=clip,
            template_name="video_template.txt",
            scene_key="video_prompt",
        )

    #
    # Internal
    #

    def _build_prompt(
        self,
        clip: dict,
        template_name: str,
        scene_key: str,
    ) -> str:

        scene = clip[scene_key]

        template_path = (
            Path("assets")
            / "prompts"
            / template_name
        )

        template = self._load_text(template_path)

        character_blocks = []

        for character in clip.get("characters", []):
            character_blocks.append(
                self._build_character_block(character)
            )

        prompt = template
        prompt = prompt.replace("{scene}", scene)
        prompt = prompt.replace(
            "{characters}",
            "\n\n".join(character_blocks),
        )

        return prompt.strip()

    def _build_character_block(
        self,
        character: CharacterState,
    ) -> str:

        name = character.name

        character_dir = self.characters_dir / name

        values = {
            "profile": self._load_text(
                character_dir / "identity" / "profile.json"
            ),
            "appearance": self._load_text(
                character_dir / "identity" / "appearance.json"
            ),
            "colors": self._load_text(
                character_dir / "identity" / "colors.json"
            ),
            "personality": self._load_text(
                character_dir / "personality" / "personality.json"
            ),
            "voice": self._load_text(
                character_dir / "personality" / "voice.json"
            ),
            "memory": self._load_text(
                character_dir / "personality" / "memory.json"
            ),
            "powers": self._load_text(
                character_dir / "abilities" / "powers.json"
            ),
            "combos": self._load_text(
                character_dir / "abilities" / "combos.json"
            ),
            "expression": self._optional_json(
                character_dir / "expressions",
                character.expression,
            ),
            "pose": self._optional_json(
                character_dir / "poses",
                character.pose,
            ),
            "costume": self._optional_json(
                character_dir / "costumes",
                character.costume,
            ),
            "selected_power": character.power or "",
        }

        block = []

        for key, value in values.items():
            if value:
                block.append(
                    f"## {key.upper()}\n{value}"
                )

        return "\n\n".join(block)

    #
    # Helpers
    #

    def _optional_json(
        self,
        directory: Path,
        filename: str | None,
    ) -> str:

        if not filename:
            return ""

        return self._load_text(
            directory / f"{filename}.json"
        )

    def _load_text(
        self,
        path: Path,
    ) -> str:

        if not path.exists():
            return ""

        return path.read_text(
            encoding="utf-8",
        ).strip()