# Nissan X-Trail 2026 × Fakto Auto — results log

Newest first. What ran, what it cost, what happened, what we learned.

| Date | What | Spend | Result | Lesson |
|---|---|---|---|---|
| 2026-10-10 | Full 30 s ad v1 built from 24 official 2026 press photos: depth-parallax camera moves (CPU, unlimited) + 2 LTX AI clips + HTML titles/callouts + synthesised music | €0 | Rendered `xtrail-fakto-ad-30s-1920x1080.mp4` | The anonymous HF GPU allowance ran out after 2 clips, so tools/parallax.py (Depth Anything V2 Small on CPU) does the camera moves instead: ~10 s per clip, no limit, car never warps. Not yet in: Fakto showroom footage, WLTP figures |
| 2026-10-10 | First AI test clips from the official press photos (LTX-Video, free HF GPU, no login): forest drive + mountain push-in, joined into `ai-test-preview-1920x1080.mp4` | €0 | 2 clips OK and the car stays intact; 3rd (orbit) refused: anonymous allowance used up after 2 clips | Works without paying. Need HF_TOKEN for more clips per day; output is 896×512, so it's soft when scaled to 1080p. Wan 2.2 refuses anonymous calls |
| 2026-10-10 | Script + storyboard v2 (30 s, 16:9, no price) | €0 | Storyboard rendered; waiting on footage | Higgsfield needs its own paid credits (a Claude plan doesn't cover them; its free plan has 0 credits and no commercial use), so the realistic shots get filmed at Fakto and edited here |
