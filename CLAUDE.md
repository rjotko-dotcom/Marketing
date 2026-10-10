# Marketing — working notes for Claude

Marketing for Rimvydas's new projects. One folder per project under `projects/`; `projects/_template/` is the starting point. Current projects to expect: **B.E.L.A** gym app (`rjotko-dotcom/B.E.L.A-gym-app`), **BELA CryptoBot** (`rjotko-dotcom/BELA-CryptoBot`).

## Layout

| Path | What |
|---|---|
| `projects/<slug>/brief.md` | what it is, who for, 90-day goal, budget, rules |
| `projects/<slug>/brand.md` | voice, colours, fonts, AI image style, allowed proof |
| `projects/<slug>/calendar.md` | dated content plan |
| `projects/<slug>/log.md` | what ran, spend, results, lessons (newest first) |
| `projects/<slug>/assets/` | logos, screenshots, generated images/video |
| `.claude/skills/` | this repo's workflows (below) |

## Skills in this repo

`new-project` → `competitor-scan` → `launch-plan` → `social-posts` / `video-script` / `ad-creative` → `weekly-review`.

## Image & video generation — Higgsfield

Generation goes through Higgsfield's official skills (`higgsfield-generate`, `higgsfield-product-photoshoot`, `higgsfield-brandkit`, `higgsfield-soul-id`, `higgsfield-video-explainer`, `higgsfield-youtube-thumbnail`, `higgsfield-marketplace-cards`, `higgsfield-websites`) from `higgsfield-ai/skills`, which drive the `higgsfield` CLI — one account, many models (GPT Image, Nano Banana, Seedream, Soul, Seedance, Kling, Veo…). Setup is in `README.md`. If the CLI is not installed or logged in, write the prompts to a file and say so; never present a generation that did not happen.

Every prompt reuses the project's image style and colours from `brand.md`. Save outputs to `projects/<slug>/assets/` with a descriptive name.

## Rules

- Never invent proof: user counts, reviews, testimonials, results, press. Only what is in `brand.md` → Proof.
- **Crypto / trading (BELA CryptoBot):** no profit or return promises, no "guaranteed", no performance numbers that aren't real, audited and shown with risk wording. Follow each ad platform's crypto/financial-services policy (often pre-approval) and EU MiCA marketing rules. While the bot is paper-trading only, say exactly that.
- **Fitness (B.E.L.A):** no medical claims, no before/after body promises.
- No fake reviews, no fake UGC presented as real customers; label AI-generated people where the platform requires it.
- Posting, spending money or sending email to people happens only when Rimvydas says so for that specific thing. Drafting is always fine.
- Lithuanian and English are both normal; write natively in each, don't translate literally.
- Keep `log.md` honest — failures are the useful part.
