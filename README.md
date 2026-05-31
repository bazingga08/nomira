<div align="center">

# Nomira

### A whole brand-naming agency, packed into one Claude Code skill.

Tell it what you're building. It asks a few sharp questions, invents hundreds of names, argues with itself about which ones are any good, checks them for trademark and language problems, scores them, and hands you a short list you can actually use.

`/nomira` · free · open source

</div>

---

## Explain it like I'm five

You made something cool and now it needs a name.

You could think hard and pick the first okay word that comes to mind. Most people do. The name usually ends up boring, or already taken, or it means something rude in another language.

Big companies skip all that. They pay a naming firm a lot of money (about the price of a car) to do it properly, with word experts, sound experts, and lawyers all working together.

**Nomira is that firm, on your computer, for free.**

Say *"I'm making a coffee app for night-shift workers."* Nomira thinks up a big pile of names, drops the bad ones, checks the good ones, and hands you the best few with a reason for each. That's it.

---

## Why this exists

A name is the one branding decision you can't easily take back, and it's the one most people rush.

The firms that named Pentium, BlackBerry, Swiffer, and Dasani don't rush it. They follow a careful process grounded in research on how sounds carry meaning, how memory works, and what trademark law actually lets you own.

Nomira learned that process. We built it by reading 373 sources: the naming firms' own playbooks, founder interviews and talks, research papers on the psychology of word sounds, and the official trademark guides from the US and world patent offices. We boiled all of it down into steps the skill runs every time.

---

## How it works

Nomira runs the same stages a real agency does. You stop once, near the start, to answer a few questions. After that it runs on its own.

```
   YOU describe the thing
          │
          ▼
   1. INTAKE        →  asks you a few sharp questions, fills the rest with smart defaults
          │
   2. STRATEGY      →  locks in the ONE idea the name must carry
          │
   3. GENERATE      →  invents hundreds of candidates, judgment switched off
          │
   4. QUICK CUT     →  drops the unpronounceable, the copycats, the duds
          │
   5. DEBATE        →  a strategist, a linguist, and a lawyer argue it out
          │
   6. SCREEN+SCORE  →  trademark + language checks, then honest numbers
          │
          ▼
   7. SHORTLIST     →  your best names, each with a real reason and a risk flag
```

What makes it more than a random word generator:

- **Meaning comes before words.** No name gets made until the strategy is set. The brief is half the job.
- **It uses sound on purpose.** Soft sounds feel calm, hard sounds feel fast. Nomira matches the sound to the feeling you're after, and it gets this from research rather than taste.
- **It argues with itself.** Different expert voices score every name and fight over the close calls. The survivors come out stronger.
- **The math can't lie.** Scoring runs through a small program, not a gut feeling. Break a rule and the score drops on its own, so the numbers always match the reasoning.
- **It's honest about risk.** You get a pre-check, not legal advice. Nomira flags trademark danger and language problems, and it says plainly when a name needs a real lawyer.

---

## Install

You'll need [Claude Code](https://docs.claude.com/en/docs/claude-code).

```bash
git clone https://github.com/bazingga08/nomira.git
ln -s "$(pwd)/nomira/skill" ~/.claude/skills/nomira
```

The second line points Claude Code at the skill. Open Claude Code, type `/nomira`, and describe what you're naming.

---

## Try it

```
/nomira

I'm building a budgeting app for freelancers who hate spreadsheets.
Calm and trustworthy, not a flashy finance-bro vibe.
```

Nomira asks two or three questions, then comes back with a ranked short list. Every name carries its reasoning, its sound notes, and a trademark risk flag. You pick one and ship.

Here's the shape of what comes back:

```
TOP 3 PICKS

1. Tendio          84  [Strong]
   Coined from "tend" (to look after) + a soft -io ending.
   Sounds calm and careful, which is the feeling you asked for.
   Trademark: clean in the finance-app space. Grab the .com.

2. Ledgerly        79  [Strong]
   "Ledger" said in a friendly, human way.
   Clear about what it does without sounding like a spreadsheet.
   Trademark: some nearby names, worth a proper search.

3. Quill           71  [Caution]
   A real word: the pen freelancers invoice with.
   Warm and simple, but heavily used, so harder to own.
   Trademark: crowded. Treat with care.
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

Everything is open. Read it, fork it, tune the scoring weights for your own taste.

---

## What it won't do

Nomira speeds you up. It doesn't replace your judgment.

- It gives a trademark **pre-screen**, not a clearance. Get a real trademark search before you commit a name.
- The sound-meaning effect is a strong tendency, not a law. It counts for more in everyday consumer products than in slow, careful B2B buying.
- The taste is still yours. Nomira gets you to a strong short list fast, but the final call, and selling the name to your team, stays with you.

> One more thing: Nomira named itself. We ran the skill on its own brief, and "Nomira" (from the Latin *nomen*, meaning *name*) came out on top.

---

## License

MIT. Use it, change it, build on it.
