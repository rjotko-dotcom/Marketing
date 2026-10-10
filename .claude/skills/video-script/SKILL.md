---
name: video-script
description: Write short-form video scripts (TikTok, Reels, Shorts, 15–60s) and longer YouTube outlines with shot lists, on-screen text and voiceover, then hand shots to Higgsfield for generation. Use for "video idea", "script", "reel", "TikTok", "storyboard", "explainer video", or "YouTube video about X".
argument-hint: "[project slug] [topic] [length] [platform]"
---

# Video script

1. Read the project's brand voice and audience.
2. Give 3 hook options (≤ 2 seconds each, spoken + on-screen). Pick one.
3. Write the script as a table: `time · shot (what we see) · on-screen text · voiceover · source`.
   Source is one of: screen recording, filmed by user, AI-generated (Higgsfield), stock.
4. Structure for short-form: hook → problem → show the thing working → proof → one CTA. Cut anything that doesn't serve the hook's promise.
5. For AI-generated shots, write the Higgsfield prompt per shot (subject, action, camera move, lighting, brand style, aspect 9:16) for `higgsfield-generate`. For a fully narrated animated explainer, use `higgsfield-video-explainer` instead. For the YouTube cover, `higgsfield-youtube-thumbnail`.
6. Add a caption + hashtags (see `social-posts`) and put the video in `calendar.md`.

Prefer real screen recordings of the product over generated footage of it — a generated UI is a fake UI.
