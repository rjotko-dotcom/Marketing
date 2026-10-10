# Marketing — working notes for Claude

Marketing for Rimvydas's new projects, done end to end by Claude at zero tool cost: strategy, copy, finished images and videos. One folder per project under `projects/`; `projects/_template/` is the starting point.

## Layout

| Path | What |
|---|---|
| `projects/<slug>/brief.md` | what it is, who for, 90-day goal, budget, rules |
| `projects/<slug>/brand.md` / `brand.css` | voice, proof · colours and fonts used by every design |
| `projects/<slug>/calendar.md` | dated content plan |
| `projects/<slug>/log.md` | what ran, spend, results, lessons (newest first) |
| `projects/<slug>/designs/` | HTML source of every image/video |
| `projects/<slug>/assets/` | logos, `screens/` (real screenshots), `out/` (rendered PNG/MP4) |
| `templates/design/` | `base.css` + `post.html`, `carousel.html`, `reel.html` |
| `tools/` | `render.mjs` (HTML→PNG), `video.mjs` (HTML→MP4), `shot.mjs` (real page→PNG) |
| `.claude/skills/` | the workflows below |

## Skills

Plan: `new-project` → `competitor-scan` → `launch-plan`
Make: `social-posts`, `video-script`, `ad-creative`, `make-visual`, `make-video`
Measure: `weekly-review`

## Making images and video

Claude designs in HTML/CSS and renders it — no paid AI image or video service. Setup in a fresh checkout:
`PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install`; in cloud sessions `export CHROMIUM_PATH=/opt/pw-browsers/chromium` (ffmpeg is preinstalled there). Always look at the rendered PNGs / video frames before handing them over.

## Rules

- Never invent proof: user counts, reviews, testimonials, results, press, or numbers inside a product screenshot. Only what is in `brand.md` → Proof.
- Product UI in creatives comes from real screenshots, never a drawn imitation.
- Regulated topics (finance/crypto, health/fitness, supplements, gambling): note the platform policy and legal limits in the brief before writing copy. No profit/return promises, no medical or before/after claims.
- Only free-licensed images, fonts and music; keep credits in the design file.
- Posting, spending money or emailing people happens only when Rimvydas says so for that specific thing. Drafting is always fine.
- Lithuanian and English are both normal; write natively in each, don't translate literally.
- Keep `log.md` honest — failures are the useful part.
