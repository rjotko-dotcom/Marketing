# Marketing

Marketing for new projects — briefs, brand, launch plans, content, ads and results, one folder per project, worked on with Claude Code.

## How to use

Open this repo in Claude Code (desktop, web or CLI) and just ask, for example:

- "new project: B.E.L.A gym app" → creates `projects/bela-gym/` and fills the brief
- "who are the competitors" → `competitors.md` with sources
- "launch plan for 1 December" → dated plan + calendar
- "10 TikTok ideas for this week, in Lithuanian" → posts in the calendar
- "make 4 Meta ad variants" → angles, copy, images via Higgsfield
- "weekly review" + paste your numbers → what to stop / keep / try

Repo skills (in `.claude/skills/`): `new-project`, `competitor-scan`, `launch-plan`, `social-posts`, `video-script`, `ad-creative`, `weekly-review`.

## One-time setup: Higgsfield (images & video, many models)

Higgsfield's official skills (`higgsfield-generate` and seven more) give Claude image, video, audio and 3D generation across their whole model catalogue under one account. They use the Higgsfield CLI.

**Claude Code on your PC:**

```bash
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
higgsfield auth login
```

Then inside Claude Code:

```
/plugin marketplace add higgsfield-ai/skills
/plugin install higgsfield@higgsfield
```

**Claude on the web / desktop chat:** Settings → Connectors → Add custom connector → `https://mcp.higgsfield.ai/mcp`, then sign in.

Generations use your Higgsfield credits.

## Recommended plugins

From the official Anthropic plugin directory (`/plugin marketplace add anthropics/knowledge-work-plugins`):

- `marketing` — campaign plans, content drafts, SEO audit, email sequences, performance reports, brand review
- `brand-voice` — keeps every piece in the project's voice
- `design` — design critique and handoff
