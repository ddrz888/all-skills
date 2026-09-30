# Infographic Builder — API Reference

## KIE AI API Details

### Base URL
`https://api.kie.ai/api/v1`

### Authentication
- Header: `Authorization: Bearer <KIE_API_KEY>`
- Key source: `.env` file (`KIE_API_KEY=...`)
- Manage keys: https://kie.ai/api-key

### Create Task

**Endpoint:** `POST /jobs/createTask`

**Headers:**
- `Authorization: Bearer <KIE_API_KEY>`
- `Content-Type: application/json`

**Request Body:**
```json
{
  "model": "nano-banana-pro",
  "input": {
    "prompt": "string (required, max 10,000 chars)",
    "image_input": ["url1", "url2"],
    "aspect_ratio": "3:4",
    "resolution": "2K",
    "output_format": "png"
  }
}
```

**Parameters:**

| Field | Required | Default | Options |
|-------|----------|---------|---------|
| `model` | Yes | — | `"nano-banana-pro"` |
| `input.prompt` | Yes | — | Max 10,000 characters |
| `input.image_input` | No | `[]` | Up to 8 images (JPEG/PNG/WebP, max 30MB each) |
| `input.aspect_ratio` | No | `"1:1"` | `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `auto` |
| `input.resolution` | No | `"1K"` | `1K`, `2K`, `4K` |
| `input.output_format` | No | `"png"` | `png`, `jpg` |

**Response (success):**
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "taskId": "task_nano-banana-pro_1765178625768"
  }
}
```

### Query Task Status

**Endpoint:** `GET /jobs/recordInfo?taskId={taskId}`

**Headers:**
- `Authorization: Bearer <KIE_API_KEY>`

Poll this endpoint every 5 seconds until the task status indicates completion. The response will include the generated image URL when ready.

### Check Credits

**Endpoint:** `GET /user/credits`

**Headers:**
- `Authorization: Bearer <KIE_API_KEY>`

### Pricing

| Resolution | Cost |
|-----------|------|
| 1K–2K | $0.09 / image (18 credits) |
| 4K | $0.12 / image (24 credits) |

## AIS Brand Reference

### Colors

| Name | Use |
|------|-----|
| Blue | Primary brand color |
| Dark Blue | Backgrounds, depth |
| Medium Blue | Secondary elements |
| Teal | Accent, highlights |
| White | Text, contrast |
| Dark Grey | Background base |
| Light Grey | Subtle elements |
| Orange | Call-to-action accent (use sparingly) |

### Typography

- **Primary:** Montserrat Light
- **Secondary:** Roboto Mono Medium (code/data only, not for infographics)

### Style

- Dark backgrounds
- Clean, modern lines
- Line-art iconography style
- Rounded button style
- Blue outer glow on the logo

### Logo Rules

- Always place in top-left corner
- Use the exact PNG from `brand-assets/AIS Logo PNG.png`
- Do not recreate, redraw, or stylize the logo
- Maintain clear space around the logo (handled by the overlay script's padding parameter)

## Logo Overlay Script

**Location:** `scripts/infographic-builder/overlay_logo.py`

**Usage:**
```bash
python scripts/infographic-builder/overlay_logo.py <base_image> <logo_image> <output_image>
```

**Parameters (configurable in code):**
- `padding`: Pixels from top-left corner (default: 20)
- `logo_scale`: Logo width as fraction of image width (default: 0.15 = 15%)

**Requirements:** Python 3 + Pillow (`pip install Pillow`)
