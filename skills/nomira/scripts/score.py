#!/usr/bin/env python3
"""Deterministic, editable-weight scoring engine for the `name` skill (Stage 6).

Replaces senior-people's-heads judgment with a transparent, tunable, reproducible
rubric. Each candidate is sub-scored 0-10 on each dimension; the engine computes a
weighted total (0-100) and a risk label.

Two enforcement mechanisms make the numbers OBEY the rules instead of merely
narrating them (this closes the validation gap where a name ranked #1 while the
prose admitted it failed the skill's own phonetic profile):

1. HARD GATES are KILL-SWITCHES: any false hard gate zeroes the score and forces the
   corresponding risk label.
2. CAPS are mechanical ceilings the upstream personas attach to a candidate when a
   deterministic rule fires (e.g. a phoneme on the Stage-2 AVOID list, or a flagged
   trademark collision). A capped sub-score CANNOT exceed its ceiling no matter what
   the LLM guessed — so a stated penalty actually drags the weighted total.

The engine ALWAYS emits the full per-dimension breakdown (sub-score, weight, capped
value, weighted contribution) so "deterministic via score.py" is verifiable and the
narrated ranking can be audited against the math.

Usage:
    python3 score.py --template                 # print the input JSON schema
    python3 score.py --input candidates.json    # score a file
    cat candidates.json | python3 score.py      # score from stdin
    python3 score.py --input c.json --weights '{"sound_symbolism": 25}'

Input JSON: {"weights": {..optional..}, "candidates": [ {candidate}, ... ]}
A candidate:
{
  "name": "Pentium",
  "scores": {                       # each 0-10
    "strategic_fit": 9, "sound_symbolism": 8, "distinctiveness": 9,
    "pronounceability": 8, "memorability": 8, "tm_domain_headroom": 7,
    "smile": 7, "keller": 8
  },
  "caps": {                         # optional; mechanical ceilings per dimension
    "sound_symbolism": 4,           # e.g. name contains a phoneme on the AVOID list
    "tm_domain_headroom": 2         # e.g. named big-mark proximity flagged
  },
  "cap_reasons": {                  # optional; why each cap fired (printed in output)
    "sound_symbolism": "onset /p/ on AVOID list for hero=reliable",
    "tm_domain_headroom": "Wayfin<->Wayfair sight/sound proximity"
  },
  "hard_gates": {                   # booleans; any false = kill-switch
    "abercrombie_not_generic": true, "tm_clear_prescreen": true,
    "cross_language_clean": true
  }
}
"""

import argparse
import json
import sys

# Default rubric weights (must sum to 100). Editable per brief via --weights or the
# "weights" key in the input file (matches strategy_object.scoring_rubric_weights).
DEFAULT_WEIGHTS = {
    "strategic_fit": 25,       # fit to the ONE hero attribute + Diamond
    "sound_symbolism": 15,     # Lowrey-Shrum MATCH (mismatch should be scored low)
    "distinctiveness": 15,     # Abercrombie strength + white space
    "pronounceability": 10,    # say-it / spell-it stability
    "memorability": 10,        # sticky, low-confusability
    "tm_domain_headroom": 15,  # pre-screen clearance likelihood + findability
    "smile": 5,                # SMILE positives
    "keller": 5,               # Keller's six brand-element criteria
}

HARD_GATES = ("abercrombie_not_generic", "tm_clear_prescreen", "cross_language_clean")


def effective_weights(overrides):
    w = dict(DEFAULT_WEIGHTS)
    if overrides:
        for k, v in overrides.items():
            if k not in w:
                raise ValueError("Unknown weight key: %s" % k)
            w[k] = float(v)
    return w


