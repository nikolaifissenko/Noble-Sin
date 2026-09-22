# Visual Identity — Reference: "Nebo" cover art

> Every photo edited for Instagram/social around this era must match this look. Don't post anything that breaks the grade or wardrobe rules below without a deliberate reason.

## Wardrobe
- White t-shirts/tanks + camo pants only
- No other colors, no visible logos/brands
- Silver jewelry only (chains, bracelets) — no gold, no color accents

## Styling
- Dirt/soot smudges on skin and clothing — deliberate, grungy, worn-in
- Hair natural/undone, not styled clean
- No smiling — flat, serious, intense expressions

## Composition
- Staggered diagonal line of subjects, front-to-back depth
- Arms crossed or neutral — no dynamic/action poses
- Industrial Rome backdrop (Gazometro Ostiense in the reference), uncluttered, no crowds

## Color grade
- Desaturated overall, not full B&W
- Cool cyan/blue in sky and shadows
- Warm golden tones in structure/midtones/skin — that cool/warm split is the signature
- Moderate contrast, slight matte/film grain finish
- Golden hour lighting, low sun angle, subjects slightly backlit

## Checklist before posting any new photo
- [ ] Wardrobe matches (white tops + camo, silver jewelry only)
- [ ] Grade has the cool-shadow/warm-midtone split, not neutral or oversaturated
- [ ] No smiling/casual poses that break the serious tone
- [ ] Background is industrial/urban Rome, not generic or busy
# Noble Sin — Visual Identity

## "Nebo" single era

- Gritty, desaturated look. Cool-blue / warm-gold split grade (shadows cool, highlights warm).
- Industrial Rome backdrop — Gazometro Ostiense specifically, not generic industrial.
- Dirt/grunge styling, camo + white tops on the band.
- Purpose: bridge the band's polished wordmark to a rougher, more "alternative rock" world without touching the mark itself.

## Logo decision (settled — do not re-open without a strong reason)

**Kept the original wordmark as-is**: flourished high-contrast serif, "NOBLE SIN" with SIN nested inside the O, white on flat black. It's distinctive and has existing recognition; not worth redesigning mid-rollout.

**Known weakness, accepted deliberately**: the typeface reads couture/fashion-editorial (Didone contrast, hairline strokes), not alternative rock. Several from-scratch redesigns were explored this session (bold industrial stencil, monumental serif with distressed SIN, elegant italic serif with a thorned vine) — all rejected. The tools available (system fonts + Python/PIL scripting, no real vector design software) can't produce letterforms that read as bespoke; every attempt looked like "a font with an effect," not a drawn mark. If the couture read genuinely becomes a problem, the fix is commissioning a real type designer to redraw the wordmark from scratch — not another scripted pass.

**The lever that's actually available**: what's behind the mark, not the mark itself.

## Background treatment rules

- Wordmark stays white, 100% opacity, Normal blend mode. No glow (glow reads couture/gothic, the opposite of the goal), no texture clipped into the letterforms.
- Legibility over a busy background is handled with a **scrim**: a blurred, dilated copy of the letter alpha mask, used to darken the zone immediately behind/around the letters while leaving the texture visible in open space. This is a compositing fix, not a style choice — keep it subtle.
- The mark is a wide/16:9-ish lockup (not square). It does not survive being cropped into a square avatar without clipping the flourishes — use the **O + nested SIN monogram** (crop of the existing mark, no redrawing) for anything small-format: profile picture, favicon, merch tag.

## Where each version is used

| Version | Use |
|---|---|
| Flat black (original) | Merch, one-sheet/EPK header, contracts/letterhead, anything that should outlive this single cycle |
| Nebo industrial texture (cool/warm dusk, defocused Gazometro-style) | General Nebo-era post templates, story headers, video intro/outro |
| Army-green / TTsKO camo | The specific military-themed single only — not the whole Nebo era |

## Current assets

`social/assets/logo/`
- `noblesin_nebo_industrial_vertical.png` — 1080×1920, Nebo-era industrial dusk background, Instagram Reels/Story ready
- `noblesin_armygreen_vertical.png` — 1080×1920, plain olive-drab variant
- `noblesin_ttsko_camo_vertical.png` — 1080×1920, TTsKO (Soviet/Russian 3-color amoeba camo — black-brown + dark green blotches on khaki, darkened and defocused), for the military-themed single

All three backgrounds are **procedural placeholders** (generated with Python/PIL noise + compositing, not real photography or a real camo asset). They're good enough to ship on social now; the Gazometro backdrop specifically is worth reshooting for real once there's time, since the location is what actually ties the mark to the era rather than "grunge in general."

## Open questions for next session

- If the military-themed single's lyrical content points to a specific era/unit rather than "military" in general, TTsKO (Cold War Soviet) may be the wrong pattern — Flora/VSR (post-Soviet Russian) or EMR/"Butterfly" (modern digital) are the alternatives, ask before assuming.
- No real Gazometro Ostiense photography has been shot yet — the industrial texture is synthetic.
