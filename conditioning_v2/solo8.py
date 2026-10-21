import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
json = __import__("json")
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
classes = __import__("conditioning_v2.classes", fromlist=["history"])
measures = tables.measures
model = measures.model
PROJECT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = "HISTORIES_SOLO8.json"
PREFIX = "pair-solo8_"


def _name(a):
    return measures.actor_name(a)


def _cls(r):
    return "O" if type(r["source"]) is tuple else r["source"][0].upper()


def sequences(h, reading="wide"):
    """Return per (actor, seat, element) source-class sequences and phase marks.

    Classes are S self, W world, O other (I2 tuple source), lower-case when not
    kept (I4). Records the transaction index of the last received use and of the
    first later self/world use at the same seat (I1 seat identity). Batch 9 §9.2.
    """
    obs = h["observation"] if reading == "wide" else h["narrow"]
    marks = h["manifest"]["phase_marks"]
    out = {}
    for i, (r, loc) in enumerate(zip(obs["records"], obs["locations"])):
        key = (r["actor"], r["seat"], r["element"])
        row = out.setdefault(key, dict(sequence="", last_received=None, first_self_after=None,
                                       collective="", solo="", probe=""))
        c = _cls(r) if r["kept"] else _cls(r).lower()
        row["sequence"] += c
        t = loc["transaction"]
        phase = "probe" if t < marks["probe_end"] else "collective" if t < marks["collective_end"] else "solo"
        row[phase] += c
        if type(r["source"]) is tuple:
            row["last_received"] = t
            row["first_self_after"] = None
        elif row["last_received"] is not None and row["first_self_after"] is None:
            row["first_self_after"] = t
    return out


def field_three_ways(h):
    """Return Alice's eight-seat field for probe+collective, solo, and whole history.

    Per seat: uses, hops, content, time, energy (CT Table 13), each with the DCNH
    greatest cells and margin via classes.summarize on the phase subset (I5
    counts preserved by construction). Batch 9 §9.2.
    """
    obs, marks = h["observation"], h["manifest"]["phase_marks"]
    kinds = h["classes"]
    out = {}
    for actor, row in obs["actors"].items():
        tim = row["tim"]
        phases = {}
        for label, lo, hi in (("collective", 0, marks["collective_end"]), ("solo", marks["collective_end"], marks["solo_end"]),
                              ("whole", 0, marks["solo_end"])):
            ids = [i for i in row["all_ids"] if lo <= obs["locations"][i]["transaction"] < hi]
            seats = {p: dict(element=model.element_at(tim, p), uses=0, hops=0, content=0, time=0, energy=0) for p in range(1, 9)}
            for i in ids:
                s, c = seats[obs["records"][i]["seat"]], kinds[i]
                s["uses"] += 1
                s["hops" if c["kind"] == "hop" else "content"] += 1
                s["time"] += c["time"]
                s["energy"] += c["energy"]
            d = measures.dcnh(actor, tim, (obs["records"][i] for i in ids))
            content = measures.dcnh(actor, tim, (obs["records"][i] for i in ids if kinds[i]["kind"] == "content"))
            phases[label] = dict(ids=tuple(ids), seats=seats, dcnh=dict(d, margin=classes.margin(d)),
                                 content_dcnh=dict(content, margin=classes.margin(content)))
        out[actor] = dict(tim=tim, phases=phases)
    return out


