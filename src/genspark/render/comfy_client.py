import time
from pathlib import Path

import requests


class ComfyClient:

    def __init__(
        self,
        server="http://127.0.0.1:8188",
    ):

        self.server = server.rstrip("/")

    def queue_prompt(
        self,
        workflow,
    ):

        response = requests.post(
            f"{self.server}/prompt",
            json={
                "prompt": workflow,
            },
        )

        response.raise_for_status()

        return response.json()["prompt_id"]

    def wait_until_done(
        self,
        prompt_id,
    ):

        while True:

            history = requests.get(
                f"{self.server}/history/{prompt_id}"
            ).json()

            if prompt_id in history:

                return history[prompt_id]

            time.sleep(2)

    def download_image(
        self,
        filename,
        subfolder,
        image_type,
        output_path: Path,
    ):

        response = requests.get(
            f"{self.server}/view",
            params={
                "filename": filename,
                "subfolder": subfolder,
                "type": image_type,
            },
        )

        response.raise_for_status()

        output_path.write_bytes(
            response.content
        )

        return output_path