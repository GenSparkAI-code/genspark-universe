def build_prompt():

    return """
Generate ONE completely original viral concept.

Return ONLY valid JSON.

Do NOT return markdown.

Do NOT return explanations.

Do NOT return notes.

Do NOT return code fences.

Do NOT think aloud.

You MUST generate EXACTLY 5 videos.

Video 1:
- EXACTLY 4 clips

Video 2:
- EXACTLY 4 clips

Video 3:
- EXACTLY 4 clips

Video 4:
- EXACTLY 4 clips

Video 5:
- EXACTLY 4 clips

Every clip MUST contain:

- title
- narrative
- camera
- hook
- image_prompt
- video_prompt

Every clip is exactly 3 seconds.

Every clip ends with a cinematic hook.

Maintain story continuity.

Maintain character continuity.

Maintain lighting continuity.

Maintain camera continuity.

Return ONLY this JSON schema.

{
    "title": "...",
    "videos": [
        {
            "title": "...",
            "clips": [
                {
                    "title": "...",
                    "narrative": "...",
                    "camera": "...",
                    "hook": "...",
                    "image_prompt": "...",
                    "video_prompt": "..."
                }
            ]
        }
    ]
}
"""