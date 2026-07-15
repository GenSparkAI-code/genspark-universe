from pathlib import Path

from genspark.render.base_image_renderer import BaseImageRenderer
from genspark.render.image_request import ImageRequest


class FluxRenderer(BaseImageRenderer):

    def render(
        self,
        request: ImageRequest,
    ) -> Path:

        raise NotImplementedError(
            "Flux renderer not connected yet."
        )