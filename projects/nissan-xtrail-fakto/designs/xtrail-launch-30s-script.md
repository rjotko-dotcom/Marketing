# X-Trail 2026 test ad: script + storyboard v2

**Format:** 30 s, 16:9, 1920×1080 (YouTube). No price. Lithuanian voiceover, LT/EN on-screen text.
**Purpose:** internal test video by Rimvydas (Fakto Auto). Before it goes public, swap the reference photos for Nissan dealer-portal assets.
**Storyboard:** `assets/out/xtrail-storyboard-1920x1440.png`

## Built version v1 (2026-10-10): made entirely from official press photos, €0

`xtrail-ad/build.py` builds it end to end → `assets/out/xtrail-fakto-ad-30s-1920x1080.mp4`.
No Fakto showroom photos existed yet, so this cut opens on the car rather than the dealership. Fakto shows up on the end card.

| Time | Shot (press photo #) | Motion | On screen |
|---|---|---|---|
| 0:00 | Tail light (44) | depth parallax push-in, fade from black | — |
| 0:02.6 | Sunset front 3/4 (28) | push-in | NAUJASIS / NISSAN X-TRAIL |
| 0:05.6 | Grille at dusk (11) | sideways parallax | Naujas veidas. Tas pats tvirtas charakteris. |
| 0:07.6 | 360°: front (54) → 3/4 (04) → side (03) → rear 3/4 (35) → badge (47) → front close (23) | whip cuts, parallax, white flashes | 360° badge + callout lines: grotelės, LED žibintai, raudoni akcentai, naujas galas |
| 0:13.4 | Details: grille macro (13), wheel (01), e-POWER badge (24), Google Maps screen (08), interior (10) | 1 s each, flash cuts | V-Motion · Pasiruošęs bekelei · e-POWER · Google integruota · ProPilot |
| 0:18.6 | Forest drive | AI clip (LTX-Video) | e-POWER — Varo elektra. Krauti nereikia. |
| 0:21.5 | Aerial, blue car (19) | parallax rise | Kiekvienam keliui. |
| 0:23.5 | Mountain overlook, two cars | AI clip (LTX-Video) | — |
| 0:25.9 | Lake overview (30), darkened | pull-out, cinema bars open | ATVYKITE PAMATYTI · Fakto + Nissan logos · faktoauto.lt · legal line |

Music: synthesised in `xtrail-ad/music.py` (drone, pulse, risers, booms on the cuts), so there's no licence.
**Before publishing:** add the WLTP fuel and CO₂ figures to the legal line, swap the press photos for dealer-portal assets, and optionally replace the opening with real Fakto showroom footage.

## How the footage gets made (€0)

Higgsfield bills its own credits. A Claude subscription doesn't cover them, and its free plan has no credits and no commercial rights. So the realistic shots are **filmed by you on a phone at Fakto**. The real car in the real showroom beats AI for realism, and the badges, grille and lights are guaranteed to be correct.
I do everything else here for free: stabilising, colour grade, speed ramps, animated callouts, titles, logos, end card, music and export.
Each shot also has an AI prompt. If you ever get credits (Higgsfield or any image-to-video tool), that shot can be generated from a real photo instead of filmed.

## Shots

| # | Time | What we see | On-screen text | Voiceover (LT) | Film it like this | AI prompt (optional, image-to-video) |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:04 | Blue hour outside Fakto. Slow push-in toward the lit showroom glass; the X-Trail glows inside. | — | — | Phone in landscape, 4K 30fps, walk slowly toward the glass at chest height; 3 takes, 20 min after sunset | "Slow dolly push-in toward a lit car showroom at blue hour, SUV visible through the glass, cinematic, realistic, no text changes" (start frame = your photo of the showroom) |
| 2 | 0:04–0:07 | Inside: low front angle, the headlights and DRLs switch on. | NAUJASIS NISSAN X-TRAIL | „Pažiūrėkite iš naujo." | Phone on the floor 1.5 m from the bumper, colleague switches the lights on; 3 takes | "Headlights switch on, subtle camera rise, showroom reflections, photoreal" (start frame = your photo) |
| 3 | 0:07–0:14 | **360° orbit** round the whole car. Thin callout lines draw on as each part passes: grille → lights → wheels → rear. | Naujas grotelių dizainas · LED žibintai · 19" ratlankiai *(check the size)* | „Naujas veidas. Tas pats tvirtas charakteris." | Walk one full circle at an even 2.5 m distance, phone at headlight height, steady pace (~20 s); 3 takes. I stabilise and speed-ramp it | "Smooth 360 orbit around the SUV, constant distance, eye level, studio lighting" (start frame = official front 3/4 photo) |
| 4 | 0:14–0:19 | **Detail jumps** on whip/flash cuts, about 1 s each: grille macro → headlight → wheel → Google screen → N-Trek seat. | Google integruota · ProPilot · e-POWER | „Google jau viduje. ProPilot — šalia jūsų kelyje." | 5 short slow slides, 3 s each, 20–30 cm from the surface; screen switched on with Maps open | "Macro slow slide across the grille mesh, shallow depth of field" (one per detail, start frame = your photo) |
| 5 | 0:19–0:26 | **In motion:** the car pulls out of the forecourt onto the street, then cuts to the forest road with a slow parallax move. | e-POWER | „Elektrinis važiavimo pojūtis. Be įkrovimo rūpesčių." *(check the wording with Nissan LT)* | From the pavement: car drives past the camera; second take from a car alongside (passenger films, never the driver) | "SUV driving along a forest dirt road at golden hour, tracking shot, dust in sunbeams" (start frame = official forest photo) |
| 6 | 0:26–0:30 | **End card:** car darkened behind the type; Fakto + Nissan logos. | Atvykite pamatyti · Fakto Auto · faktoauto.lt · [adresas] · WLTP: [l/100 km], CO₂ [g/km] | „Naujasis Nissan X-Trail. Jau Fakto Auto." | — (motion graphic, made here) | — |

**Sound:** one cinematic pulse/hybrid track (free-licensed, credit noted here), with a whoosh on each whip cut and a light hit when the headlights come on. Voiceover recorded by you or a colleague on a phone in a quiet room; I'll clean it up.

## Hooks considered

1. **Showroom push-in, lights on (picked):** starts at the dealership, as you asked.
2. Grille macro with a light sweep, "Naujas veidas."
3. Car fully dark, lights come on one by one on the beat.

## Shooting checklist (one visit, about 1 hour)

- [ ] Car washed and dried, same colour all day, no number plate or a Fakto plate
- [ ] Showroom lights on, forecourt clear of other cars for the 360
- [ ] Phone: landscape, 4K 30fps, lens cleaned, focus/exposure locked (long-press)
- [ ] Shots 1–5, 3 takes each, plus 10 s of silent room tone
- [ ] 6 stills: front 3/4, side, rear 3/4, rear, interior, dashboard (for the end card and the AI prompts)
- [ ] Upload everything to `assets/raw/` (or send me a link)

## Assets

| Asset | Status |
|---|---|
| Fakto + Nissan logos (from faktoauto.lt) | `assets/fakto-logo.svg`, `assets/nissan-logo.svg` |
| Official reference photos (press previews, low-res, storyboard only) | `assets/ref/` |
| Your footage + stills | needed |
| WLTP figures for the version shown | needed (nissan.lt / Fakto) |
| Showroom address line for the end card | needed |
| Music | I pick 2–3 free options for you to choose from |
