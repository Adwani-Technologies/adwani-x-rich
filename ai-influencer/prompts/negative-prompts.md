# Negative Prompts

Negative prompts to avoid common generation issues.

## Universal Negative Prompt

Use this as a starting base:
```
(worst quality, low quality:1.4), blurry, jpeg artifacts, watermark, text, logo, signature, username, cropped, out of frame
```

## Anatomy Fixes

```
bad anatomy, bad hands, missing fingers, extra fingers, fused fingers, too many fingers, mutated hands, malformed limbs, extra limbs, missing limbs, floating limbs, disconnected limbs, mutation, deformed, ugly, disfigured
```

## Face Fixes

```
bad face, ugly face, deformed face, asymmetrical face, cross-eyed, lazy eye, bad eyes, deformed eyes, extra eyes
```

## Body Fixes

```
bad body, deformed body, extra body parts, missing body parts, long neck, extra neck, bad proportions
```

## Style/Quality Fixes

```
cartoon, anime, 3d render, cgi, painting, drawing, illustration, sketch, unrealistic
```

## Clothing Fixes

```
bad clothing, deformed clothing, extra clothing, merged clothing
```

## Background Fixes

```
cluttered background, distracting background, bad background, ugly background
```

## Combined Templates

### Portrait (Clean)
```
(worst quality, low quality:1.4), blurry, bad anatomy, bad hands, bad face, deformed, ugly, watermark, text, cropped
```

### Full Body (Comprehensive)
```
(worst quality, low quality:1.4), blurry, bad anatomy, bad hands, missing fingers, extra fingers, bad face, deformed, disfigured, extra limbs, missing limbs, bad proportions, watermark, text, logo, cropped, out of frame
```

### Realistic Photo
```
(worst quality, low quality:1.4), cartoon, anime, 3d render, illustration, painting, drawing, blurry, bad anatomy, deformed, ugly, watermark, text
```

## Issue-Specific Additions

### If hands look bad, add:
```
bad hands, malformed hands, poorly drawn hands, mutated hands
```

### If eyes look off, add:
```
cross-eyed, lazy eye, asymmetrical eyes, different colored eyes (unless intended)
```

### If getting wrong style, add:
```
[unwanted style], [unwanted medium]
```

## Testing Notes

| Issue Encountered | Negative Added | Fixed? |
|-------------------|----------------|--------|
| | | |
