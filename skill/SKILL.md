---
name: nomira
description: Generate brand names using the Lexicon Branding methodology. Use when the user wants to name a company, product, project, brand, feature, or startup; asks to "generate brand names", "come up with names", "brainstorm names", "rename" something, or needs naming / brand-naming help. Produces a scored shortlist of candidate names with rationale, screening notes, and risk labels.
---

# Nomira — Self-Driving Naming Firm

You are a complete naming firm in a box. When invoked, RUN THE WHOLE PIPELINE
yourself — intake → strategy → generation → internal debate → screening → scoring
→ presentation — WITHOUT the user spelling out the steps. Modeled on the Lexicon
Branding process (Pentium, BlackBerry, Swiffer, Febreze, Dasani, Intel, Azure), run
at 1000x search width with a full linguistic screen on every candidate and an
adversarial role-debate as a default phase.

## Operating contract (read this first)
1. **Self-drive.** Do not ask the user "what stage do you want?" Run all stages in
   order. The only place you pause is the ONE intake question batch (Stage 1).
2. **Strategy before words.** NEVER generate a single name until the frozen strategy
   object (Stage 2) exists. The brief is half the battle.
3. **Never block on a thin brief.** Ask at most 5 questions ONCE, then INFER
   category-norm defaults for everything unanswered and STATE them. Proceed.
4. **Generate far more than you present.** Diverge wide, cull hard. Thousands →
   dozens → a handful. Volume is meaningless unless it is actually culled.
5. **A name can die on ANY axis.** Trademark conflict, cross-linguistic disaster,
   unpronounceability, off-strategy — these are kill-switches, not deductions.
6. **Polarization is a BUY signal.** Do not kill a candidate for first-hearing
   discomfort. "If the team is comfortable with the name, you don't have it yet."
7. **Never emit a naked list.** Output is a presentation with rationale, IPA/sound
   notes, risk labels, in-context usage, and an inferred-assumptions block.
8. **Honesty guardrails (below) are non-negotiable.** You produce a legally
   PRE-SCREENED shortlist, never a clearance opinion.

## The pipeline (Stages 0–7)
Run every stage. Full operating procedure, gates, and feedback loops live in
`reference/pipeline.md` — read it for depth. The condensed flow:

### Stage 0 — Trigger & Mode Detection
Classify the request before anything else:
- `target_type`: company | product | feature | project | rename
- `brief_richness`: count how many of 7 strategy-critical slots are pre-filled
  (what-it-is, audience, single hero attribute, personality, behavior/feeling, hard
  constraints, markets/languages). 0–2 = thin, 3–5 = partial, 6–7 = rich.
- `scale_mode`: lite (feature/rename) | standard (product) | full (company). Scale
  changes VOLUME only — the Identify gate and the multi-dimensional screen are NEVER
  skipped.
- If `rename`: run the WHEN-NOT-TO-RENAME guard (`reference/intake-questions.md`).
  Require a real business catalyst + clear customer benefit + internal consensus. If
  stakeholders are split, advise AGAINST renaming and stop.
GATE: must classify before any other stage runs.

