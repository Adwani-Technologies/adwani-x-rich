# Adwani x Rich

Collaborative workspace for Jon and Rich's content and ecommerce projects.

## Projects

| Project | Description | Platforms |
|---------|-------------|-----------|
| [AI Influencer](./ai-influencer/) | SFW AI-generated social media content | Instagram, TikTok, Twitter |
| [Podcast Clips](./podcast-clips/) | Famous podcast clips for short-form content | YouTube Shorts, TikTok |
| [TikTok Commerce](./tiktok-commerce/) | Product content and sales | TikTok Shop |
| [Dropshipping](./dropshipping/) | Ecommerce stores | Shopify, etc. |

## Repository Structure

```
adwani-x-rich/
├── ai-influencer/           # AI Influencer project
│   ├── character/           # Character definition and style
│   ├── workflows/           # ComfyUI workflow files
│   ├── prompts/             # Prompt libraries
│   └── content-calendar.md
├── podcast-clips/           # Podcast clip content
│   ├── scripts/             # Editing scripts/templates
│   ├── clip-ideas.md
│   └── posting-schedule.md
├── tiktok-commerce/         # TikTok product sales
│   ├── products/
│   ├── scripts/             # Video scripts
│   └── content-calendar.md
└── dropshipping/            # Dropshipping stores
    ├── stores/              # Each store gets a subfolder
    └── product-research.md
```

## Shared Resources — Google Drive

Large files (images, videos, assets) are stored in shared Google Drive under "Adwani Technologies":

```
Adwani Technologies/
├── AI Influencer/
│   ├── Generated Images/
│   ├── Generated Videos/
│   └── Reference/
├── Podcast Clips/
│   ├── Raw Clips/
│   ├── Edited/
│   └── Posted/
├── TikTok Commerce/
│   ├── Product Photos/
│   ├── Videos/
│   └── Posted/
└── Dropshipping/
    ├── Product Images/
    ├── Store Assets/
    └── Supplier Info/
```

**Drive Link:** https://drive.google.com/drive/folders/1fl7aoTQ5EK_FowpB90CoPVGT3XOA1Yki

## Quick Start

```bash
# Clone the repo
git clone https://github.com/corleoneshow/adwani-x-rich.git
cd adwani-x-rich

# After making changes
git add .
git commit -m "Your commit message"
git push

# Get latest changes
git pull
```

## Key Rules

- **NEVER commit** generated images, videos, or large files — use Google Drive
- Pull before starting work (`git pull`)
- Check project-specific READMEs for workflow details

## Collaborators

- **Jon Adwani** (corleoneshow)
- **Rich Isho** (richardisho)
