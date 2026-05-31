# Nomira — Naming Skill Project

Everything for **Nomira**, the brand/product/company naming skill, lives in this folder, self-contained so the Desktop stays clean.

> **Name origin:** *Nomira* — from Latin *nomen* ("name") + a flowing *-ira* ending. Chosen by running the skill on itself (4 rounds, deterministic scoring): 83.5 [Strong], clean trademark headroom, coined-but-complete. Invoked as `/nomira`.

## Structure
```
work/skills/naming/
├── skill/                         ← THE MASTER SKILL (source of truth)
│   ├── SKILL.md                   ← the self-driving 8-stage pipeline
│   ├── reference/                 ← methodology, sound-symbolism, scoring-rubric,
│   │                                screening-checklist, generation-playbook, pipeline,
│   │                                intake-questions
│   └── scripts/score.py           ← deterministic scoring engine
└── research/
    ├── knowledge-base/            ← synthesized, cited research
    │   ├── lexicon-naming-knowledge-base.md      (v1 survey)
    │   ├── lexicon-naming-knowledge-base-v2.md   (hardened, 50KB, primary)
    │   ├── naming-deep-insights.md               (firm org chart + curriculum + rival firms)
    │   └── naming-skill-architecture.md          (the company-replacement spec)
    ├── sources/                   ← primary source material (Yorkston & Menon paper + extracts)
    └── raw-web-dumps/             ← raw web-fetch captures (hits, snips)
```

## How the live skill connects
Claude Code only loads skills from `.claude/skills/`. So the master lives **here**
(`skill/`) and is **symlinked** in (matching how every other skill on this machine is set up):

```
~/Desktop/.claude/skills/nomira  ->  ../../work/skills/naming/skill
```

Edit the files in `skill/` — changes take effect immediately through the link.
Invoke with `/nomira` (triggers: name a company / product / project / brand / feature / startup).

## Status
Built, validated by adversarial judges, and hardened: scores now mechanically OBEY the
rules (see `skill/reference/scoring-rubric.md` caps + the Stage-7 self-audit gate in
`skill/SKILL.md`). Verified on the exact case it previously failed.

Built from **373 web pages read** (597 fetches, 400 searches) across the naming firms,
the founders' talks/podcasts, peer-reviewed sound-symbolism papers, and USPTO/WIPO.
