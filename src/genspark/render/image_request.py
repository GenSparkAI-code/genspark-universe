from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImageRequest:

    prompt: str

    output_path: Path