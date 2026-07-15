from pathlib import Path


class PromptBuilder:

    def __init__(self):

        self.characters_dir = (
            Path("assets") / "characters"
        )

    #
    # Public
    #

    def build_image_prompt(
        self,
        clip: dict,
    ) -> str:

        scene = clip["image_prompt"]

        prompts = []

        for character in clip.get(
            "characters",
            [],
        ):

            prompts.append(
                self._build_character_prompt(
                    character,
                    scene,
                )
            )

        return "\n\n".join(
            x for x in prompts if x.strip()
        )

    #
    # Character
    #

    def _build_character_prompt(
        self,
        character,
        scene: str,
    ) -> str:

        #
        # Backward compatibility
        #

        if isinstance(character, str):

            character = {
                "name": character,
            }

        character_name = character["name"]

        expression_name = character.get(
            "expression",
            "",
        )

        pose_name = character.get(
            "pose",
            "",
        )

        character_dir = (
            self.characters_dir
            / character_name
        )

        template = self._load_text(
            character_dir
            / "render"
            / "image_template.txt"
        )

        #
        # Identity
        #

        appearance = self._load_text(
            character_dir
            / "identity"
            / "appearance.json"
        )

        profile = self._load_text(
            character_dir
            / "identity"
            / "profile.json"
        )

        #
        # Personality
        #

        personality = self._load_text(
            character_dir
            / "personality"
            / "personality.json"
        )

        voice = self._load_text(
            character_dir
            / "personality"
            / "voice.json"
        )

        memory = self._load_text(
            character_dir
            / "personality"
            / "memory.json"
        )

        #
        # Abilities
        #

        powers = self._load_text(
            character_dir
            / "abilities"
            / "powers.json"
        )

        combos = self._load_text(
            character_dir
            / "abilities"
            / "combos.json"
        )

        #
        # Expression
        #

        expression = ""

        if expression_name:

            expression = self._load_text(
                character_dir
                / "expressions"
                / f"{expression_name}.json"
            )

        #
        # Pose
        #

        pose = ""

        if pose_name:

            pose = self._load_text(
                character_dir
                / "poses"
                / f"{pose_name}.json"
            )

        #
        # Replace template variables
        #

        prompt = template

        replacements = {
            "{appearance}": appearance,
            "{profile}": profile,
            "{personality}": personality,
            "{voice}": voice,
            "{memory}": memory,
            "{powers}": powers,
            "{combos}": combos,
            "{expression}": expression,
            "{pose}": pose,
            "{scene}": scene,
        }

        for key, value in replacements.items():

            prompt = prompt.replace(
                key,
                value,
            )

        return prompt

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