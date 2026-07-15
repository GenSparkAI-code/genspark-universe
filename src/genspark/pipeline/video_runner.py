from genspark.pipeline.clip_runner import ClipRunner


class VideoRunner:

    def __init__(self):

        self.clip_runner = ClipRunner()

    def run(
        self,
        concept,
        video,
        video_index,
        total_videos,
        concept_dir,
    ):

        print()
        print("=" * 70)
        print(
            f"Video {video_index}/{total_videos}: {video['title']}"
        )
        print("=" * 70)

        clips = video["clips"]

        for clip_index, clip in enumerate(
            clips,
            start=1,
        ):

            self.clip_runner.run(
                concept=concept,
                video=video,
                clip=clip,
                concept_dir=concept_dir,
                video_index=video_index,
                clip_index=clip_index,
                total_clips=len(clips),
            )