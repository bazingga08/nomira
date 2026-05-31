# Sound Symbolism — Phoneme-Feel Table

Used as BOTH a generation driver (Stage 3) and a scoring dimension (Stage 6). This is
a WEIGHTED HEURISTIC (~60–75% cross-cultural tendency), NOT a law. Bouba/kiki
replicates at ~70%, not 95%. Weight it LOWER for high-deliberation B2B buyers and
HIGHER for impulse/low-consideration consumers (Yorkston-Menon; Alter-Oppenheimer).

---

## Plosives / stops
- **Voiceless stops /p/ /t/ /k/** — fast, sharp, precise, light, tech, energetic.
  Front-of-mouth release = quick, snappy.
- **Voiced stops /b/ /d/ /g/** — solid, heavy, reliable, grounded, substantial.

## Fricatives
- **Voiceless fricatives /f/ /s/ /θ/** — smooth, airy, fast, flowing, soft.
- **Voiced fricatives /v/ /z/ /ʒ/** — buzzy, energetic, modern, premium.

## Sibilants
- **/s/** — speed, smoothness, sleekness; can also read as small / light.
- **/ʃ/ (sh)** — quiet, soft, hushed, calming.

## Liquids / sonorants
- **/l/ /m/ /n/ /r/** — smooth, flowing, calming, soft, human, warm.

## Affricates
- **/tʃ/ (ch) /dʒ/ (j)** — rich, premium, textured; late-acquired in childhood →
  reads as sophisticated.

## Vowels
- **Front / high vowels /i/ /ɪ/ (ee, i)** — small, fast, light, bright, sharp, precise.
- **Back / low vowels /ɑ/ /o/ /u/ (ah, oh, oo)** — large, slow, heavy, solid,
  powerful, round.
- **Long vowels** — slower, grander, more premium.
- **Short vowels** — quick, snappy, casual.

## Bouba / kiki
Round shapes → round sounds (bouba: /b/, /o/, /m/). Sharp shapes → sharp sounds
(kiki: /k/, /i/, /t/). ~70% cross-cultural replication — strong tendency, not certainty.
A few languages (Romanian, Mandarin, Turkish) fell at/below chance — the local lexicon
can override the mapping, so always screen against the target market.

## Weighting within a name (where the cues live)
- The **stressed-syllable vowel** carries the most size/weight signal — fix it first.
  (Vowels ~81% size accuracy vs consonants ~55–76%.)
- The **initial onset consonant** carries the most symbolic primacy — weight it next.
- Frish/Frosh proof: identical ice cream named "Frish" (/i/) vs "Frosh" (/ɑ/) → "Frosh"
  rated smoother/creamier/richer. The effect is automatic and STRONGER under cognitive
  load — people can't discount it, which is exactly why it matters for impulse buyers.

## Signature single-letter cues (Placek / Lexicon)
| Letter | Connotation | Example |
|---|---|---|
| V | most "alive and vibrant"; more V's = more energy | Vercel, Corvette |
| B | one of the most reliable sounds | BlackBerry |
| Z | noisy / energetic / attention-drawing | Azure |
| X | fast, crisp, innovative | (innovation cue) |

## Phonesthemes (sub-morphemic clusters; seed the good, screen out the bad)
| Cluster | Meaning | Examples |
|---|---|---|
| gl- | light / vision / shine | glow, glitter, gleam, glint |
| fl- | quick / light movement | fly, flutter, flicker, flash, flow |
| str- | lines / tension / strength | string, streak, stripe, stretch, stream |
| sn- | nose / mouth | sniff, snore, snout, snack |
| sl- | slippery — **PEJORATIVE, avoid** | slime, slip, sludge, sleazy |
| -ash | forceful sudden impact | crash, smash, dash, splash |
| -ump | roundness / heaviness | lump, bump, plump, clump |
| wr- | twisting / distortion | wring, wrap, wrench, wrinkle |

---

## Attribute → phoneme quick map

| Hero attribute | Favor | Avoid |
|---|---|---|
| Fast / sharp / tech | /p t k/, /i ɪ/, short vowels | heavy voiced stops, long back vowels |
| Reliable / solid | /b d g/, /ɑ o u/ back vowels | thin /i/, hissy /s/-heavy clusters |
| Luxury / premium | /tʃ dʒ ʒ/, long vowels | clipped voiceless-stop staccato |
| Calming / soft | /l m n r/, /ʃ/, rounded vowels | hard /k t/ onsets, sharp /i/ |
| Energetic / exciting | voiceless stops + /z v/, bright /i/ | sleepy sonorant-only strings |

---

## Application rules (don't break these)
- **Congruence over intensity.** Reinforce ONE attribute; don't mix contradictory cues
  (front-vowel "small" + voiced-stop "heavy" cancel out).
- **Fit-to-category (Lowrey-Shrum).** Match the connoted attribute to what's DESIRABLE
  for the product; an incongruent name is worse than a neutral one.
- **Validate, don't intuit.** Frish/Frosh proves you can't feel these from the inside.

## Application in the pipeline
1. **Generation (Stage 3):** derive the target phonetic profile from the hero
   attribute + Aaker personality, then generate names that HIT it.
2. **Scoring (Stage 6):** score each candidate's sound-symbolism MATCH to the hero
   attribute, AND attach a mechanical cap so the penalty BINDS the number:
   - IPA-transcribe the name. Read off its onset consonant and stressed-syllable vowel.
   - Look up the hero attribute's FAVOR / AVOID lists in the "Attribute → phoneme quick
     map" above.
   - **If the name contains ANY AVOID-list phoneme → set `caps.sound_symbolism = 4`.**
   - **Else if the onset is not in the FAVOR class → set `caps.sound_symbolism = 6`.**
   - Else no cap (clean MATCH may score 8–10).
   - Put the offending phoneme + hero attribute in `cap_reasons.sound_symbolism`, and
     record the MATCH verdict in the Linguist note. Per Lowrey-Shrum a MISMATCH is a
     PENALTY, never neutral — and the cap is what makes that true in the math, so a
     name can NEVER rank #1 while admitting a phonetic mismatch (the validation defect
     this closes).
