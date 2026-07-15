from dataclasses import dataclass


@dataclass
class CharacterState:

    name: str

    expression: str | None = None

    pose: str | None = None

    costume: str | None = None

    power: str | None = None