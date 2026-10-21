import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
tables = __import__("conditioning_v2.tables", fromlist=["table"])
measures = tables.measures
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def _both(h):
    return h["observation"], h.get("narrow") or measures.history(h["transactions"], h["events"], "narrow")


def _actor_rows(h, prefix=()):
    wide, narrow = _both(h)
    return [(*prefix, measures.actor_name(a), r["tim"], "active" if r["active"] else "inactive",
             tables.ratio(r["conditioning"]), tables.ratio(narrow["actors"][a]["conditioning"]),
             tables.ratio(r["hold"]), tables.ratio(narrow["actors"][a]["hold"]))
            for a, r in wide["actors"].items()]


def _dcnh_rows(h, prefix=()):
    wide, narrow = _both(h)
    rows = []
    for a, r in wide["actors"].items():
        n = narrow["actors"][a]
        rows.append((*prefix, measures.actor_name(a), r["tim"], len(r["all_ids"]),
                     len(r["held"]), len(n["held"]),
                     ",".join(r["all_dcnh"]["cells_with_greatest_load"]),
                     ",".join(r["received_kept_dcnh"]["cells_with_greatest_load"]),
                     ",".join(n["received_kept_dcnh"]["cells_with_greatest_load"]),
                     "agree" if r["all_dcnh"] == r["received_kept_dcnh"] else "diverge",
                     "agree" if n["all_dcnh"] == n["received_kept_dcnh"] else "diverge"))
    return rows


ACTOR_HEADER = ("Actor", "TIM", "Status", "Conditioning wide", "Conditioning narrow", "Hold wide", "Hold narrow")
DCNH_HEADER = ("Actor", "TIM", "All uses (both)", "Received kept wide", "Received kept narrow",
               "Greatest all (both)", "Greatest received kept wide", "Greatest received kept narrow",
               "Comparison wide", "Comparison narrow")


def population(histories):
    """Return REPORT.md from restored population histories, under both readings.

    Preserve I1-I5 via measured inputs; assert repeated numeric claims before
    collapsing seeds. Batch 5, Batch 7 A1/A2 and A5 define the reporting scope.
    """
    first = histories[0]
    for h in histories:
        if _actor_rows(h) != _actor_rows(first) or _dcnh_rows(h) != _dcnh_rows(first):
            raise ValueError("population report needs per-history actor rows")
        for data in _both(h):
            if data["received"] or any(r["source"] != "world" for r in data["records"]):
                raise ValueError("population zero-delivery statement no longer holds")
    inputs = []
    for model in dict.fromkeys(h["manifest"]["model"] for h in histories):
        subset = [h for h in histories if h["manifest"]["model"] == model]
        facts = {(len(h["observation"]["profiles"]), h["manifest"]["transactions"]) for h in subset}
        if len(facts) != 1:
            raise ValueError("population inputs need per-history rows")
        inputs.append((model, ", ".join(str(h["manifest"]["seeds"]["fixture"]) for h in subset), *facts.pop()))
    text = """# Function Conditioning Ledger — population report

## 1. What was generated

Generated population histories contain Alice=IEE, Bob=SLI, and Eve=LIE. The
accepted manifests and original paid-use counts are unchanged under A5.

""" + tables.table(("Model", "Fixture seeds", "Actors", "Transactions"), inputs)
    text += "\nSource: [accepted inputs](TABLES/per_population.md#accepted-inputs).\n\n"
    text += """## 2. Cross-actor delivery and corrected conditioning

**No cross-actor delivery observed in generated histories under either reading.**
Wide uses every exact operation input; narrow uses only source.N/source_input.
Every source here is world. Both readings have zero received uses. The corrected
conditioning index is received weak uses / ALL weak uses; hold is kept received
/ received. A zero denominator is N/A. These rows hold in every listed history.
Bob's 0/9 means nine weak-seat uses and none received: a defined zero, not N/A.

""" + tables.table(ACTOR_HEADER, _actor_rows(first))
    text += "\nSources: [actor indices](TABLES/per_actor.md#actor-indices), [use trace](TABLES/per_actor.md#use-trace), [population summary](TABLES/per_population.md#population-summary).\n\n"
    text += "## 3. DCNH all-use versus received-and-kept\n\nEvery row holds at every seed and model. Comparisons use complete observations; greatest-load cells retain all ties.\n\n"
    text += tables.table(DCNH_HEADER, _dcnh_rows(first))
    text += "\nSource: [DCNH rows](TABLES/dcnh_two_ways.md). Empty received-and-kept observations do not assign a subtype.\n\n"
    text += "## 4. Coverage per population and episode\n\n"
    rows = []
    for h in histories:
        w, n = _both(h)
        if tuple(w["episode_coverage"]) != (0, 1) or tuple(n["episode_coverage"]) != (0, 1):
            raise ValueError("population report needs explicit episode columns")
        rows.append((h["manifest"]["name"], tables.ratio(w["coverage"]["ratio"]),
                     tables.ratio(n["coverage"]["ratio"]),
                     *(str(d["episode_coverage"][ep]["ratio"][0]) + "/" + str(d["episode_coverage"][ep]["ratio"][1])
                       for ep in (0, 1) for d in (w, n))))
    text += tables.table(("History", "Final wide", "Final narrow", "Episode 0 wide", "Episode 0 narrow", "Episode 1 wide", "Episode 1 narrow"), rows)
    text += "\nSources: [population summary](TABLES/per_population.md#population-summary) and [episode coverage](TABLES/per_population.md#coverage-by-episode-index). All committed actors' weak seats remain in the denominator. Episode indices pool actor-local episodes, not clock time.\n\n"
    text += "## 5. Sterile ordered pairs\n\nThese rows hold in every history. Sterile requires zero received uses in both directions.\n\n"
    w, n = _both(first)
    rows = [(measures.actor_name(p["sender"]), measures.actor_name(p["receiver"]), p["relation"],
             len(p["forward"]), len(q["forward"]), len(p["reverse"]), len(q["reverse"]), p["sterile"], q["sterile"])
            for p, q in zip(w["pairs"], n["pairs"])]
    text += tables.table(("Source", "Receiver", "Relation", "Forward wide", "Forward narrow", "Reverse wide", "Reverse narrow", "Sterile wide", "Sterile narrow"), rows)
    text += "\nSource: [ordered pairs](TABLES/per_population.md#ordered-pairs). Names annotate measured pairs.\n\n"
    text += "## 6. Benefit pair versus triad\n\n"
    rows = [(measures.actor_name(p["sender"]), measures.actor_name(p["receiver"]), p["relation"],
             len(p["forward"]), len(q["forward"]), len(w["benefit_ids"]), len(n["benefit_ids"]), "N/A: not generated")
            for p, q in zip(w["pairs"], n["pairs"]) if p["relation"] in measures.BENEFIT]
    text += tables.table(("Source", "Receiver", "Relation", "Pair wide", "Pair narrow", "Triad wide", "Triad narrow", "Standalone pair"), rows)
    text += "\nSource: [benefit rows](TABLES/per_population.md#benefit-pairs-within-the-triad-versus-triad-total). Pair subsets are within this triad; independent pair experiments were not generated.\n\n"
    text += """## 7. Limits

Generated workloads only; no historical archives, feedback, learning, subtype
assignment, or claims about people. Both readings preserve all-use counts and
DCNH. No actor-produced inputs were consumed in this fixture, so its zero
received counts do not test response to another actor's presence. Conditioning
is now defined when weak uses exist; hold and supplier concentration remain
N/A when no received uses exist. Wide is an operation-input upper bound on
semantic delivery. Narrow still assigns an operation's semantic-source tuple
to every paid block, not a verified lineage for each element. See [LIMITS.md](LIMITS.md).
"""
    return text


