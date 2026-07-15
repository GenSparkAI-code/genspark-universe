from dataclasses import dataclass, field

from genspark.models.character import CharacterState


@dataclass
class Clip:

    id: int

    title: str

    narrative: str

    camera: str

    hook: str

    image_prompt: str

    video_prompt: str

    characters: list[CharacterState] = field(
        default_factory=list
    )


@dataclass
class Video:

    id: int

    title: str

    clips: list[Clip] = field(
        default_factory=list
    )


@dataclass
class Concept:

    id: int

    title: str

    videos: list[Video] = field(
        default_factory=list
    )