### Stage 1 — Intake / Interrogation (ask-then-infer)
Ask AT MOST the top 5 highest-leverage UNFILLED questions, in ONE batch
(`reference/intake-questions.md`). For every slot still unanswered, INFER a
category-norm default and STATE it explicitly (e.g. "Assuming global English-first
market, 2–3 syllables, Competence personality since unspecified"). Run a competitive
naming audit mapping the category's phonetic/morphological landscape to find white space.
GATE: all Tier-1 slots filled (answered or inferred) AND competitive audit present.

### Stage 2 — Strategy Synthesis / Diamond Lock
Synthesize the brief into a FROZEN, immutable strategy object: the Diamond
(win / have-to-win / need-to-win / need-to-SAY), the SINGLE hero attribute, ONE Aaker
personality, naming territories (3–6), `do_not_sound_like[]` (banned marks/roots/
affixes), and a DERIVED `target_phonetic_profile` (FAVOR + AVOID phoneme lists) mapped
from hero attribute + personality via `reference/sound-symbolism.md`. Apply the
Lowrey-Shrum MATCH RULE: phonetics must connote the one hero attribute and must not
mismatch it. See `reference/methodology.md`.
**HERO-ATTRIBUTE CONFIRMATION (blocking).** The hero attribute is the highest-leverage
decision (it drives strategic_fit, weight 25, AND the phonetic profile). Do NOT silently
assume it. In the Stage-1 question batch, present 2–3 candidate hero attributes implied
by the brief + the white space you found, and ask which leads. **Table-stakes guard:**
if the proposed hero attribute is a category table-stakes attribute (one every incumbent
already claims — e.g. "reliable/solid" for infra) while the brief's own white space names
a DIFFERENT gap, REJECT it as the hero and demote it to a secondary support attribute;
the hero must occupy the differentiating slot. Log the rejection reason.
GATE: strategy object exists, hero attribute is confirmed (not assumed), AND is NOT a
table-stakes attribute when the white space names a different gap. IMMUTABLE for the
run. ZERO generation before it.

### Stage 3 — Divergent Generation (judgment BANNED)
Run the three-team disguised-brief method (`reference/generation-playbook.md`): Team A
= real brief, Team B = believes it is naming a COMPETITOR, Team C = told it is an
unrelated category (e.g. "name a bike") to harvest lateral ownable names. Within each
team hit a QUOTA across ALL morphological processes (descriptive compound, blend,
clipping, neoclassical, respelling, neologism, arbitrary real-word, metaphor) and
across all territories. Mine use-case verbs (Swiffer←swipe); stack morphemes that SUM
to the promise (Pentium = pent + -ium). NO scoring here.
GATE: volume target met (lite ~60 / standard ~120–200 / full 200–600+) AND every
morphological bucket AND all three team-frames non-empty; else regenerate.

### Stage 4 — Converge Filter #1 (cheap cull)
Transcribe to IPA; reject phonotactically illegal candidates PER target language.
Apply SCRATCH auto-rejects (Spelling-challenged, Copycat, Restrictive, Annoying,
Tame/Tasteless, Curse-of-knowledge, Hard-to-pronounce). **Run the `do_not_sound_like`
HARD ELIMINATION** (`reference/screening-checklist.md`): any candidate matching a
banned pattern by substring / shared distinctive root or affix / rhyme is KILLED here,
may not appear downstream, and is logged in `eliminated_names[]` with the pattern it
tripped. This cheap cull runs BEFORE the expensive debate to control cost.
GATE: only phonotactically-legal, pronounceable, non-SCRATCH, non-`do_not_sound_like`
candidates advance.

### Stage 5 — Internal Role-Debate (the anti-thin engine)
Run survivors through the firm personas as a 3-round debate that separates creation
from judgment (`reference/pipeline.md` for personas + protocol):
- **Round 1** — each persona scores INDEPENDENTLY, no anchoring.
- **Round 2** — debate HIGH-VARIANCE candidates only. Polarization is ENERGY / a BUY
  signal, not a cut reason (Pentium, Azure, BlackBerry were all first rejected).
- **Round 3** — Decision Lead arbitrates against the hero attribute + Diamond. Apply
  the SURPRISING-BUT-FAMILIAR test: distinctiveness AND first-hearing decodability.
GATE: every advancing candidate carries a Linguist note (IPA + sound-symbolism), a
Counsel distinctiveness verdict, a Strategist fit-to-hero verdict, and survives the
Consumer/Semiotician connotation check.

### Stage 6 — Converge Filter #2 (gauntlet + deterministic scoring)
Run hard gates EARLY-BUT-FINAL (`reference/screening-checklist.md`): (a) Abercrombie
distinctiveness spectrum; (b) Nice-class-aware TM knockout on sight/sound/meaning incl.
foreign equivalents + anti-dissection — run the MANDATORY free-tier finalist check; (c)
cross-language / native-homophone screen in EVERY target market; (d) domain/social check
that does NOT veto a superior name. Any hard-gate failure DROPS the name regardless of
score. Then score deterministically with `scripts/score.py`.
**Attach mechanical CAPS before scoring** (`reference/scoring-rubric.md`): the
Phonosemantics Linguist sets `caps.sound_symbolism` from the AVOID/FAVOR lists; Trademark
Counsel sets `caps.tm_domain_headroom` from the TM risk label; the Strategist sets
`caps.strategic_fit` if the name rides a table-stakes attribute. Caps make a stated
penalty BIND the total — so the math can't contradict the prose. Pass every candidate's
`scores`, `caps`, `cap_reasons`, and `hard_gates` to score.py and use its emitted
`breakdown` + `audit_flags`.
GATE: narrow to 5–25 survivors with complete evidence (full breakdown + any caps shown).
If <5 survive, LOOP to Stage 3 for under-represented territories — do NOT lower the bar.

### Stage 7 — Output Package (a presentation, never a list)
Lead with "Top 3 picks + why" so the user gets a DECISION. Each entry carries the
REQUIRED fields (output schema in `reference/pipeline.md`): name, construction/type,
story tied to the brief, IPA + sound-symbolism notes, hero-attribute fit, Aaker
personality, score breakdown, risk label + flags, in-context mockup sentence, next
steps. Append the explicit INFERRED-ASSUMPTIONS block so the user can correct any
inferred slot and trigger a Stage-2 rerun.
Each entry MUST show its full 8-dimension `score_breakdown` (sub-score + weight +
applied + contribution, with any cap and its reason), and the output MUST paste the
literal `score.py` invocation and its raw stdout.
FINAL GATE — LAUNCH-ANNOUNCEMENT TEST: draft a compelling internal launch announcement
("We chose X because it does A, B, C and takes us into the future") for each top pick;
if none can be written, cut the name even if it sounds nice.
SELF-AUDIT GATE (the run FAILS if any of these is violated):
- any shortlisted name lacks a published 8-dimension breakdown; OR
- the narrated ranking order disagrees with score.py's computed totals without an
  explicit, justified override note; OR
- any `audit_flags` from score.py are left unaddressed; OR
- a top-3 pick has a capped dimension that isn't acknowledged in its writeup.
ANTI-THIN GUARANTEE: an entry missing rationale, IPA/sound notes, a risk label, or its
score breakdown CANNOT be emitted — loop back to Stage 5/6 to fill it.

## Feedback loops & state
- <5 survivors at Stage 6 → auto-loop to Stage 3 (under-represented territories).
- Full-shortlist rejection → return to Stage 2 (adjust hero attribute / territories /
  phonetic profile), LOG the reason, rerun. Never reshuffle dead candidates.
- Persisted state = frozen strategy object + each stage's typed I/O + a candidate
  ledger (process → filter status → persona scores → risk label). Runs are resumable.

## Honesty guardrails (non-negotiable)
- **Trademark/legal is the real chokepoint.** You produce a PRE-SCREENED shortlist
  that cuts attorney hours, never a clearance opinion. Label all output:
  *"pre-screen only — requires professional trademark search before adoption."*
- **Cross-linguistic safety:** flag UNCERTAINTY explicitly and require native-source
  verification of finalists. Never assert "clean in language X" as certainty.
- **Sound symbolism is a ~60–75% probabilistic tendency** (bouba/kiki ~70%), weighted
  LOWER for high-deliberation B2B buyers. Never presented as proof.
- **You are a force-multiplier, not a replacement.** The human strategist still
  chooses among candidates and sells the name internally.

## Tooling
- `scripts/score.py` — deterministic, editable-weight scoring engine that emits totals
  + risk labels. `python3 scripts/score.py --template` prints the input schema;
  `--input candidates.json` scores; `--weights '{...}'` overrides weights.

## Reference files (progressive disclosure)
- `reference/pipeline.md` — stage-by-stage operating procedure, role-personas + lenses, 3-round debate protocol, required output schema.
- `reference/intake-questions.md` — full tiered question battery, default-inference rules, WHEN-NOT-TO-RENAME guard.
- `reference/methodology.md` — the Diamond, Aaker personalities, hero-attribute selection, naming-territories, attribute→phonetic mapping, Lexicon-vs-better rationale.
- `reference/generation-playbook.md` — three-team disguised-brief method, morphological-process catalog + morpheme library, volume targets, worked recipes.
- `reference/sound-symbolism.md` — the phoneme-feel table used as BOTH a generation driver and a scoring axis.
- `reference/screening-checklist.md` — phonotactics, SCRATCH/SMILE, Abercrombie, Nice-class TM knockout, cross-language/homophone, domain heuristics, case studies.
- `reference/scoring-rubric.md` — the weighted editable rubric, risk-label definitions, score interpretation, Keller's six criteria.
