# Marketing

Marketing for new projects, done with Claude Code: briefs, competitor research, launch plans, posts, ad copy, and finished images and videos. No paid design or AI-generation tools needed.

## Start a session

- **Claude app / web (claude.ai/code):** new session → pick the `marketing` repo.
- **PC:** `git clone https://github.com/rjotko-dotcom/marketing`, `cd marketing`, `npm install`, `npx playwright install chromium`, then `claude`.

## What to say

| You say | You get |
|---|---|
| `new project: <name> — <link or one line>` | `projects/<slug>/` with the brief filled in, after ≤ 5 questions |
| `competitor scan` | `competitors.md` with sources and angles to own |
| `launch plan, start <date>` | dated plan + calendar |
| `10 posts for next week, Lithuanian + English` | captions per platform + the images |
| `make an Instagram carousel about <topic>` | PNG slides |
| `make a 10s reel / TikTok about <feature>` | MP4, 1080×1920 |
| `4 Meta ad variants for signups` | angles, copy within limits, images in every size, test plan |
| `store screenshots` | App Store / Play images with real screens |
| `weekly review` + paste numbers | what to stop, keep and try next |

Everything is saved in the project folder, so the next session continues where the last one stopped. Claude drafts and makes; you post and spend.

## How images and videos are made

Claude writes each design as HTML/CSS (`projects/<slug>/designs/`) using the project's colours and fonts (`brand.css`) and renders it:

```bash
node tools/render.mjs projects/<slug>/designs/post.html      # PNG in every size listed in the file
node tools/video.mjs  projects/<slug>/designs/reel.html      # MP4 (needs ffmpeg)
node tools/shot.mjs   https://your-product.com --dark --out projects/<slug>/assets/screens/home.png
```

Text is always sharp and spelled right, colours exact, and every design can be re-edited and re-rendered in any size. What it can't do is invent photos of people or places — for those use your own photos, free stock (Unsplash, Pexels), or film it on your phone and Claude writes the shot list.

## Add your first project

1. Start a session (above).
2. Say `new project: <name> — <link>`.
3. Answer the questions, drop a logo and 3–5 screenshots/photos into `projects/<slug>/assets/` (or attach them in chat).
4. Say `launch plan` and go from there.
