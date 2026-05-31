# Pipeline — Stage-by-Stage Operating Procedure

This is the full operating procedure for the self-driving naming run. SKILL.md is
the condensed map; this file is the depth. Run Stages 0–7 in order. Each stage has
typed inputs, typed outputs, and a GATE that must pass before the next stage runs.

---

## Stage 0 — Trigger & Mode Detection

**Input:** raw user request.
**Output:** `{intent_confirmed, target_type, brief_richness, rename_flag, scale_mode}`.

Score how many of the 7 strategy-critical slots are pre-filled in the request:
what-it-is, audience+buyer-condition, single hero attribute, personality,
behavior/feeling, hard constraints, target markets/languages.
- 0–2 filled → `thin` → ask the full top-5 battery.
- 3–5 filled → `partial` → ask only the highest-leverage gaps.
- 6–7 filled → `rich` → confirm in one line and proceed.

Map size → `scale_mode`: a feature rename = `lite` (scaled-down volume); a product =
`standard`; a company/brand = `full`. Scale only changes generation VOLUME. The
Identify gate (Stage 2) and the multi-dimensional screen (Stages 4/6) are NEVER skipped.

If `rename_flag`: run the WHEN-NOT-TO-RENAME guard (see `intake-questions.md`).

**GATE:** classification complete. No other stage runs before this. (Lexicon has no
auto-triage; a skill must self-scope — this stage is a pure improvement.)

---

## Stage 1 — Intake / Interrogation (ask-then-infer)

**Input:** `brief_richness` + raw request.
**Output:** filled brief slots tagged `source=USER_ANSWERED|INFERRED`, a written
naming brief, a competitive naming audit.

1. Ask AT MOST the top 5 unfilled questions from the battery, highest-leverage first,
   in ONE batch (`intake-questions.md`). Never trickle questions across turns.
2. For every slot still unanswered after the answer (or if the user says "just go"),
   INFER a category-norm default and STATE it. Never block on a thin brief.
3. Competitive naming audit: map the category's phonetic/morphological texture (the
   "first hundred names competitors already tossed around") to locate white space —
   which sounds/structures are crowded, which are open.

**GATE:** all Tier-1 slots filled (answered or inferred) AND a competitive audit exists.
The hard 5-question cap + ask-then-infer kills death-by-questionnaire AND the
vague-brief failure simultaneously — something a human kickoff meeting cannot guarantee.

---

## Stage 2 — Strategy Synthesis / Diamond Lock

**Input:** filled brief + competitive audit.
**Output:** a FROZEN, immutable strategy object:
```
{
  diamond: { win, have_to_win, need_to_win, need_to_SAY },
  single_hero_attribute,
  target_personality,            # one Aaker dimension
  name_objectives[],
  naming_territories[],          # 3-6 strategic/emotional angles
  target_phonetic_profile,       # derived deterministically
  competitor_phonetic_landscape, do_not_sound_like[],
  target_market_languages[],
  nice_classes[],
  scoring_rubric_weights         # editable
}
```
Derive `target_phonetic_profile` by mapping the SINGLE hero attribute + Aaker
personality to phonemes via `sound-symbolism.md`. Apply the Lowrey-Shrum MATCH RULE:
phonetics must connote the one hero attribute and must NOT mismatch it (a mismatch
actively lowers preference). See `methodology.md` for the Diamond + mapping detail.

**GATE:** strategy object exists and is IMMUTABLE for the run. Any later stage that
needs to change it RESTARTS here with a logged reason. ZERO generation before it.
The phonetic profile is computed deterministically and frozen as a typed contract, so
generation is steered, not vibes-based.

---

## Stage 3 — Divergent Generation (judgment BANNED)

See `generation-playbook.md`. Three teams (A=real, B=competitor, C=unrelated
category), quota across all 8 morphological processes and all territories, volume
per `scale_mode` (lite ~60 / standard ~120–200 / full 200–600+). No scoring or
rejecting here. 8+ deterministic lenses at near-zero marginal cost cover strategic
territory a time-boxed human team would prune away early — turning a sampling problem
into a near-exhaustive search.

**GATE:** volume met AND every morphological bucket non-empty AND all three team
frames non-empty; else regenerate the empty buckets only.

---

## Stage 4 — Converge Filter #1 (cheap cull)

See `screening-checklist.md` (phonotactics + SCRATCH). This CHEAP cull runs BEFORE
the expensive debate to control token/latency cost. Improvement on Lexicon: the full
cross-linguistic + pronounceability screen is applied to EVERY candidate early as a
generation-time filter (Lexicon's 90-linguist screen runs LATE, only on survivors,
because human screening is expensive) — disasters die before anyone falls in love.

**GATE:** only phonotactically-legal, pronounceable, non-SCRATCH candidates advance.

---

## Stage 5 — Internal Role-Debate

**Input:** filtered candidates + strategy object.
**Output:** annotated survivors with per-persona scores, objections, and verdicts.

### The role-personas (the firm in a box)

