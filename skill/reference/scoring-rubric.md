# Scoring Rubric — Stage 6

Scoring is DETERMINISTIC and REPEATABLE via `scripts/score.py` (the whole reason to
build a skill vs ad-hoc prompting). Weights are EDITABLE per brief — tune them in the
strategy object's `scoring_rubric_weights` and pass via the script. Each dimension is
sub-scored 0–10 per candidate; the script computes a weighted total 0–100 and a risk
label. Hard-gate failures are KILL-SWITCHES (zeroed + labeled), not deductions.

---

## The weighted rubric (defaults; editable)

| Dimension (score.py key) | Default weight | What it measures |
|---|---|---|
| `strategic_fit` | 25 | Does the name carry the ONE hero attribute + Diamond? |
| `sound_symbolism` | 15 | Do the phonemes MATCH the attribute (Lowrey-Shrum)? Mismatch scored low. |
| `distinctiveness` | 15 | Abercrombie strength + category white-space. |
| `pronounceability` | 10 | The "say-it / spell-it" stability test. |
| `memorability` | 10 | Sticky, not easily confused with rivals. |
| `tm_domain_headroom` | 15 | Pre-screen clearance likelihood + digital findability. |
| `smile` | 5 | Suggestive, Memorable, Imagery, Legs, Emotional. |
| `keller` | 5 | Keller's six brand-element criteria. |

Weighting guidance: raise **sound_symbolism** for impulse/consumer briefs; lower it
for deliberate B2B. Raise **tm_domain_headroom** when a clearable .com is required.

---

## Anchored bands (what a sub-score MEANS — no unanchored guessing)

Every 0–10 sub-score MUST be justified against these bands. A score with no band
justification is invalid. Bands keep two runs of the same brief consistent and stop
the rubric from being "theater."

| Score | Generic band meaning |
|---|---|
| **10** | Textbook-perfect on this dimension; nothing to improve. |
| **8** | Strong; a minor caveat at most. |
| **5** | Mixed / neutral; real upside and a real weakness. |
| **3** | Weak; a notable problem on this dimension. |
| **0** | Fails this dimension outright. |

### Per-dimension mechanical anchors (override the generic band)
- **`strategic_fit`** — 10 only if the name carries the SINGLE hero attribute AND sits
  in the named white-space slot. **Cap ≤6 if it expresses a TABLE-STAKES category
  attribute** (one every incumbent already claims) instead of the differentiating slot
  the Diamond named. Cap ≤3 if it is off-strategy/contradicts the Diamond.
- **`sound_symbolism`** — driven by the Stage-2 `target_phonetic_profile` FAVOR/AVOID
  lists (`reference/sound-symbolism.md`). **Hard cap ≤4 if the name contains ANY phoneme
  on the AVOID list** for the hero attribute. **Cap ≤6 if it misses the FAVOR onset
  class.** 8–10 only for a clean MATCH (favored onset + favored stressed vowel, no AVOID
  phonemes). Mismatch is a PENALTY (Lowrey-Shrum), never neutral.
- **`distinctiveness`** — anchored to Abercrombie: Fanciful 9–10 · Arbitrary 8 ·
  Suggestive 6 · Descriptive ≤3 · Generic 0 (also trips the hard gate).
- **`tm_domain_headroom`** — anchored to the TM risk label (see CAP table below).
- **`pronounceability`** — 10 = spelled correctly after one hearing; ≤4 if it fails the
  say-it/spell-it test in any target market.
- **`memorability`** — 10 = vivid + low-confusability; ≤4 if easily confused with a
  rival or instantly forgettable.
- **`smile`** — +2 each for Suggestive, Memorable, Imagery, Legs, Emotional present.
- **`keller`** — count of Keller's six criteria met, scaled to 0–10.

---

## Mechanical CAPS (passed to score.py as `caps` + `cap_reasons`)

Caps are how a STATED rule becomes a BINDING number. When a deterministic rule fires,
attach a cap; score.py enforces `applied = min(raw, cap)` so the penalty actually drags
the weighted total — it can't be narrated and then ignored.

