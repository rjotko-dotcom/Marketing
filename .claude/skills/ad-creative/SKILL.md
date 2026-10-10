---
name: ad-creative
description: Plan and produce paid-ad creative sets (Meta, TikTok, Google, App Store/Play) — angles, copy within each platform's limits, and finished image/video ads rendered with the make-visual and make-video skills. Use when the user asks for "ads", "ad creative", "variations to test", "UGC-style ad", "make banners", or a campaign's visuals.
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
4. **Visuals** — for each angle, one static and one video, made for real, not just described:
   - static → `make-visual` (`templates/design/post.html` renders 1:1, 4:5, 9:16 and 1.91:1 in one go)
   - video → `make-video` (6–15s, hook in the first 2s)
   - real product screens via `tools/shot.mjs`; the user's own photos/footage when people need to be in it
   - UGC-style (a person talking to camera): write the script and shot list for the user or a creator to film on a phone — that format can't be faked honestly.
5. **Test plan** — which 2–3 variants run first, budget per variant, the single metric (CPI, CPA, CTR) and the stop rule (e.g. stop a variant at 2× target CPA with ≥ 1,000 impressions).
6. Save generated files under `projects/<slug>/assets/ads/` and log the test in `log.md`.

Compliance: no before/after body claims for fitness, no income or return promises for finance/crypto, no fake reviews or fake UGC presented as real customers. Label AI-generated people where the platform requires it.
