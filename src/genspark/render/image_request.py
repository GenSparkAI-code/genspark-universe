from dataclasses import dataclass
from pathlib import Path

from genspark.models.character import CharacterState


@dataclass
class ImageRequest:

    prompt: str

    output_path: Path

    characters: list[CharacterState]