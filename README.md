<div align="center">

# Nomira

### A whole brand-naming agency, packed into one Claude Code skill.

Tell it what you're building. It asks a few sharp questions, dreams up hundreds of names, argues with itself about which ones are any good, checks them for trademark and language landmines, scores them, and hands you a short list you'd actually be proud to use.

No blank-page panic. No "we'll fix the name later." Just good names, with reasons.

`/nomira` · free · open source

</div>

---

## Explain it like I'm five

You made something cool. Now it needs a name.

You could think hard for ten minutes and pick the first okay word that pops up. Most people do. The name usually ends up forgettable, or already taken, or it means something embarrassing in another language.

The big companies don't gamble like that. They hand the job to a naming studio and pay about the price of a car for it. Inside that studio sit word people, sound people, and lawyers, all fussing over a single name for weeks.

**Nomira is that studio, living on your laptop, working for free, and it never gets tired.**

Say *"I'm making a coffee app for night-shift workers."* Nomira dreams up a big pile of names, throws out the duds, double-checks the survivors, and hands you the best few with a reason for each. Done.

---

## What went into this (the fun part)

Nomira isn't a word blender with a thesaurus taped to it. It's the distilled habits of an entire craft.

To build it, we went to school on naming. We sat with the published playbooks of the world's most respected naming studios, the ones whose names you say every single day without ever wondering who dreamed them up. We read the founders being interviewed, watched the talks, and pulled the transcripts so nothing got lost in a summary.

Then we went deeper than the studios usually let on. We dug into the actual science of why some words *feel* right:

- **The psychology of sound.** Why "Kee-koo" feels sharp and "Boo-bah" feels round to almost everyone on Earth, in study after study, across languages and even with little kids who can't read yet. Real peer-reviewed research, not vibes.
- **How memory actually grabs a word.** Why some names stick on the first hearing and others slide right off.
- **What the law will actually let you own.** Straight from the official trademark offices, so the names you fall in love with aren't ones you can never have.

All of it, hundreds of sources, got boiled down into a method the skill runs the same careful way every time. The afternoon you'd spend guessing is the afternoon Nomira spends *working*, except it does the work of a dozen specialists at once and doesn't need coffee.

> Behind that friendly `/nomira` prompt is a small army of experts who all happen to live in the same program.

---

## How it works

Nomira runs the same stages a real studio does. You stop once, near the start, to answer a few questions. After that, it runs the whole show itself.

```
   YOU describe the thing
          │
          ▼
   1. INTAKE        →  asks you a few sharp questions, fills the rest with smart defaults
          │
   2. STRATEGY      →  locks in the ONE idea the name has to carry
          │
   3. GENERATE      →  dreams up hundreds of candidates, judgment switched off
          │
   4. QUICK CUT     →  drops the unpronounceable, the copycats, the duds
          │
   5. DEBATE        →  a strategist, a word-nerd, and a lawyer fight it out
          │
   6. SCREEN+SCORE  →  trademark + language checks, then cold, honest numbers
          │
          ▼
   7. SHORTLIST     →  your best names, each with a real reason and a risk flag
```

What makes it more than a random word generator:

- **Meaning comes before words.** No name gets made until the strategy is nailed down. A muddled brief makes muddled names, so this step quietly does half the work.
- **It uses sound on purpose.** Soft sounds feel calm, hard sounds feel fast. Nomira matches the sound to the feeling you're after, and it learned that from research, not taste.
- **It argues with itself.** Different expert voices score every name and brawl over the close calls. The survivors come out stronger for it.
- **The math can't lie.** Scoring runs through a small program, not a gut feeling. Break a rule and the score drops on its own, so the numbers never quietly disagree with the reasoning.
- **It's honest about risk.** You get a pre-check, not legal cover. Nomira flags trademark danger and language traps, and it tells you plainly when a name needs a real lawyer.

---

## Install

You'll need [Claude Code](https://docs.claude.com/en/docs/claude-code).

```bash
git clone https://github.com/bazingga08/nomira.git
ln -s "$(pwd)/nomira/skill" ~/.claude/skills/nomira
```

The second line points Claude Code at the skill. Open Claude Code, type `/nomira`, and tell it what you're naming.

---

## Try it

```
/nomira

I'm building a budgeting app for freelancers who hate spreadsheets.
Calm and trustworthy, not a flashy finance-bro vibe.
```

Nomira asks two or three quick questions, then comes back with a ranked short list. Here's the shape of what lands:

```
TOP 3 PICKS

1. Tendio          84  [Strong]
   Coined from "tend" (to look after) + a soft -io ending.
   Sounds calm and careful, which is the feeling you asked for.
   Trademark: clean in the finance-app space. Grab the .com.

2. Ledgerly        79  [Strong]
   "Ledger" said in a friendly, human way.
   Clear about what it does without sounding like a spreadsheet.
   Trademark: a few neighbors, worth a proper search.

3. Quill           71  [Caution]
   A real word: the pen freelancers invoice with.
   Warm and simple, but heavily used, so harder to own.
   Trademark: crowded. Handle with care.
```

You pick one and ship.

---

## What's in this repo

```
nomira/
├── skill/            the actual skill Claude runs
│   ├── SKILL.md          the main pipeline
│   ├── reference/        the deep method: sound rules, scoring, screening
│   └── scripts/          the scoring program
└── research/         the knowledge base behind it all, with sources cited
```

Everything is open. Read it, fork it, tune the scoring weights to your own taste. The research folder is the good stuff: the distilled craft, laid out so you can see *why* it makes the calls it makes.

---

## What it won't do

Nomira speeds you up. It doesn't replace your judgment.

- It gives a trademark **pre-screen**, not a clearance. Get a real trademark search before you commit a name.
- The sound-meaning effect is a strong tendency, not a law. It counts for more in everyday consumer products than in slow, careful B2B buying.
- The taste is still yours. Nomira gets you to a strong short list fast, but the final call, and selling the name to your team, stays with you.

> One more thing: Nomira named itself. We pointed the skill at its own brief and let it run. The first round flopped. It dusted itself off, went again, and landed on "Nomira" (from the Latin *nomen*, meaning *name*). The tool passed its own exam.

---

## License

MIT. Use it, change it, build something better on top of it.
