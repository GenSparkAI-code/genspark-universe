import json
import random
import shutil
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
            / "flux_redux.json"
        )

        self.workflow = json.loads(
            workflow_path.read_text(
                encoding="utf-8",
            )
        )

        self.comfy_input_dir = Path(
            "/workspace/ComfyUI/input"
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

        workflow["6"]["inputs"][
            "text"
        ] = request.prompt

        #
        # Character reference images (Redux)
        #

        load_image_nodes = [
            node_id
            for node_id, node in workflow.items()
            if node["class_type"] == "LoadImage"
        ]

        for node_id, character in zip(
            load_image_nodes,
            request.characters,
        ):

            source = (
                Path("assets")
                / "characters"
                / character.name
                / "identity"
                / "turnaround.png"
            )

            filename = (
                f"{character.name}_turnaround.png"
            )

            destination = (
                self.comfy_input_dir
                / filename
            )

            shutil.copy2(
                source,
                destination,
            )

            workflow[node_id]["inputs"][
                "image"
            ] = filename

        #
        # Random seed
        #

        workflow["25"]["inputs"][
            "noise_seed"
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