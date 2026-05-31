<div align="center">

# ✨ Nomira

### a whole brand-naming agency, stuffed into one Claude Code skill 🪄

You bring the half-baked idea. It brings the strategist, the word-nerd, and the trademark lawyer.

Tell it what you're building → it asks a couple of sharp questions → dreams up *hundreds* of names → argues with itself about which ones slap → screens them for trademark + language landmines → scores them cold → hands you a shortlist you'd actually be proud to ship. 🔥

**no blank-page panic. no "we'll fix the name later." just good names, with receipts.**

```
/nomira
```

`free` · `open source` · `MIT` · `runs in Claude Code`

</div>

---

You made something cool. Now it needs a name.

You *could* think hard for ten minutes and grab the first okay word that shows up. Most people do. That name usually ends up forgettable, already taken, or secretly cursed in another language. 💀

Big companies don't gamble like that. They hand the job to a naming studio and pay roughly *the price of a car* for it. Inside that studio: word people, sound people, and lawyers, all sweating over one name for weeks.

**Nomira is that studio, living on your laptop, working for free, and it literally never gets tired.**

You say *"coffee app for night-shift workers"* → it dreams up a big pile of names, yeets the duds, double-checks the survivors, and hands you the best few with a reason for each. that's the whole vibe. ☕

---

## 🧠 what actually went into this (the lore)

Nomira is not a word blender with a thesaurus taped to it. it's the distilled habits of an entire craft.

We basically went to school on naming. 🎓 We sat with the published playbooks of the world's most respected naming studios. (You know the ones. Their names live in your pocket and you say them every single day without ever wondering who cooked them up.) We read the founders getting interviewed, watched the talks, pulled the transcripts so nothing got lost in translation.

Then we went deeper than the studios usually let on, into the actual *science* of why some words just **feel** right:

- 🔊 **the psychology of sound.** why "kee-kee" feels sharp and "boo-bah" feels round to basically everyone on Earth, in study after study, across languages, even with toddlers who can't read yet. real peer-reviewed research, not vibes.
- 🧲 **how memory grabs a word.** why some names stick on the first listen and others slide right off your brain.
- ⚖️ **what the law will actually let you own.** straight from the official trademark offices, so the name you fall for isn't one you can never have.

Hundreds of sources. one method. boiled down so the skill runs it the same careful way *every single time.* the afternoon you'd waste guessing is the afternoon Nomira spends **working**, except it's doing the job of a dozen specialists at once and doesn't need snacks.

> 🥷 behind that cute little `/nomira` prompt is a small army of experts who all happen to live inside the same program.

---

## ⚙️ how it works

Real studio process, automated. You stop *once*, near the start, to answer a few Qs. After that it runs the whole show solo. 🎬

```
        🧑‍💻 you describe the thing
                │
                ▼
   1️⃣  INTAKE        →  asks a few sharp Qs, fills the rest with smart defaults
                │
   2️⃣  STRATEGY      →  locks the ONE idea the name has to carry
                │
   3️⃣  GENERATE      →  dreams up hundreds of names, judgment switched OFF
                │
   4️⃣  QUICK CUT     →  drops the unpronounceable, the copycats, the cringe
                │
   5️⃣  DEBATE        →  strategist 🆚 word-nerd 🆚 lawyer, fight!
                │
   6️⃣  SCREEN+SCORE  →  trademark + language checks, then cold honest numbers
                │
                ▼
   7️⃣  🏆 SHORTLIST  →  your best names, each with a reason + a risk flag
```

why it's more than a vibes-based word generator:

- 🎯 **meaning before words.** no name gets made until the strategy is locked. a messy brief makes messy names, so this step quietly does half the work.
- 🔊 **sound on purpose.** soft sounds feel calm, hard sounds feel fast. Nomira matches the *sound* to the *feeling* you want, and it learned that from research, not taste.
- 🥊 **it argues with itself.** different expert voices score every name and throw hands over the close calls. survivors come out stronger.
- 🧮 **the math can't lie.** scoring runs through an actual program, not a gut feeling. break a rule → the score drops on its own. the numbers never quietly disagree with the reasoning.
- 🚧 **honest about risk.** you get a pre-check, not legal cover. it flags trademark danger + language traps, and straight-up tells you when a name needs a real lawyer.

---

## 🚀 install

You'll need [Claude Code](https://docs.claude.com/en/docs/claude-code). Then:

```bash
git clone https://github.com/bazingga08/nomira.git
ln -s "$(pwd)/nomira/skill" ~/.claude/skills/nomira
```

That second line points Claude Code at the skill. Open Claude Code, type `/nomira`, describe what you're naming. that's it. ⚡

---

## 🎮 try it

```
/nomira

budgeting app for freelancers who hate spreadsheets.
calm + trustworthy, NOT a flashy finance-bro vibe.
```

a couple quick Qs later, you get back something like this 👇

```
🏆 TOP 3 PICKS

1. Tendio          84  🟢 Strong
   coined: "tend" (to look after) + soft -io ending
   sounds calm + careful, exactly the feeling you asked for
   trademark: clean in the finance-app space. grab the .com 👀

2. Ledgerly        79  🟢 Strong
   "ledger," but said like a human, not a spreadsheet
   clear about what it does, still has warmth
   trademark: a few neighbors, worth a proper search

3. Quill           71  🟡 Caution
   real word: the pen freelancers invoice with
   warm + simple, but heavily used → harder to own
   trademark: crowded. handle with care
```

you pick one. you ship. you go touch grass. 🌱

---

## 📦 what's in the box

```
nomira/
├── skill/            👈 the actual skill Claude runs
│   ├── SKILL.md          the main pipeline
│   ├── reference/        the deep method: sound rules, scoring, screening
│   └── scripts/          the scoring program
└── research/         🧠 the knowledge base behind it all, sources cited
```

it's all open. read it, fork it, tune the scoring weights to your own taste. the `research/` folder is the real treasure: the distilled craft, laid out so you can see *why* it makes the calls it makes.

---

## 🙅 what it won't do

Nomira is a glow-up for your process, not a replacement for your brain.

- ⚖️ trademark **pre-screen**, not a clearance. get a real search before you commit.
- 🔊 the sound→meaning effect is a strong *tendency*, not a law. matters more for everyday consumer stuff than slow, careful B2B buys.
- 🫵 the taste is still yours. it gets you to a strong shortlist *fast*, but the final call (and selling it to your team) stays human.

> 🤯 plot twist: **Nomira named itself.** we pointed the skill at its own brief and let it cook. round one flopped. it dusted itself off, ran again, and landed on *Nomira* (from Latin *nomen* = "name"). the tool passed its own exam. 🎓

---

<div align="center">

### built by an AI agency that's naming itself into existence, one skill at a time.

if Nomira names something you ship, tag it. we wanna see. 👀

**⭐ star it · 🍴 fork it · 🛠️ build on it**

`MIT`. use it, remix it, make something better.

</div>