**Sound-symbolism cap (set by the Phonosemantics Linguist):**
- name contains any AVOID-list phoneme for the hero attribute → `caps.sound_symbolism = 4`
- name misses the FAVOR onset class → `caps.sound_symbolism = 6`
- `cap_reason` must name the offending phoneme and the hero attribute.

**Strategic-fit cap (set by the Brand Strategist):**
- hero attribute = a table-stakes category attribute while the white space names a
  different gap → `caps.strategic_fit = 6`.

**Trademark cap (set by Trademark Counsel) — TM risk label → ceiling:**
| TM pre-screen risk | `caps.tm_domain_headroom` |
|---|---|
| Conflict-risk / named big-mark proximity (sight/sound/meaning) | **≤2** |
| Caution (same field, some distance) | **≤5** |
| Clear (no flagged collision) | up to 10 |

A flagged collision therefore MUST demote the name in the ranking, not just print a
footnote. `cap_reason` must name the colliding mark (e.g. "Wayfin↔Wayfair sight/sound").

---

## Hard gates (kill-switches, passed to score.py as `hard_gates`)
- `abercrombie_not_generic` — false → score 0, label **Reject-generic**.
- `tm_clear_prescreen` — false → score 0, label **Conflict-risk**.
- `cross_language_clean` — false → score 0, label **Conflict-risk**.

---

## Risk labels (emitted by score.py)
- **Strong** — passes all hard gates, high score, low pre-screen TM risk.
- **Caution-descriptive** — weak on Abercrombie (descriptive/surname/geographic) or a
  mid score; defensibility risk; usable but flag.
- **Reject-generic** — fails the Abercrombie generic gate. Cut.
- **Conflict-risk** — likely TM conflict on sight/sound/meaning, or a cross-language
  problem. Cut or flag hard.

---

## Score interpretation
- **80–100** — strong shortlist candidate.
- **60–79** — viable; note weaknesses.
- **40–59** — weak; usually cut.
- **<40** — reject.

---

## Keller's six brand-element criteria
Memorable · Meaningful · Likable · Transferable · Adaptable · Protectable.

## Overlays the human Decision Lead applies on top of the script
- **Two-axis discipline:** a name can't win on distinctiveness alone — it must ALSO be
  decodable on first hearing ("surprising, but surprisingly familiar"). Flag any
  candidate high on one axis and low on the other.
- **SMILE minimums:** drop or downgrade anything that scores 0 on Suggestive, Imagery,
  OR Emotional (the stickiness drivers).
- **Story / ask-a-question test:** every finalist must support a one-sentence "why this
  name" story, make a listener want to ask a follow-up, and extend into a brand world.
  A name with no narrative is dead on arrival, however clever the phonetics.
- **Polarization adjustment:** discomfort is NOT a deduction. Mark a strong-but-uneasy
  name "polarizing — energy present" and keep it. Only penalize discomfort that comes
  from confusion, a bad meaning, or unpronounceability — never from boldness.

---

## Running the scorer
```
python3 scripts/score.py --template                       # print input schema
python3 scripts/score.py --input candidates.json          # score a file
cat candidates.json | python3 scripts/score.py            # score from stdin
python3 scripts/score.py --input candidates.json --weights '{"sound_symbolism": 25}'
```
Output is a ranked JSON. For EACH candidate it emits `{name, score, risk_label,
killed_by_hard_gate, breakdown[]}` where `breakdown` lists every dimension's
`{weight, raw, applied, contribution, capped?, cap?, cap_reason?}` — so the total is
fully reconstructable and every cap is visible. It also emits `audit_flags` (capped
top-3 picks, near-ties).

**Output contract (enforced at Stage 7):**
1. The literal `score.py` invocation AND its raw stdout are pasted into the final output.
2. Every shortlisted name shows its full 8-dimension `breakdown`.
3. The narrated ranking MUST equal the `results` order (by total). If prose wants to
   override the math (e.g. "we'd still pick B over A"), it must say so explicitly and
   justify it — it may not silently reorder.
4. Any `audit_flags` are addressed in the writeup, not hidden.
