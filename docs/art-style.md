# House art style — Codecraft anthology

The visual language for AI-generated illustrations that replace the old
unowned Flickr photos. The goal is a **cohesive set**: 44+ images that look
like they belong to one professional anthology, not a grab-bag. Generated with
openart.ai; every resulting image is **owned with full rights** and recorded in
[`assets/CREDITS.yml`](../assets/CREDITS.yml).

## The style: editorial line illustration

Clean, minimalist, conceptual line art — think a refined technical-book chapter
opener or a *New Yorker* spot illustration, in the brand's warm palette.

- **Single-weight linework**, no sketchy/variable strokes.
- **Conceptual, not literal** — one clear metaphor, generous negative space.
- **Flat** — no gradients, drop shadows, or 3D.
- **No text or lettering** of any kind in the image.
- **Not photorealistic.**
- **Timeless**, calm, a little witty — matching the essays' voice.

### Palette (the brand)

| Role | Hex | Use |
|---|---|---|
| Linework | `#491705` | deep brown — the main lines (brand heading color) |
| Accent | `#914f37` | muted terracotta — one accent per image (brand link color) |
| Background | `#faf7f2` | warm off-white |
| Optional shade | `#765043` | sparingly, for a second subtle tone |

### The reusable **style suffix**

Append this to every prompt — it's what makes the set consistent. Only the
first clause (the concept) changes per image:

> `minimalist editorial line illustration, single-weight line art in deep brown (#491705) with one muted terracotta (#914f37) accent, warm off-white (#faf7f2) background, flat with no gradients or shadows, generous negative space, conceptual and timeless, centered, no text, no lettering, not photorealistic`

### Negative prompt (paste into openart.ai's negative field)

> `photograph, photorealistic, 3d render, text, words, letters, watermark, signature, busy, cluttered, gradient, drop shadow, neon, harsh colors, multiple accent colors`

### openart.ai settings

- **Aspect ratio:** 4:3 (most originals were landscape ~4:3). Use 1:1 for the
  few square ones.
- **Consistency tips:** keep the same model and sampler across the batch; if the
  tool supports a style reference or fixed seed family, reuse it so all 44 share
  a feel. Generate 2–4 per concept and keep the best.
- **Per-image prompts** live in [`assets/art-prompts.yml`](../assets/art-prompts.yml).

## The workflow

1. Open `assets/art-prompts.yml`; for each `status: pending` entry, paste its
   `prompt` (+ the negative prompt above) into openart.ai.
2. Save the chosen image to `assets/` using the entry's `filename`.
3. Run the localizer (a `generate`-aware pass of `apply_image_triage.py`, TBD)
   to rewrite the essay `<img src>` and record provenance in `CREDITS.yml`
   (origin: AI-generated; model: openart.ai; the prompt; rights: owned).

## Notes

- The `concept` clauses are **starting points** — tweak any that don't capture
  the essay's metaphor. A few were inferred from the essay title where the old
  caption was just a photo credit; those are flagged `review: true`.
- xkcd comics, the lone movie still, and other one-offs are **out of scope** for
  this style pass (a comic can't be restyled) — they get a separate
  drop/attribute/replace decision.
