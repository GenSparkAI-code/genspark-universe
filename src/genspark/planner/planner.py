from genspark.models.concept import Clip
from genspark.models.concept import Concept
from genspark.models.concept import Video


class Planner:

    def generate(self) -> Concept:

        concept = Concept(
            title="Demo Concept"
        )

        for video_number in range(1, 6):

            video = Video(
                id=video_number,
                title=f"Video {video_number}",
            )

            for clip_number in range(1, 5):

                video.clips.append(
                    Clip(
                        id=clip_number,
                        title=f"Clip {clip_number}",
                    )
                )

            concept.videos.append(video)

        return concept