---
name: make-visual
description: Design and render finished marketing images for free — social posts, ads in every size, carousels, banners, App Store / Play screenshots, thumbnails, quote cards, OG images — by writing HTML/CSS and rendering it to PNG with tools/render.mjs. Use whenever the user wants an image, graphic, banner, post, ad visual, carousel, mockup or screenshot set. No paid AI image service needed.
argument-hint: "[project slug] [what: post|ad|carousel|store-screens|banner|thumbnail] [sizes]"
---

# Make a visual

Claude designs in code and renders it pixel-exact. Nothing is AI-painted, so text is always sharp and spelled right, and brand colours are exact.

## Setup (once per machine/session)

`ls node_modules/playwright >/dev/null 2>&1 || PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install`
In cloud sessions also `export CHROMIUM_PATH=/opt/pw-browsers/chromium`. On a PC without that, `npx playwright install chromium` once.

## Steps

1. Read `projects/<slug>/brand.md` and make sure `projects/<slug>/brand.css` carries its colours and fonts (Google Fonts may be loaded with an `@import` at the top of brand.css).
2. **Get real material first.** Product screens: `node tools/shot.mjs <url> --dark --out projects/<slug>/assets/screens/<name>.png`. For apps that open on an empty first-run screen, seed demo data with `--storage state.json` and navigate with `--click "<selector>"`; strip toasts with `--hide`. User-supplied logos/photos go in `assets/`.
3. Copy the closest template from `templates/design/` into `projects/<slug>/designs/<date>-<name>.html`:
   - `post.html`: one image, reflows for 1:1, 4:5, 9:16, 1.91:1
   - `carousel.html`: one PNG per `[data-slide]`
   - start from scratch with `base.css` for anything else (store screenshots 1290x2796 / 1080x1920, YouTube thumbnail 1280x720, OG 1200x630, Facebook cover 1640x624)
4. Write the copy into it (voice from brand.md). Use the classes in `base.css` (`.headline`, `.sub`, `.cta`, `.phone`, `.browser`, `.card`) and size everything in `var(--u)` so it scales across sizes.
5. Render: `node tools/render.mjs projects/<slug>/designs/<file>.html --out projects/<slug>/assets/out` (`--size` to override; `--scale 2` for retina).
6. **Look at every PNG** (Read the image). Fix overlap, clipped text, tiny text on 9:16, and anything that reads badly as a thumbnail, then re-render. Don't ship the first render unseen.
7. Send the finished files to the user, and note them in `calendar.md`.

## Design rules

- One message per image. Headline ≤ 7 words on ads.
- Contrast: text must be readable at phone size, and as a 300px thumbnail.
- 9:16: keep text out of the top 13% and bottom 20% (platform UI).
- Real screenshots only for product UI. Never draw a fake interface or invent numbers in one.
- For photos of people or places you don't have, either use the user's own photos, free-licensed stock (Unsplash/Pexels, keep the credit in the design file's comment), or design a type-led graphic instead.
