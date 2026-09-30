---
name: infographic-builder
description: Use when creating an infographic, designing a visual explainer, making an educational infographic, or generating infographic images. Produces branded PNG infographics using KIE AI.
---

## What This Skill Does

Generates educational infographic images using KIE AI's nano banana pro model. Every infographic follows AIS brand guidelines and includes the AIS logo in the top-left corner.

## Context

Before generating, read these files:

1. `brand-assets/AIS Brand Guidelines-1.png` -- Brand colors, typography, and style rules
2. `brand-assets/AIS Logo PNG.png` -- The AIS logo (placed in top-left of every infographic)

For full API reference and parameters, see [reference.md](reference.md).

### Brand Rules (Always Apply)

- **Font:** Montserrat (primary)
- **Colors:** Blue (#0077FF range), Dark Blue, Teal, White, Medium Blue, Dark Grey, Light Grey, Orange (accent)
- **Style:** Dark background, clean lines, modern iconography
- **Logo:** AIS logo in top-left corner of every infographic, exactly as provided
- **Content:** Minimal text. Visually pleasing and easy to look at. NOT wordy.

## Step-by-Step Workflow

### Step 1: Understand the Request

Ask the user what topic they want the infographic to cover. If they already stated it, skip this step.

### Step 2: Craft the Image Prompt

Write a detailed prompt for nano banana pro that includes:

1. The educational topic and key visual concepts
2. Explicit style instructions:
   - "Professional infographic design with a dark background"
   - "Color palette: blues (#0077FF, dark blue, medium blue), teal accents, white text, dark grey background"
   - "Modern, clean design with clear visual hierarchy"
   - "Montserrat font style for any text"
   - "Minimal text -- use icons, diagrams, and visuals to convey information"
   - "Educational and easy to understand at a glance"
   - "Leave the top-left corner area clear for a logo overlay"
3. Do NOT ask the AI to draw the AIS logo -- it will be composited separately

### Step 3: Call the KIE AI API

Make a POST request to create the image generation task:

```bash
curl -X POST "https://api.kie.ai/api/v1/jobs/createTask" \
  -H "Authorization: Bearer $KIE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nano-banana-pro",
    "input": {
      "prompt": "<crafted prompt from Step 2>",
      "aspect_ratio": "1:1",
      "resolution": "2K",
      "output_format": "png"
    }
  }'
```

The API key is stored in `.env` as `KIE_API_KEY`. Read it with:
```bash
source .env 2>/dev/null || export KIE_API_KEY=$(grep KIE_API_KEY .env | cut -d= -f2)
```

### Step 4: Poll for Results

Poll the task status every 5 seconds until complete:

```bash
curl -s "https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>" \
  -H "Authorization: Bearer $KIE_API_KEY"
```

Wait for the response to contain a completed status and an image URL.

### Step 5: Download the Image

Download the generated PNG from the returned URL:

```bash
curl -o "projects/infographic-builder/<topic-slug>-base.png" "<image_url>"
```

### Step 6: Overlay the AIS Logo

Run the logo overlay script to place the AIS logo in the top-left corner:

```bash
python scripts/infographic-builder/overlay_logo.py \
  "projects/infographic-builder/<topic-slug>-base.png" \
  "brand-assets/AIS Logo PNG.png" \
  "projects/infographic-builder/<topic-slug>.png"
```

This composites the logo exactly as-is onto the top-left corner of the infographic.

### Step 7: Present the Result

1. Show the user the final infographic by reading the output file
2. Tell them the file is saved at `projects/infographic-builder/<topic-slug>.png`
3. Ask if they want any adjustments (different aspect ratio, different style emphasis, etc.)

## Output Format

- **File:** `projects/infographic-builder/<topic-slug>.png`
- **Naming:** Lowercase, hyphenated topic slug (e.g., `how-dns-works.png`)
- **Base file** (without logo) is kept as `<topic-slug>-base.png` in case of re-compositing

## Notes

- **No NSFW content.** All prompts must be educational and appropriate.
- **Minimal text.** Infographics should communicate through visuals, icons, and diagrams -- not paragraphs of text.
- **Always use Montserrat** as the font reference in prompts (not Roboto Mono).
- **Always leave top-left clear** in the AI prompt so the logo overlay looks clean.
- **Cost:** ~$0.09 per image at 2K resolution. No confirmation needed before generating.
- **Aspect ratio default:** 1:1 (square). Can be changed per request.
- **Resolution default:** 2K. Do not exceed 2K unless the user explicitly asks.
- If the Python overlay script is missing or fails, install Pillow (`pip install Pillow`) and try again.
- If the API returns an error, check the API key and retry once. If it fails again, report the error to the user.
