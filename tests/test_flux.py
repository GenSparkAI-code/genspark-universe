from pathlib import Path

from genspark.render.image_renderer import ImageRenderer
from genspark.render.image_request import ImageRequest


def main():

    renderer = ImageRenderer()

    request = ImageRequest(
        prompt="""
Photorealistic cinematic fantasy.

A tiny blue dragon flying beside a brave female explorer in a snowy mountain valley at sunrise.

Ultra detailed.

IMAX.

8k.

Masterpiece.
""",
        output_path=Path(
            "tests/output/test_flux.png"
        ),
    )

    request.output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    renderer.render(request)

    print(
        request.output_path
    )


if __name__ == "__main__":
    main()