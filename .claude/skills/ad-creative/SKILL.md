---
name: ad-creative
description: Plan and produce paid-ad creative sets (Meta, TikTok, Google, App Store/Play) — angles, copy within each platform's limits, and image/video generation through Higgsfield. Use when the user asks for "ads", "ad creative", "variations to test", "UGC-style ad", "make banners", or a campaign's visuals.
argument-hint: "[project slug] [platform] [goal: installs|signups|sales]"
---

# Ad creative

1. Read the brief (audience, goal, rules) and brand (voice, colours, image style, proof).
2. **Angles** — write 4–6 distinct angles (pain, outcome, objection-killer, social proof, demo, comparison). One line each, with the audience insight behind it.
3. **Copy** per angle, inside the platform limits, checked by counting characters:
   - Meta: primary text (aim ≤ 125 visible), headline ≤ 40, description ≤ 30.
   - Google RSA: headlines ≤ 30 ×15, descriptions ≤ 90 ×4.
   - TikTok: ad text ≤ 100; the hook lives in the first 2 seconds of video.
   - Limits change; say the date you last confirmed them.
4. **Visuals** — for each angle, one static and one video concept. Produce them with the Higgsfield skills when they are installed:
   - product/app shots → `higgsfield-product-photoshoot`
   - general images, UGC-style or avatar ads, image-to-video → `higgsfield-generate` (Marketing Studio for ads)
   - the founder on camera → `higgsfield-soul-id`, then generate with that Soul ID
   Always pass the brand image style and colours. Sizes: 1:1 and 4:5 feed, 9:16 stories/reels/TikTok, 1.91:1 link.
   If Higgsfield is not set up, write the prompts into `projects/<slug>/ads/<date>-<angle>.md` so they can be run later — do not fake outputs.
5. **Test plan** — which 2–3 variants run first, budget per variant, the single metric (CPI, CPA, CTR) and the stop rule (e.g. stop a variant at 2× target CPA with ≥ 1,000 impressions).
6. Save generated files under `projects/<slug>/assets/ads/` and log the test in `log.md`.

Compliance: no before/after body claims for fitness, no income or return promises for finance/crypto, no fake reviews or fake UGC presented as real customers. Label AI-generated people where the platform requires it.
