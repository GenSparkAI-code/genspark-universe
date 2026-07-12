from dataclasses import dataclass, field


@dataclass
class Clip:
    id: int
    title: str = ""


@dataclass
class Video:
    id: int
    title: str = ""
    clips: list[Clip] = field(default_factory=list)


@dataclass
class Concept:
    title: str = ""
    videos: list[Video] = field(default_factory=list)