def delivery(histories):
    """Return REPORT_DELIVERY.md from circuit histories with wide/narrow views.

    Preserve I1-I5 and verify seed-collapsed measures; Batch 6, A3/A4,
    Batch 7 A1/A2 and A5. Provenance bounds are observations, not causation.
    """
    representatives = {}
    for h in histories:
        c = h["manifest"]["composition"]
        representatives.setdefault(c, h)
        other = representatives[c]
        if _actor_rows(h) != _actor_rows(other) or _dcnh_rows(h) != _dcnh_rows(other):
            raise ValueError("delivery report needs per-seed actor rows")
        for d, e in zip(_both(h), _both(other)):
            for key in ("coverage", "pairs", "concentration", "episode_coverage"):
                if d[key] != e[key]:
                    raise ValueError("delivery report needs per-seed population rows")
    generator = __import__("generate.histories_delivery", fromlist=["first_delivery"])
    first = representatives["pair"]
    text = """# Function Conditioning — delivery report

## 1. Fixture and first delivery

The accepted fixture is `tests_u11.fixtures.circuit11(flat=False)`; the original
Step 1 probe was not rerun. Existing parameterized setup/group/join calls
produce pair and pair-sterile compositions. All use legacy-r4, seeds 17, 29,
43, 61, and one harness episode including preparation. Seeds vary finite,
nonbinding budgets; they are not distinct stochastic workloads.

Wide includes source.N, source_input and input.N. Narrow excludes input.N.
The earliest observed deliveries in pair-seed-17 are:

"""
    rows = []
    for reading, obs in zip(("wide", "narrow"), _both(first)):
        witness = generator.first_delivery(first["transactions"], obs, reading)
        if witness:
            e = witness["exact_inputs"][0]
            rows.append((reading, "u" + str(witness["use"]), witness["transaction"], witness["operation"],
                         witness["actor"], witness["element"], witness["seat"], witness["dim"],
                         ",".join(witness["sources"]), e["transaction"], e["ref"]))
        else:
            rows.append((reading, *(["none"] * 10)))
    text += tables.table(("Reading", "Use", "Transaction", "Operation", "Receiver", "Element", "Seat", "Dim", "Sources", "Producer transaction", "Exact input"), rows)
    text += "\nSources: [manifest](HISTORIES_DELIVERY.json) for calls and wide witness; [pair trace](TABLES/pair_per_actor_delivery.md#use-trace) and exact-revision joins in the regenerated journal for both readings.\n\n"
    text += "## 2. Actor indices\n\nReceived weak uses / all weak uses is the corrected conditioning index; kept received / received is hold. N/A denotes a zero denominator. Rows apply at every seed.\n\n"
    text += tables.table(("Composition", *ACTOR_HEADER), [r for c, h in representatives.items() for r in _actor_rows(h, (c,))])
    text += "\nSources: [pair indices](TABLES/pair_per_actor_delivery.md#actor-indices), [pair-sterile indices](TABLES/pair-sterile_per_actor_delivery.md#actor-indices).\n\n"
    text += "## 3. Coverage across compositions\n\n"
    rows = []
    for c, h in representatives.items():
        w, n = _both(h)
        rows.append((c, len(w["received"]), len(n["received"]), tables.ratio(w["coverage"]["ratio"]), tables.ratio(n["coverage"]["ratio"])))
    rows.append(("triad (IEE/SLI/LIE)", "N/A", "N/A", "not producible", "not producible"))
    text += tables.table(("Composition", "Received wide", "Received narrow", "Coverage wide", "Coverage narrow"), rows)
    text += """\nThese values hold at every seed and through episode 0. Compare each reading
separately: coverage is identical across the supported pair compositions.
The wide reading records U11 delivery for both duality and conflict; narrow records none; this does not establish
relation independence generally. Eve is an inactive SLI in both compositions
and remains in the denominator. No IEE/SLI/LIE triad or third-person presence
comparison was producible with the authorized calls.

Sources: [pair population](TABLES/pair_per_population_delivery.md),
[pair-sterile population](TABLES/pair-sterile_per_population_delivery.md).

## 4. Sterile pairs and prediction

"""
    rows = []
    for c, h in representatives.items():
        w, n = _both(h)
        for p, q in zip(w["pairs"], n["pairs"]):
            if p["sender"] > p["receiver"]:
                continue
            rows.append((c, measures.actor_name(p["sender"]), measures.actor_name(p["receiver"]), p["relation"],
                         len(p["forward"]), len(q["forward"]), len(p["reverse"]), len(q["reverse"]), p["sterile"], q["sterile"]))
    text += tables.table(("Composition", "Source", "Receiver", "Relation", "Forward wide", "Forward narrow", "Reverse wide", "Reverse narrow", "Sterile wide", "Sterile narrow"), rows)
    text += "\nEach row includes both directions and holds across seeds. The name pair-sterile records the directive's conflict prediction, not the result. No independent yield-table artifact was located. Eve's zeros do not show intrinsic sterility. Sources: ordered-pair rows in both population tables.\n\n"
    text += "## 5. DCNH all-use versus received-and-kept\n\n"
    text += tables.table(("Composition", *DCNH_HEADER), [r for c, h in representatives.items() for r in _dcnh_rows(h, (c,))])
    text += "\nAll-use rows equal native Phase 7 observations. Comparisons use complete observations; a shared greatest cell alone is not agreement. Eve's agreement is between empty observations. Sources: [pair DCNH](TABLES/pair_dcnh_two_ways_delivery.md), [pair-sterile DCNH](TABLES/pair-sterile_dcnh_two_ways_delivery.md).\n\n"
    text += """## 6. Limits

Wide provenance is an upper bound: any exact operation input counts, including collective
evidence such as an invitation. Narrow removes generic input.N evidence, but
still assigns each operation's selected supplier tuple to every paid block.
Neither reading proves an element's semantic lineage, learning, or causation.

Only supplied generated workloads were measured. U11 emphasizes strong seats
and repeated work; retention is nearly saturated at this workload. Four seeds
vary only nonbinding budgets. Eve is always inactive. The requested triad was
not producible, so this is not a test of an added person's presence. No historical
archive was used. The circuit's existing paid damage renews supplied demand;
no new demand formation, feedback, regeneration, pricing, or Model G seats were
added. Read-engine hashes are unchanged. Undefined ratios remain N/A. See
[LIMITS.md](LIMITS.md) for consolidated bounds.
"""
    return text


def write(histories, delivery=False):
    """Write and return a report path from measured histories and report choice.

    Preserve I1-I5 via the renderers; enforce R3 text size (Batch 7 A/B and A5).
    """
    name = "REPORT_DELIVERY.md" if delivery else "REPORT.md"
    text = globals()["delivery"](histories) if delivery else population(histories)
    if len(text.encode()) >= 200000:
        raise ValueError("report exceeds R3")
    (PROJECT / name).write_text(text, encoding="utf-8")
    return name
