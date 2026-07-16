import json
import random
from copy import deepcopy
from pathlib import Path

from genspark.render.base_image_renderer import BaseImageRenderer
from genspark.render.comfy_client import ComfyClient
from genspark.render.image_request import ImageRequest


class FluxRenderer(BaseImageRenderer):

    def __init__(self):

        self.client = ComfyClient()

        workflow_path = (
            Path("workflows")
            / "flux.json"
        )

        self.workflow = json.loads(
            workflow_path.read_text(
                encoding="utf-8",
            )
        )

    def render(
        self,
        request: ImageRequest,
    ) -> Path:

        workflow = deepcopy(
            self.workflow
        )

        #
        # Prompt
        #

        workflow["56:51"]["inputs"][
            "text"
        ] = request.prompt

        #
        # Random seed
        #

        workflow["56:52"]["inputs"][
            "seed"
        ] = random.randint(
            0,
            2**63 - 1,
        )

        #
        # Output filename
        #

        workflow["9"]["inputs"][
            "filename_prefix"
        ] = request.output_path.stem

        prompt_id = self.client.queue_prompt(
            workflow
        )

        history = self.client.wait_until_done(
            prompt_id
        )

        images = []

        for output in history[
            "outputs"
        ].values():

            images.extend(
                output.get(
                    "images",
                    [],
                )
            )

        if not images:

            raise RuntimeError(
                "No image generated."
            )

        image = images[0]

        return self.client.download_image(
            filename=image["filename"],
            subfolder=image["subfolder"],
            image_type=image["type"],
            output_path=request.output_path,
        )