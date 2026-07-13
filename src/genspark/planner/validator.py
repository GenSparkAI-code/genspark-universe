class PlannerValidator:

    @staticmethod
    def validate(concept):

        if len(concept["videos"]) != 5:
            raise ValueError(
                f"Expected 5 videos, got {len(concept['videos'])}"
            )

        for video in concept["videos"]:

            if len(video["clips"]) != 4:
                raise ValueError(
                    "Every video must contain exactly 4 clips."
                )