def render(histories):
    """Return the Batch 9 sequence and field tables for the solo8 histories.

    Additive to tables.render and classes.render (A8); every cell traces to
    per_actor's use trace (I5). Batch 9 §9.2.
    """
    seq_rows, field_rows = [], []
    for h in histories:
        name = h["manifest"]["name"]
        classes.history(h, "wide")
        for reading in ("wide", "narrow"):
            for (actor, seat, element), row in sorted(sequences(h, reading).items(), key=lambda kv: (_name(kv[0][0]), kv[0][1])):
                seq_rows.append((name, reading, _name(actor), seat, element, row["probe"] or "-", row["collective"] or "-",
                                 row["solo"] or "-", "-" if row["last_received"] is None else row["last_received"],
                                 "-" if row["first_self_after"] is None else row["first_self_after"]))
        for actor, data in field_three_ways(h).items():
            for label, ph in data["phases"].items():
                for p in range(1, 9):
                    s = ph["seats"][p]
                    field_rows.append((name, _name(actor), data["tim"], label, p, s["element"], model.fields(p)["dimensionality"],
                                       s["uses"], s["hops"], s["content"], s["time"], s["energy"],
                                       ",".join(ph["dcnh"]["cells_with_greatest_load"]) + " (" + str(ph["dcnh"]["margin"]) + ")",
                                       ",".join(ph["content_dcnh"]["cells_with_greatest_load"]) + " (" + str(ph["content_dcnh"]["margin"]) + ")"))
    seq_text = """# Source-class sequences — Batch 9 (pair-solo8)

Per (actor, seat, element), the source class of each paid use in transaction
order: S self, W world, O other-actor tuple; lower-case marks a use that is not
kept (no later same-seat use). Phases follow the manifest's phase marks: probe
(the uptake prerequisite), collective (the pair sequence), solo (the eight-element
program). The last two columns give the zero-based transaction index of the last
received use and of the first self/world use after it at that seat, if any.

""" + tables.table(("History", "Reading", "Actor", "Seat", "Element", "Probe", "Collective", "Solo",
                     "Last received tx", "First self/world after"), seq_rows)
    field_text = """# Eight-seat field three ways — Batch 9 (pair-solo8)

Each actor's field through the probe and collective phases, through the solo
phase alone, and over the whole history. Per seat: uses, hops, content, time and
CT Table 13 block energy. The greatest-load DCNH cells and margin are given for
all uses and for content only, over that phase's uses. Ties are ties; no subtype
is assigned.

""" + tables.table(("History", "Actor", "TIM", "Phase", "Seat", "Element", "Dim", "Uses", "Hops", "Content", "Time", "Energy",
                     "Greatest (margin)", "Greatest content (margin)"), field_rows)
    return {"sequence.md": seq_text, "field.md": field_text}


