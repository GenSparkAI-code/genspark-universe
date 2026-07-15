from abc import ABC
from abc import abstractmethod
from pathlib import Path

from genspark.render.image_request import ImageRequest


class BaseImageRenderer(ABC):

    @abstractmethod
    def render(
        self,
        request: ImageRequest,
    ) -> Path:
        pass