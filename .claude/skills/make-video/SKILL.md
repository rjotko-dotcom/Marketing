---
name: make-video
description: Make short marketing videos for free — Reels, TikToks, Shorts, animated ads, product demos with real screenshots, kinetic-text videos, slideshow videos — by animating HTML/CSS and rendering frame by frame to MP4 with tools/video.mjs and ffmpeg. Use when the user wants a video, reel, TikTok, animated ad or motion graphic.
argument-hint: "[project slug] [topic] [length] [9:16|1:1|16:9]"
---

# Make a video

Motion graphics built in code, rendered deterministically to H.264 MP4 ready to upload.

## Setup

As in `make-visual` (npm install, CHROMIUM_PATH in cloud). Needs `ffmpeg` on PATH (installed in cloud sessions; on Windows `winget install ffmpeg`).

## Steps

1. Script first (use `video-script`): hook ≤ 2s, one idea per scene, CTA last. Typical: 7–15s for ads, 15–30s for organic.
2. Gather real material: product screenshots (`tools/shot.mjs`), screen recordings, user photos. A screen recording can be embedded with `<video src muted>` only if the page also defines `window.seek(t)` that sets `video.currentTime = t`; simpler is to cut screen recordings in with ffmpeg afterwards.
3. Copy `templates/design/reel.html` to `projects/<slug>/designs/<date>-<name>.html`. Each `<section class="scene" style="--in:Xs; --out:Ys">` is a scene; animate elements with `.rise`, `.fade`, `.pop`, `.drift` and `animation-delay`. Set `<meta name="duration">`.
4. Render: `node tools/video.mjs <file> --out projects/<slug>/assets/out/<name>.mp4` (`--size 1080x1080` for square, `1920x1080` for YouTube, `--fps 30`).
5. Check it: pull frames with `ffmpeg -ss <t> -i out.mp4 -frames:v 1 f.png` at the hook, each scene and the end, and look at them. Fix and re-render.
6. Sound: TikTok/Instagram trending audio is added in their app (best for reach). For a baked-in track use only royalty-free music (YouTube Audio Library, Pixabay Music) with `--audio file.mp3`. Voiceover: the user records it on their phone; join with `ffmpeg -i video.mp4 -i vo.m4a -c:v copy -shortest out.mp4`.
7. Burned-in captions: put the spoken words on screen as text in the scenes — most people watch muted.

Keep text on screen long enough to read twice (~0.3s per word, minimum 1.2s).