def report(histories, document):
    """Return REPORT_SOLO8.md (<= 500 words) from measured solo8 histories.

    States the prediction as recorded before generation, its outcome at every
    seed, the eight-seat field, prices, and internalisation (I5 preserved).
    Batch 9 §9.2.
    """
    first = histories[0]
    rows, seats_rows, intern_rows, refused = [], [], [], []
    for h in histories:
        name = h["manifest"]["name"]
        s = classes.history(h, "wide")
        n = classes.history(h, "narrow")
        alice = next(a for a in s["actors"] if a.key == "alice")
        bob = next(a for a in s["actors"] if a.key == "bob")
        a, b = s["actors"][alice], s["actors"][bob]
        intern_rows.append((name, tables.ratio(a["internalisation"]), tables.ratio(a["internal_by_seat"][5]),
                            tables.ratio(a["internal_by_seat"][6]), tables.ratio(n["actors"][alice]["internalisation"]),
                            tables.ratio(b["internalisation"]), ",".join(str(a["by_seat"][p]["content"]) for p in range(1, 9))))
        refused.extend((name, r["row"], r["key"], r["failure"]) for r in h["manifest"]["refused_rows"])
    f = field_three_ways(first)
    alice = next(a for a in f if a.key == "alice")
    for label, ph in f[alice]["phases"].items():
        rows.append((label, len(ph["ids"]), ",".join(str(ph["seats"][p]["content"]) for p in range(1, 9)),
                     ",".join(str(ph["seats"][p]["time"]) for p in range(1, 9)),
                     ",".join(ph["dcnh"]["cells_with_greatest_load"]) + " (" + str(ph["dcnh"]["margin"]) + ")",
                     ",".join(ph["content_dcnh"]["cells_with_greatest_load"]) + " (" + str(ph["content_dcnh"]["margin"]) + ")"))
    marks = first["manifest"]["phase_marks"]
    text = "# Function Conditioning — pair-solo8 report\n\n"
    text += "## 1. Prediction, recorded before generation\n\n> " + document["prediction"] + "\n\n"
    text += ("Composition: the setup11 workshop seeded on `WorkflowEngine` with the c7 workflow equipment, "
             "the uptake probe (Express/expenditure), the committed pair sequence, then the eight-element program "
             "(A9: " + str(len(document["program"])) + " rows). Phase marks (seed 17): probe " + str(marks["probe_end"])
             + ", collective " + str(marks["collective_end"]) + ", solo " + str(marks["solo_end"]) + " transactions.\n\n")
    text += "## 2. Outcome at every seed\n\n"
    text += tables.table(("History", "Alice internalisation wide", "Seat 5", "Seat 6", "Alice narrow", "Bob wide", "Alice content per seat 1-8"), intern_rows)
    text += "\nRefused rows: " + (", ".join(f"{n} row {r} ({k}: {f})" for n, r, k, f in refused) if refused else "none") + ". "
    text += ("Narrow is no longer empty: workflow operations declare `source.N`/`source_input`, so exchange replies "
             "produced by Bob are received under both readings in the solo phase (first narrow deliveries in the project).\n\n")
    text += "## 3. Alice's eight-seat field (seed 17)\n\n"
    text += tables.table(("Phase", "Uses", "Content per seat 1-8", "Time per seat 1-8", "Greatest (margin)", "Greatest content (margin)"), rows)
    text += ("\nSources: [field](TABLES/" + PREFIX + "field.md), [sequence](TABLES/" + PREFIX + "sequence.md), "
             "[classes](TABLES/" + PREFIX + "classes.md), [price of type](TABLES/" + PREFIX + "price_of_type.md), "
             "[per actor, seed 17](TABLES/" + PREFIX + "per_actor_seed-17.md).\n\n")
    text += """## 4. Limits

The solo phase is Alice's program; Share and Coordinate rows need a peer by the
fixture's construction, so Bob completes exchange replies and those rows' uses
are received under the wide reading. The workflow world's care stock holds two
units, so only the probe and row 2 consume care (A9). Seeds vary a nonbinding
budget. Internalisation counts a later self/world use at the same seat, of
either class; it does not show retained information. Everything else in
[LIMITS.md](LIMITS.md) applies.
"""
    return text


def main():
    """Write every pair-solo8 table and REPORT_SOLO8.md; verify I1-I5 on load.

    Runs tables.render, classes.render and render over the solo8 manifest with
    the pair-solo8_ prefix and no suffix; never touches other artifacts (A8).
    Batch 9 §9.2.
    """
    document = json.loads((PROJECT / MANIFEST).read_text())
    histories = tables.load_histories(MANIFEST)
    folder = PROJECT / "TABLES"
    outputs = {}
    renderers = (tables.render, classes.render, render)
    for renderer in renderers:
        for name, text in renderer(histories).items():
            stem = PREFIX + pathlib.Path(name).stem
            if len(text.encode()) < 200000:
                outputs[stem + ".md"] = text
                continue
            # R3: a table over 200 KB is split per history, one file per seed.
            for h in histories:
                part = renderer([h])[name]
                if len(part.encode()) >= 200000:
                    raise ValueError("table exceeds R3: " + name)
                outputs[stem + "_seed-" + str(h["manifest"]["seeds"]["fixture"]) + ".md"] = part
    for name, text in outputs.items():
        (folder / name).write_text(text, encoding="utf-8")
        print("TABLES/" + name + ": " + str(len(text.encode())) + " bytes", flush=True)
    text = report(histories, document)
    if len(text.split()) > 500:
        raise ValueError("REPORT_SOLO8.md exceeds 500 words")
    (PROJECT / "REPORT_SOLO8.md").write_text(text, encoding="utf-8")
    print("REPORT_SOLO8.md: " + str(len(text.split())) + " words", flush=True)


if __name__ == "__main__":
    main()
