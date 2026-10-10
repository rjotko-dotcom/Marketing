---
name: new-project
description: Start marketing for a new project. Use when the user says "new project", "start marketing for X", "set up X", or names a product that has no folder under projects/ yet. Interviews for the brief, creates projects/<slug>/ from the template, and proposes the first three moves.
argument-hint: "[project name] [link or one-line description]"
---

# New project

1. Pick a short lowercase slug (`bela-gym`, `bela-cryptobot`). If `projects/<slug>/` exists, stop and open it instead.
2. Copy `projects/_template/` to `projects/<slug>/`.
3. Fill `brief.md`. Read what you can first (the link, the repo's README, the store page) and only ask the user for what is still empty. Ask at most five questions in one message; the essentials are: who it's for, the 90-day goal (one number), budget, markets/languages.
4. Fill `brand.md` from existing material (app colours, logo, screenshots). Leave a field blank rather than invent it.
5. Propose the first three moves, each with channel, effort, cost and the number it should move. Prefer cheap and measurable: one organic channel the audience already uses, one piece of reusable creative, one way to measure (UTM links, store analytics).
6. Commit the folder.

Rules:
- Never invent proof (user counts, reviews, results). Proof comes from `brand.md` → Proof.
- Money, health or finance products: write the no-go claims into the brief's Rules row before writing any copy (see CLAUDE.md).
