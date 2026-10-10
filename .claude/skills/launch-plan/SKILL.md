---
name: launch-plan
description: Build a dated launch or growth plan for one project — pre-launch, launch week, first 30 days — with channels, assets to make, owners, budget and the metric each step moves. Use when the user says "launch plan", "how do we launch X", "go-to-market", "plan the release", or "grow X".
argument-hint: "[project slug] [launch date]"
---

# Launch plan

Inputs: `projects/<slug>/brief.md` and `brand.md`. If the brief is empty, run the `new-project` skill first.

Write `projects/<slug>/launch-plan.md` with:

1. **Goal** — the one number from the brief and the date.
2. **Audience & where they are** — 2–3 places (subreddits, TikTok niches, forums, Facebook groups, app-store search terms). Name real ones; mark any you could not verify.
3. **Message** — one-line promise, three supporting points, the proof for each.
4. **Phases** (dated table: date · action · channel · asset · cost · metric)
   - T-14 to T-1: waitlist/landing page, teaser content, seed 10–20 real users, collect first testimonials.
   - Launch week: the announcement on every owned channel, community posts (follow each community's self-promo rules), Product Hunt / store featuring requests if relevant.
   - Days 8–30: double down on what moved the number, cut the rest. Weekly review (see `weekly-review`).
5. **Asset list** — every image/video needed, with format and size. Mark which ones go to Higgsfield (`higgsfield-generate`, `higgsfield-product-photoshoot`, `higgsfield-youtube-thumbnail`) and draft the prompt for each using the image style in `brand.md`.
6. **Budget** — split by channel; with €0 budget, organic only and say so.
7. **Risks** — what could make this flop and the early signal for it.

Then add the dated rows to `calendar.md`. Keep the plan to what one person can actually do; cut rather than pad.
