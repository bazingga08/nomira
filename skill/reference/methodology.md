# Methodology — Strategy, the Diamond, and Why This Beats Ad-Hoc Prompting

This file covers Stage 2 (strategy synthesis) and the design philosophy. Strategy
comes BEFORE words. No name is generated until the frozen strategy object exists.

---

## Core beliefs (hold these the whole way)
- **The best names don't describe reality; they change it.** Bias away from
  descriptive/generic names toward suggestive, arbitrary, and (gated) coined names.
- **"Surprising, but surprisingly familiar."** Every finalist must be BOTH distinctive
  AND instantly decodable on first hearing.
- **Polarization is a BUY signal.** Pentium, Azure, BlackBerry were all initially
  rejected internally. Discomfort is not a cut reason.
- **Name to the customer's emotion/belief problem, not the mechanism.** (BlackBerry
  named the email-anxiety problem, not the radio hardware.)
- **Sound carries meaning.** Phonemes encode size, speed, luxury, shape — engineer
  them on purpose against the ONE hero attribute.
- **A .com is not a veto.** Secure the name; the domain can be prefixed or alt-TLD.

---

## The Diamond (frozen strategy object)
Synthesize the brief into four locked answers:
1. **What do we WIN?** The ultimate business objective the name serves (future desired
   behavior/experience, not today's mission statement).
2. **What do we HAVE TO WIN?** Non-negotiable battles — the category you must compete in.
3. **What do we NEED TO WIN?** The specific perceptual territory / gap to capture.
4. **What do we NEED TO SAY?** The single message the name must communicate.

The Diamond plus the hero attribute, Aaker personality, territories, and derived
phonetic profile form the IMMUTABLE strategy object for the run.

---

## Hero attribute selection (the single most important output)
The name carries ONE attribute. If the brief lists several, force a ranking and pick
the top. **Lowrey-Shrum match rule:** the name's phonetics must connote this ONE
attribute and must NOT mismatch it — a phonetic mismatch actively LOWERS preference,
it is not merely neutral. One attribute, chosen deliberately, drives both generation
and scoring.

---

## Aaker's five brand-personality dimensions (pick exactly ONE)
- **Sincerity** — down-to-earth, honest, wholesome, cheerful (Hallmark, Coca-Cola).
- **Excitement** — daring, spirited, imaginative, up-to-date (Red Bull, MTV).
- **Competence** — reliable, intelligent, successful (IBM, Microsoft, Intel).
- **Sophistication** — upper-class, charming, glamorous (Chanel, Mercedes).
- **Ruggedness** — outdoorsy, tough, strong (Jeep, Levi's).

---

## Naming territories (3–6 strategic/emotional angles)
Each territory is a distinct conceptual direction to generate around. They guarantee
the generation space is covered mile-wide instead of clustering on one idea.
Example — a payments product: Trust/Security · Speed/Flow · Simplicity/Clarity ·
Global/Borderless · Human/Warmth.

---

## Attribute → phonetic-profile mapping (derive deterministically, then freeze)
Map the SINGLE hero attribute + Aaker personality to a target phonetic profile. This
is the typed contract that STEERS generation — not vibes. Full table in
`sound-symbolism.md`; the headline mappings:

| Hero attribute | Phonemes to favor | Examples |
|---|---|---|
| Fast / sharp / tech | front/high vowels /i/, voiceless stops p,t,k | Pentium, Kindle |
| Reliable / solid | voiced stops b,d,g, back vowels | BlackBerry, Hadoop |
| Luxury / premium | affricates tʃ/dʒ, late-acquired phonemes | Jaguar, Chanel |
| Calming / soft | sonorants m,l,n,r, rounded vowels | Aveeno, Lumen |

The profile is computed and FROZEN as a typed contract so generation is steered, not guessed.

---

## Lexicon-vs-better: the design philosophy
**Keep Lexicon's PROVEN FUNNEL as the immutable backbone** — Strategy → divergent
generation → convergent screening → validation — and improve only where Lexicon's
quality ceiling is set by HUMAN-RESOURCE limits, not the method itself.

### Follow Lexicon faithfully on:
1. **Strategy-before-words** — the Identify/Diamond gate; generation is refused until
   a single hero attribute, Aaker personality, and phonetic profile exist.
2. **Divergent/convergent split** — Invent is creative and judgment-banned; Implement
   (screening + scoring) is deterministic and repeatable.
3. **Sound symbolism as a first-class engine**, not a garnish — a generation driver
   AND an explicit scoring axis.
4. **Multi-dimensional screen with kill-switches** — a name can die on any axis.
5. **Generate-far-more-than-you-present** volume with a brutal, actually-culled funnel.
6. **Output as a strategy-tied presentation** with rationale, never a naked list.

### Improve where the caps are human, not methodological:
- **(A) Full linguistic + phonotactic screen on EVERY candidate EARLY** (Stage 4).
  Lexicon's 90-linguist network is expensive, so it screens LATE on survivors only;
  an AI inverts the funnel and kills disasters before anyone falls in love.
- **(B) Adversarial debate as a GUARANTEED, auditable phase** (Stage 5) — never-tired,
  never boss-anchored, no-anchor independent scoring + variance-triggered debate.
- **(C) Deterministic, editable-weight scoring** via `scripts/score.py` (Stage 6) —
  transparent, tunable, reproducible; not taste-by-fiat.
- **(D) Iterate the whole loop at near-zero marginal cost** — regenerate around
  winning veins and loop Stage 3↔6 many times before a human sees round 10. Naming
  becomes a near-exhaustive search, not a sampling problem.
- **(E) Category-reframing (the expansionist BlackBerry move)** and the three-team
  disguised-brief as DELIBERATE, always-run generators — not lucky accidents.
- **(F) Auto-triage + ask-then-infer + scale modes** so the skill self-scopes and
  never over-interrogates — capabilities a human kickoff meeting cannot guarantee.

### Critical honesty guardrails (where AI must NOT overclaim)
- Trademark/legal is the real chokepoint → produce a legally-PRE-VETTED shortlist that
  cuts attorney hours; label "pre-screen only — requires professional trademark
  search." Never a clearance opinion.
- Cross-linguistic safety → flag UNCERTAINTY and require native-source verification of
  finalists. Never assert certainty; never hallucinate "clean in language X."
- Sound symbolism is a ~60–75% probabilistic tendency (bouba/kiki ~70%), weighted
  lower for high-deliberation B2B. Never proof.
- The human strategist still chooses and sells internally. The skill is a
  force-multiplier, not a replacement for taste and buy-in.

**Net:** run the exact Lexicon process at 1000x search width, with the full screen on
every candidate and adversarial debate as default — faithful where the method is the
asset, improved where the bottleneck was merely human.
