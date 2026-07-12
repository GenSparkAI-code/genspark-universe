def build_prompt():

    return """
Generate ONE viral concept.

Rules:

- Return JSON only.
- Produce exactly 5 videos.
- Every video has exactly 4 clips.
- Every clip is exactly 3 seconds.
- Every clip must end with a cinematic hook.
- Character continuity.
- Lighting continuity.
- Camera continuity.

JSON:

{
"title":"",
"videos":[]
}
"""