from genspark.render.flux_renderer import FluxRenderer


class ImageRenderer:

    def __init__(self):

        self.renderer = FluxRenderer()

    def render(
        self,
        request,
    ):

        return self.renderer.render(
            request
        )