| Persona | Owns | Guards against |
|---|---|---|
| **Brand Strategist** (intake owner) | Diamond, positioning, territories, desired future behavior; judges fit to hero attribute | off-strategy cleverness |
| **Creative Namer Teams A/B/C** | high-volume divergent generation (judgment BANNED in their stage) | timid/literal/descriptive names; supplies lateral options |
| **Phonosemantics Linguist** | IPA, sound-symbolism MATCH vs profile, syllable/stress/rhythm, phonotactics, pronounceability | names that sound wrong for the attribute or are hard/illegal to say |
| **Global / Cross-cultural Linguist** | connotation + native-homophone + cultural-disaster checks in EVERY market; flags UNCERTAINTY; requires native verification of finalists | Pajero/Fitta-class disasters and hallucinated "clean in language X" claims; **hard veto** |
| **Trademark / IP Counsel** | Abercrombie placement, Nice-class knockout (sight/sound/meaning + foreign equivalents + anti-dissection), risk labels, clearance-before-presentation | undefensible/generic/conflict-risk names; produces a PRE-SCREEN, never a legal opinion |
| **Domain / Digital Strategist** | .com + social handles + acquisition strategy; no veto over a superior name | unfindable handles AND the ".com-or-nothing" trap; re-verifies finalists live |
| **Consumer Researcher** (audience proxy) | first-reaction + recall via competitor-test framing ("a competitor just launched as X — your reaction?"), never "do you like it" | names that blend into the category / test poorly because merely literal |
| **Semiotician** | Saussure/Peirce/Barthes layers, iconicity, 2nd-order connotation/myth vs positioning | names whose cultural connotation conflicts with the brief even when denotation fits |
| **Decision / Synthesis Lead** (chair) | aggregates scores, resolves debate, treats polarization as energy, writes per-name rationale, applies launch-announcement gate | premature consensus AND shipping a name with no story |

### The 3-round protocol (separates CREATION from JUDGMENT)
- **Round 1 — Independent scoring (no anchoring).** Each persona scores every
  candidate ALONE, blind to others. Kills groupthink and boss-anchoring.
- **Round 2 — Variance debate.** Compute cross-persona variance. Deep-debate ONLY
  high-variance candidates (cost control). Polarization is ENERGY / a BUY signal, not
  a cut reason (Pentium, Azure, BlackBerry were all initially rejected). Linguist vs
  Counsel vs Strategist vs Consumer-proxy argue it out.
- **Round 3 — Arbitration.** Decision Lead resolves each against the single hero
  attribute + Diamond. Apply the SURPRISING-BUT-FAMILIAR test: require BOTH
  distinctiveness AND first-hearing decodability.

Improvement on Lexicon: debate becomes a guaranteed, auditable, never-tired,
never-boss-anchored pipeline phase instead of a scarce, politically-loaded meeting.

**GATE:** each survivor carries a Linguist note (IPA + sound-symbolism), a Counsel
distinctiveness verdict, a Strategist fit-to-hero verdict, and passes the
Consumer/Semiotician connotation check.

---

## Stage 6 — Converge Filter #2 (gauntlet + deterministic scoring)

See `screening-checklist.md` for the hard gates and `scoring-rubric.md` +
`scripts/score.py` for scoring. Hard-gate failures DROP names regardless of score
(kill-switches, not deductions). Scoring is code-deterministic and rubric weights are
editable per brief, so shortlisting is defensible and tunable, not taste-by-fiat.

**GATE:** 5–25 survivors with complete evidence. If <5, loop to Stage 3 (do NOT
lower the bar). Label everything "pre-screen only — requires professional trademark
search before adoption."

---

## Stage 7 — Output Package

### Required output schema (per candidate — ANTI-THIN GUARANTEE)
An entry MISSING any required field below cannot be emitted; loop to Stage 5/6 to fill it.
```
{
  name,
  construction / name_type,         # e.g. "neoclassical blend (pent- + -ium)"
  story / rationale,                # tied explicitly to the brief + hero attribute
  ipa,                              # /ˈpɛn.ti.əm/
  sound_symbolism_notes,            # which phonemes carry the attribute + MATCH verdict
  hero_attribute_fit,
  aaker_personality,
  score_breakdown,                  # per-dimension sub-scores + total
  risk_label,                       # Strong / Caution-descriptive / Reject-generic / Conflict-risk
  flags,                            # TM/cross-language/domain notes; Nice class checked
  in_context_mockup,                # a real usage sentence / tagline / UI label
  next_steps
}
```

### Presentation structure
1. **Top 3 picks + why** first — give a DECISION, not a dump.
2. The rest grouped by territory or score.
3. Every name shown IN CONTEXT (mockup/sentence), never naked.
4. **Inferred-assumptions block** — list every slot tagged INFERRED so the user can
   correct one and trigger a Stage-2 rerun.
5. **Next action:** offer comprehensive professional TM clearance + a realistic-context
   consumer test (competitor-test framing, not "do you like it").

### FINAL GATE — Launch-Announcement Test
For each top pick, draft a compelling internal launch announcement ("We chose X
because it does A, B, C and takes us into the future"). If you cannot write a
compelling one, CUT the name even if it sounds nice.

The required-field schema + launch-announcement gate make thin output structurally
impossible.

---

## Feedback / state machine
- <5 survivors at Stage 6 → auto-loop to Stage 3 (under-represented territories).
- Full-shortlist rejection → return to Stage 2 (adjust hero attribute / territories /
  phonetic profile), LOG the reason, rerun. NEVER reshuffle dead candidates.
- Persisted state: frozen strategy object + each stage's typed I/O + a candidate
  ledger (process → filter status → persona scores → risk label). Makes runs
  resumable and auditable.
