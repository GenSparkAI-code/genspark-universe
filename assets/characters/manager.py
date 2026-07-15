from pathlib import Path

from genspark.models.character import Character


class CharacterManager:

    def __init__(self):

        self.root = Path("assets/characters")

    def get(
        self,
        name: str,
    ) -> Character:

        character_root = self.root / name.lower()

        return Character(
            name=name,
            root=character_root,
            turnaround=character_root / "turnaround.png",
            bible=character_root / "bible.md",
        )