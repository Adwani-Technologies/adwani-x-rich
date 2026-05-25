# Adwani x Rich — Claude Instructions

## FIRST THING EVERY SESSION
1. Run `git config user.name` to find out who is currently working
   - richardisho = Richie, corleoneshow = Jon
2. Run `git pull` to get latest changes including any inbox messages
3. Check `.claude/inbox/` for messages addressed to the current user — look for files matching `*-to-richie.md` (if Richie) or `*-to-jon.md` (if Jon). If any exist, display them clearly under a **Messages** header, then delete those files, commit, and push so the inbox stays clean.
4. Run `git log --all --pretty=format:"%h %an: %s (%ar)" -30` to get recent history
5. Find the last commits made by the OTHER collaborator (not the current user) and give a brief 2-3 sentence summary of what they did and when. Keep it casual.

## What This Is
A collaborative workspace between Rich (richardisho) and Jon (corleoneshow) for multiple content and ecommerce projects:

1. **AI Influencer** — SFW AI-generated social media content (Instagram, TikTok, Twitter)
2. **Podcast Clips** — Famous podcast clips for YouTube Shorts/TikTok
3. **TikTok Commerce** — Product content and sales via TikTok Shop
4. **Dropshipping** — Ecommerce stores

## Collaborators
- **Jon Adwani** — corleoneshow on GitHub
- **Rich Isho** — richardisho on GitHub, richardisho@gmail.com

## Repo Structure
```
adwani-x-rich/
├── ai-influencer/           # AI Influencer (character, workflows, prompts)
├── podcast-clips/           # Podcast clips (scripts, clip ideas, schedule)
├── tiktok-commerce/         # TikTok commerce (products, scripts, calendar)
└── dropshipping/            # Dropshipping (stores, product research)
```

## Key Rules
- NEVER commit generated images, videos, or large files — these go to Google Drive only
- Always pull before starting work (`git pull`)
- Check project-specific READMEs for workflow details

## Branch Naming
- `richie/feature-name` — Richie's branches
- `jon/feature-name` — Jon's branches
- `shared/feature-name` — collaborative features either person can work on

## First-Time Setup (after cloning)
Run once to install git hooks that block accidental image/video commits:
```bash
bash scripts/install-hooks.sh
```

## Google Drive
Shared folder under "Adwani Technologies": https://drive.google.com/drive/folders/1fl7aoTQ5EK_FowpB90CoPVGT3XOA1Yki

Structure mirrors the projects:
- `AI Influencer/` — Generated images, videos, reference
- `Podcast Clips/` — Raw clips, edited, posted
- `TikTok Commerce/` — Product photos, videos, posted
- `Dropshipping/` — Product images, store assets, supplier info

## Project-Specific Notes

### AI Influencer
- Check `ai-influencer/character/style-guide.md` first — character consistency is everything
- Check `ai-influencer/character/lora-notes.md` for current model versions
- Proven prompts live in `ai-influencer/prompts/image-prompts.md`
- ComfyUI workflows exported as JSON go in `ai-influencer/workflows/`

### Podcast Clips
- Track clip ideas in `podcast-clips/clip-ideas.md`
- Posting schedule in `podcast-clips/posting-schedule.md`

### TikTok Commerce
- Product info in `tiktok-commerce/products/`
- Content calendar in `tiktok-commerce/content-calendar.md`

### Dropshipping
- Each store gets its own subfolder in `dropshipping/stores/`
- Product research tracked in `dropshipping/product-research.md`