def score_candidate(cand, weights):
    scores = cand.get("scores", {})
    caps = cand.get("caps", {})
    cap_reasons = cand.get("cap_reasons", {})
    gates = cand.get("hard_gates", {})

    # Kill-switches first: a name can die on any hard gate.
    killed = None
    if gates.get("abercrombie_not_generic") is False:
        killed = "Reject-generic"
    elif gates.get("tm_clear_prescreen") is False:
        killed = "Conflict-risk"
    elif gates.get("cross_language_clean") is False:
        killed = "Conflict-risk"

    total_w = sum(weights.values()) or 1.0
    breakdown = []
    weighted = 0.0
    for dim, w in weights.items():
        raw = max(0.0, min(10.0, float(scores.get(dim, 0))))   # clamp 0-10
        cap = caps.get(dim, None)
        applied = raw
        if cap is not None:
            applied = min(raw, max(0.0, min(10.0, float(cap))))
        contribution = applied * w / total_w * 10.0            # this dim's share of 100
        weighted += applied * w
        entry = {"dimension": dim, "weight": w, "raw": round(raw, 1),
                 "applied": round(applied, 1),
                 "contribution": round(contribution, 1)}
        if cap is not None and cap < raw:
            entry["capped"] = True
            entry["cap"] = float(cap)
            entry["cap_reason"] = cap_reasons.get(dim, "(reason not supplied)")
        breakdown.append(entry)

    final = round(weighted / total_w * 10.0, 1) if killed is None else 0.0
    label = killed if killed else risk_label(final, scores, caps)
    return {"name": cand.get("name", "?"), "score": final, "risk_label": label,
            "killed_by_hard_gate": killed, "breakdown": breakdown}


def risk_label(final, scores, caps):
    # Descriptive-but-legal names get flagged even with a decent score.
    if float(scores.get("distinctiveness", 10)) <= 3:
        return "Caution-descriptive"
    # A fired TM cap means a flagged collision: never label "Strong".
    tm_capped = caps.get("tm_domain_headroom") is not None and \
        float(caps.get("tm_domain_headroom")) <= 5
    if final >= 75 and not tm_capped:
        return "Strong"
    if final >= 75 and tm_capped:
        return "Caution-tm"
    if final >= 55:
        return "Caution-descriptive"
    return "Reject-generic"


def audit(results):
    """Self-audit: the emitted order must equal the order sorted by total. Always true
    by construction here, but we also surface any near-ties and any capped winners so
    the narrated ranking can't silently disagree with the math."""
    flags = []
    for i, r in enumerate(results):
        capped = [b["dimension"] for b in r["breakdown"] if b.get("capped")]
        if capped and i < 3:
            flags.append("Top-%d pick '%s' has CAPPED dimensions %s — verify it still "
                         "deserves the rank." % (i + 1, r["name"], capped))
    for i in range(len(results) - 1):
        if 0 < results[i]["score"] - results[i + 1]["score"] <= 1.5:
            flags.append("Near-tie: '%s' (%.1f) vs '%s' (%.1f) — within 1.5; break it "
                         "on a stated tiebreaker, not vibes."
                         % (results[i]["name"], results[i]["score"],
                            results[i + 1]["name"], results[i + 1]["score"]))
    return flags


def run(payload, cli_weights):
    overrides = dict(payload.get("weights", {}))
    if cli_weights:
        overrides.update(cli_weights)
    weights = effective_weights(overrides)

    results = [score_candidate(c, weights) for c in payload.get("candidates", [])]
    results.sort(key=lambda r: r["score"], reverse=True)
    return {"weights": weights,
            "note": "pre-screen only - requires professional trademark search before adoption",
            "ranking_rule": "sorted by weighted total DESC; prose ranking MUST match this order",
            "audit_flags": audit(results),
            "results": results}


TEMPLATE = {
    "weights": DEFAULT_WEIGHTS,
    "candidates": [
        {
            "name": "Pentium",
            "scores": {
                "strategic_fit": 9, "sound_symbolism": 8, "distinctiveness": 9,
                "pronounceability": 8, "memorability": 8, "tm_domain_headroom": 7,
                "smile": 7, "keller": 8,
            },
            "caps": {},
            "cap_reasons": {},
            "hard_gates": {
                "abercrombie_not_generic": True, "tm_clear_prescreen": True,
                "cross_language_clean": True,
            },
        }
    ],
}


def main():
    ap = argparse.ArgumentParser(description="Deterministic name-scoring engine.")
    ap.add_argument("--input", help="path to candidates JSON (else stdin)")
    ap.add_argument("--weights", help="JSON object of weight overrides")
    ap.add_argument("--template", action="store_true",
                    help="print the input JSON schema and exit")
    args = ap.parse_args()

    if args.template:
        print(json.dumps(TEMPLATE, indent=2))
        return

    raw = open(args.input).read() if args.input else sys.stdin.read()
    payload = json.loads(raw)
    cli_weights = json.loads(args.weights) if args.weights else None
    print(json.dumps(run(payload, cli_weights), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
