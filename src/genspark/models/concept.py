from dataclasses import asdict
from dataclasses import dataclass, field


@dataclass
class Clip:
    id: int
    title: str = ""
    narrative: str = ""
    camera: str = ""
    hook: str = ""
    image_prompt: str = ""
    video_prompt: str = ""


@dataclass
class Video:
    id: int
    title: str = ""
    clips: list[Clip] = field(default_factory=list)


@dataclass
class Concept:
    title: str = ""
    videos: list[Video] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)