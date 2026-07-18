import json
from pathlib import Path


class CharacterRegistry:

    def __init__(self):

        self.characters_dir = (
            Path("assets")
            / "characters"
        )

    def planner_description(self) -> str:

        blocks = []

        for character_dir in sorted(
            self.characters_dir.iterdir()
        ):

            if not character_dir.is_dir():
                continue

            name = character_dir.name

            block = [
                f"Character: {name}"
            ]

            expressions = self._list_json_names(
                character_dir / "expressions"
            )

            if expressions:

                block.append(
                    "Expressions:"
                )

                block.extend(expressions)

            poses = self._list_json_names(
                character_dir / "poses"
            )

            if poses:

                block.append(
                    "Poses:"
                )

                block.extend(poses)

            costumes = self._list_json_names(
                character_dir / "costumes"
            )

            if costumes:

                block.append(
                    "Costumes:"
                )

                block.extend(costumes)

            powers = self._load_power_names(
                character_dir
                / "abilities"
                / "powers.json"
            )

            if powers:

                block.append(
                    "Powers:"
                )

                block.extend(powers)

            blocks.append(
                "\n".join(block)
            )

        return "\n\n".join(blocks)

    #
    # Helpers
    #

    def _list_json_names(
        self,
        directory: Path,
    ):

        if not directory.exists():
            return []

        return sorted(
            f.stem
            for f in directory.glob(
                "*.json"
            )
        )

    def _load_power_names(
        self,
        path: Path,
    ):

        if not path.exists():
            return []

        try:

            data = json.loads(
                path.read_text()
            )

        except Exception:

            return []

        if isinstance(data, list):

            return [
                item["name"]
                for item in data
                if "name" in item
            ]

        if isinstance(data, dict):

            if "powers" in data:

                return [
                    item["name"]
                    for item in data["powers"]
                    if "name" in item
                ]

        return []