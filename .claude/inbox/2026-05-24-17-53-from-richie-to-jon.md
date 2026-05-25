---
from: richie
to: jon
date: 2026-05-24
---

Yo Jon — got the workflow fully set up. Here's everything you need to do to get up to speed.

---

## One-time setup (do this now)

**1. Install the git hooks**
Run this once from the project root — it stops you from ever accidentally committing images or model files:
```
bash scripts/install-hooks.sh
```

**2. Enable branch protection on main**
You're the repo owner so only you can do this:
- Go to github.com/corleoneshow/adwani-x-rich
- Settings → Branches → Add branch protection rule
- Branch name: `main`
- Check: "Require a pull request before merging"
- Save

---

## How we work now

**Branching**
- Your branches: `jon/feature-name`
- My branches: `richie/feature-name`
- Nothing goes directly to main — always open a PR

**PRs auto-fill** with a checklist (platform, Drive link, safety check). Just fill it in before requesting review.

**Google Drive auto-backup** — every push to main zips the repo and uploads it to our shared Drive folder automatically. Don't commit images, videos, or model files — those go to Drive manually.

---

## Shared Claude commands (the good stuff)

Open this project in Claude Code and you have access to:

- `/generate-post <platform> <vibe>` — generates a full post: caption, hook, hashtags, 2 alt versions. Reads the character style guide automatically.
- `/message richie <message>` — sends me a message that shows up at the start of my next Claude session

More commands coming as we build out.

---

## Every time you open the project

Claude Code will automatically:
1. Pull latest
2. Check your inbox for messages from me
3. Summarize what I've been working on since you were last in

Same happens on my end for your activity.

---

## Still needs both of us

Character bible (`character/style-guide.md`) is blank — we need to sit down and define who she is before the agents can generate on-brand content. Everything else is ready to go the moment that's filled in.

Lmk when you're set up. — Richie
