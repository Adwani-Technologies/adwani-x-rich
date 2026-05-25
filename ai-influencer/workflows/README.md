# ComfyUI Workflows

This directory contains ComfyUI workflow files for generating consistent content.

## Available Workflows

### portrait-workflow.json
**Purpose:** Generate portrait images of the character
**Use when:** Creating headshots, profile pics, close-ups
**Key settings:**
- Resolution:
- LoRA weight:

### video-workflow.json
**Purpose:** Generate video content or animated sequences
**Use when:** Creating TikToks, Reels, video clips
**Key settings:**
- Frame count:
- FPS:

## How to Use

1. Open ComfyUI
2. Drag and drop the JSON file onto the canvas (or use Load)
3. Update any necessary paths (models, LoRAs)
4. Adjust prompts as needed
5. Generate!

## Required Models

Make sure you have these installed before using workflows:

- **Checkpoint:** [Name] - get from shared Drive `Models/Checkpoints/`
- **LoRA:** [Name] - get from shared Drive `Models/LoRAs/`
- **VAE:** [Name]

## Customization

### Changing the Prompt
Look for the "CLIP Text Encode" node - this is where you edit prompts.

### Changing Resolution
Find the "Empty Latent Image" node and adjust width/height.

### Adjusting LoRA Strength
Find the "Load LoRA" node and adjust the strength values.

## Workflow Versions

| Workflow | Version | Last Updated | Changes |
|----------|---------|--------------|---------|
| portrait-workflow.json | 1.0 | [Date] | Initial |
| video-workflow.json | 1.0 | [Date] | Initial |

## Troubleshooting

### "Missing node" error
Install the required custom nodes: [list them]

### Outputs look different
Check that you're using the exact model/LoRA versions specified above.

### Out of VRAM
Try reducing resolution or batch size.
