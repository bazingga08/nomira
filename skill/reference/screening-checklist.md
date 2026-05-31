# Screening Checklist — Stages 4 & 6

Two passes: a CHEAP hard-reject cull EARLY (Stage 4, before the expensive debate),
then the FULL gauntlet of hard gates + scoring LATE (Stage 6). Every hard gate is a
KILL-SWITCH — a name failing it is dropped regardless of score. Label everything
**"pre-screen only — requires professional trademark search before adoption."**

---

## Stage 4 — Cheap cull (before debate)

### Phonotactics
Transcribe each candidate to IPA. Reject onset/coda consonant clusters that are
illegal or hard in each TARGET-MARKET language. Phonotactics are language-specific —
re-check per market, not just English.

### SCRATCH auto-rejects (any one = drop)
- **S** — Spelling-challenged (people can't spell it after hearing it)
- **C** — Copycat (looks/sounds like competitors)
- **R** — Restrictive (boxes in future growth/categories)
- **A** — Annoying (forced, gimmicky, tries too hard)
- **T** — Tame / Tasteless (timid and forgettable, or off-putting)
- **C** — Curse-of-knowledge (only insiders decode it)
- **H** — Hard-to-pronounce

### `do_not_sound_like` HARD ELIMINATION (deterministic — runs here, not as a footnote)
The Stage-2 strategy object stores `do_not_sound_like[]` (banned competitor marks,
roots, and affixes — e.g. "Link-*", "Wayfair"). At THIS stage, mechanically KILL any
candidate that matches a pattern by **substring, shared distinctive root/affix, or
rhyme**. A killed name may NOT appear in any downstream stage. Log each kill in an
`eliminated_names[]` ledger with the exact pattern it tripped. (Validation defect this
closes: "Link-*" was listed as do_not_sound_like, yet Driftlink and Lumalink reached
the shortlist. A constraint that removes nothing is decoration.)

---

## Stage 6 — Full gauntlet (hard gates, EARLY-BUT-FINAL)

### (a) Abercrombie distinctiveness spectrum
Weakest → strongest legal protection:
**Generic (REJECT) → Descriptive (flag, weak) → Suggestive (good) → Arbitrary (strong)
→ Fanciful (strongest).** Bias toward fanciful / arbitrary / suggestive.

### (b) Trademark knockout (Nice-class-aware) — PRE-SCREEN ONLY
Knockout on **sight / sound / meaning**, including phonetic equivalents and FOREIGN
equivalents. Apply the **anti-dissection rule**: compare marks as WHOLES, not by
splitting into parts. Check against the relevant Nice class(es). This is a pre-screen
to cut attorney hours — NEVER a clearance opinion.
- Clearance is **per class** (45 Nice classes: 1–34 goods, 35–45 services). Screen the
  relevant + adjacent classes, not "the name" in the abstract.
- **Class 9 (software/electronics) is saturated** (2M+ marks vs ~500k dictionary words)
  — expect collisions there and lean harder on coined/arbitrary names.
- Rights are **territorial** — plan per region or via the Madrid System (one filing,
  up to ~131 countries; needs a home-base mark).
- USPTO search: https://www.uspto.gov/trademarks/search · WIPO Nice:
  https://www.wipo.int/classifications/nice/en/ · Madrid: https://www.wipo.int/madrid/en/

**MANDATORY finalist check (not optional).** For EVERY finalist (the 5–25 survivors),
run the free-tier checks inline: USPTO TESS + EUIPO eSearch + npm / GitHub-org + the
.com domain + the bare name with the category. This is a weight-15 axis — it may NOT
be evidence-free. Then bind the result to the score via the TM cap
(`reference/scoring-rubric.md`): Conflict-risk / named-big-mark proximity →
`caps.tm_domain_headroom = 2`; Caution → `= 5`; Clear → no cap.
**If web tools are unavailable**, cap `tm_domain_headroom` at 5 for every finalist and
label it "unverified — TM tools unavailable." Never assert a collision call from memory
as if it were searched; cite the source (which register, what was found) or mark it
unverified. (Validation defect this closes: finalists shipped adjacent to live marks —
Wayfin↔Wayfair, Veerly↔Verily — with no demotion and no evidence.)

### (c) Cross-language / cultural screen — in EVERY target market
Native-homophone + connotation + cultural-disaster check in every target language,
even non-operating ones ("your brand name is instantly global"). Real cautionary cases:
**Mitsubishi Pajero**, **Honda Fitta**, **Ford Pinto**. Do NOT repeat apocrypha — Chevy
Nova ("no va") and Coca-Cola ("wax tadpole") are partly myth; verify, don't assert.
FLAG UNCERTAINTY explicitly and require native-source verification of finalists. Never
assert "clean in language X" as certainty; never hallucinate it.

### (d) Domain / social check — heuristic, NOT a veto
Check .com + social handles and propose an acquisition strategy. Does NOT veto a
superior name (".com is an area code"). Lexicon research: only ~28% of consumers attend
to the URL and ~42% don't recall the extension. Workarounds: secure the name first,
then prefix/suffix (get-, try-, -app, -hq) or use an alt-TLD. Treat earlier signals as
heuristic and re-verify finalists live.

### Consumer validation (decision tool, not popularity)
Frame for message delivery & believability, NOT "do you like it." Use the COMPETITOR
TEST: *"Our competitor just launched with this name — what's your reaction?"* The name
that would worry you most about a rival is usually the winner. A winning name "does not
need to be comfortable or popular." Add the say-it-out-loud / phone test: if it can't be
spelled after one hearing or pronounced after one reading, downgrade it.

---

## SMILE — positive signals (reward)
- **S** — Suggestive (hints at the benefit/positioning)
- **M** — Memorable (sticky, easy recall)
- **I** — Imagery (evokes a concrete picture)
- **L** — Legs (room to extend into a brand/line)
- **E** — Emotional (creates a feeling)

---

## Output per candidate
A risk label: **Strong / Caution-tm / Caution-descriptive / Reject-generic /
Conflict-risk**, plus the Nice class checked, the TM cap applied (if any) with the
colliding mark named, and any cross-language/domain flags. Names failing a hard gate
are dropped, not deducted; names with a flagged collision are CAPPED (not just
footnoted) so the demotion shows up in the total.

---

## Case studies (illustrative, not proof of universal optimality)
- **BlackBerry** — name a wireless email device; problem = email anxiety. Hero:
  calming/approachable (Sincerity). Team C (nature) harvested fruit names; keys looked
  like drupelets. /b/ + liquids = calming; vivid imagery; counter-positions anxiety.
  Initially resisted internally — polarization-as-energy.
- **Pentium** — name Intel's 586 (numbers aren't trademarkable). Hero:
  powerful/fundamental (Competence). Neoclassical: pent- + -ium → "fundamental element
  of computing"; /p t/ = fast/sharp; scientific-premium.
- **Swiffer** — quick floor-cleaning tool. Hero: quick/effortless (Excitement). Mine
  the verb swipe/sweep/swift + -er; /sw/ = sweeping motion.
- **Febreze** — fabric odor eliminator. Hero: fresh/clean (Sincerity). Blend
  fabric+breeze, respelled; /f z/ = airy.
- **Dasani** — Coca-Cola bottled water. Hero: pure/refreshing (Sincerity). Pure
  neologism; /s n/ + /ɑ/ = smooth/fresh; broke water place-name convention; ownable.
- **Azure** — Microsoft cloud. Hero: limitless/sky (Competence). Arbitrary real-word
  (sky blue); broke "cloud X" convention; initially polarizing.
- **Windsurf** — AI coding IDE (Codeium). Hero: flow/effortless momentum (Excitement).
  Metaphor — riding the wind; concrete, energetic, distinctive in dev-tools.
