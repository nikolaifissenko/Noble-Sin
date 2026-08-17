# Production Pipeline: Preprod → Studio → AI Mix/Master → Commercial Master

> Goal: take preprod arrangements to a commercial, loudness-viable release without paying for full manual mix/master time. Applies to the September 2026 singles and any future release.

---

## 1. PREPROD (before booking studio time)

- Finalize arrangement, tempo map (with tempo automation if not a strict click), key, and song structure. Changes made after tracking cost money and studio hours — lock this first.
- Build a rough mix/reference of the preprod (even programmed drums + scratch vocal) so the engineer and the AI tools later have a target to match.
- Pick 1–2 commercial reference tracks (same genre, similar energy). These get fed into the AI mastering tool later for tonal/loudness matching.

---

## 2. STUDIO DAY — record only what AI can't fake well

- **Drums**: track live/multi-mic in a real room (kick in/out, snare top/bottom, OH, room). This is what AI mixing tools handle best when given clean, well-recorded stems. Bad stems = bad AI mix — don't skimp on mic placement.
- **Vocals**: comp 3–5 takes per section, track dry with a clean signal chain (no committed effects), pop filter, consistent mic distance. AI pitch/tuning tools work far better on clean, well-gained takes.
- **Guitars/bass**: keep preprod takes if DI/amp-sim quality is already good. Re-amp for a better tone rather than re-tracking.

---

## 3. AI MIXING / MASTERING

### Mixing
- iZotope Neutron (per-track balance/EQ/dynamics assistant) gets an ~80% mix from stems in minutes.
- Always do a manual pass after (vocal rides, effects sends, arrangement automation) — don't trust full auto-mix blind. Spot-check against the reference track.

### Mastering
- iZotope Ozone's Master Assistant, fed the reference track, gives a strong starting master.
- Run 2–3 variants (different target loudness/intensity), A/B against the reference by ear, not just by meter.

### Tool cost comparison

| Tool | Model | Cost |
|---|---|---|
| BandLab Mastering | Free, unlimited | $0 — good for scratch/reference masters, not final commercial grade |
| CloudBounce | Per-track or subscription | ~€5–10/track, or ~€15/mo unlimited |
| eMastered | Subscription (needed to download) | ~$12–20/mo unlimited |
| LANDR | Free tier (watermarked/low-res) or subscription | Creator ~$12–25/mo unlimited, Pro ~$25/mo adds distribution extras |
| **iZotope Ozone** (Standard/Advanced) | **One-time purchase, plugin you own** | **~$130–250 on sale** (watch for frequent 50%+ off sales), Elements ~$30 |
| Waves AI mastering plugins | One-time purchase (frequent sales) | ~$30–100 depending on bundle/sale |

**Decision for Noble Sin**: since releases are recurring (multiple singles per year, not a one-off), buy Ozone once rather than renting a subscription service indefinitely. It also pairs with Neutron for the mixing step, so one purchase covers unlimited mixing + mastering forever. Use BandLab's free tier for quick scratch masters during preprod/pre-studio decisions.

---

## 4. EXPORT & FINISH WORKFLOW

1. Mix down in the DAW with headroom — **no limiter/maximizer on the master bus**, peaks around **-6dB**, no clipping.
2. Export **WAV, 24-bit, same sample rate as the session** — don't dither or convert yet.
3. **If using Ozone**: load as a plugin (or standalone) on the exported WAV, feed the Master Assistant the reference track, target loudness below, tweak, then export.
   **If using an online service** (LANDR/eMastered/CloudBounce): upload the WAV directly, pick style/reference if offered, download the mastered file.
4. Sanity-check the result against the reference track by ear, and on multiple playback systems (phone speaker, headphones, car) before sending to distribution.
5. Export final deliverables:
   - **WAV 24-bit** — archive master
   - **WAV 16-bit / 44.1kHz, dithered** — for distribution, if the distributor doesn't auto-convert

**Rule**: never export a mixdown that's already loud/limited. Mastering tools (AI or human) need headroom — a pre-limited mix distorts or gets squashed further.

---

## 5. LOUDNESS TARGETS

- Streaming platforms (Spotify, Apple Music, YouTube) normalize to roughly **-14 LUFS integrated** (Spotify -14, Apple Music -16, YouTube -14). Mastering hotter than that just adds distortion for nothing, since the platform turns it back down.
- Target **-9 to -11 LUFS integrated, true peak ≤ -1dBTP** at the master stage — current alt-rock commercial norm. Let streaming normalization handle the rest; ask the AI mastering tool to target LUFS explicitly rather than "loudest possible."

---

## 6. ASSET CHECKLIST TIE-IN

Once a track clears this pipeline, it feeds directly into `releases/single_rollout_template.md` → **Assets Checklist** → "Final master (WAV)".
