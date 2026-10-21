import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
argparse = __import__("argparse")
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
measures = tables.measures
energy = measures.energy
model = measures.model
axes = measures.axes
PROJECT = pathlib.Path(__file__).resolve().parents[1]
KINDS = ("hop", "content")
RINGS = ("mental", "vital")
SUPPORT_SEATS = (5, 6, 7, 8)


def _route_kinds(d):
    kinds = []
    for i in range(d["route_count"]):
        prefix = f"route.{i}."
        paths = [k for k in d if k.startswith(prefix + "path.")]
        support, at = d[prefix + "support_seat"], d[prefix + "support_at"]
        if support not in SUPPORT_SEATS or type(at) is not int or not 0 <= at < len(paths):
            raise ValueError("route support seat outside the vital ring or support index out of range")
        kinds.extend([("hop", support, at)] * (len(paths) - 1) + [("content", support, at)])
    return kinds


def classify(transactions, records):
    """Return one class dict per paid use from the journal and Batch 3 records.

    Each dict holds kind (hop or content), time, energy (CT Table 13 block
    energy), ring, support_seat and support_at. Walks the same head-tracking
    and completion rule as measures.locate_uses so the i-th class is the i-th
    record (I5 canonical order and count); rejects any (actor, element)
    mismatch with the Batch 3 sequence (I1 alignment). Batch 8 §8.2; kinds are
    recovered from committed route.* attributes, never recomputed from routes.
    """
    records = tuple(records)
    heads, out = {}, []
    for tx in transactions:
        for version in tx.versions:
            d = energy.data(version)
            if d.get("record_type") == "operation":
                previous = heads.get(version.ref.identity)
                before = 0 if previous is None else energy.data(previous).get("completed", 0)
                tags = _route_kinds(d) if "route_count" in d else []
                j = 0
                for start, end, block_energy, element in energy.blocks(d):
                    if element is None:
                        continue
                    kind, support, at = tags[j]
                    j += 1
                    if not before < end <= d["completed"]:
                        continue
                    i = len(out)
                    if i >= len(records) or (records[i]["actor"], records[i]["element"]) != (d["actor"], element):
                        raise ValueError("use class trace differs from Batch 3 sequence")
                    seat = records[i]["seat"]
                    out.append(dict(kind=kind, time=end - start, energy=block_energy,
                                    ring=model.fields(seat)["ring"], support_seat=support, support_at=at))
            heads[version.ref.identity] = version
    if len(out) != len(records):
        raise ValueError("use class trace differs from Batch 3 sequence")
    validate(out, records)
    return tuple(out)


def validate(classes, records):
    """Reject forged class fields; enforce I1 seat/ring and I5 count alignment.

    A hop's time is the seat's CT TIME and its energy the seat's CT ENERGY; a
    content block's time is a positive multiple of TIME with energy scaled by
    that multiple. Support seats lie in the vital ring (5-8). Batch 8 §8.5.
    """
    classes, records = tuple(classes), tuple(records)
    if len(classes) != len(records):
        raise ValueError("use class count differs from records")
    for c, r in zip(classes, records):
        seat = r["seat"]
        unit, unit_energy = energy.TIME[seat - 1], energy.ENERGY[seat - 1]
        if c["kind"] not in KINDS or c["ring"] not in RINGS or c["support_seat"] not in SUPPORT_SEATS:
            raise ValueError("forged use class")
        if c["ring"] != model.fields(seat)["ring"]:
            raise ValueError("use class ring differs from seat")
        if type(c["time"]) is not int or c["time"] <= 0 or c["time"] % unit:
            raise ValueError("use class time differs from CT table")
        if c["kind"] == "hop" and c["time"] != unit:
            raise ValueError("hop time differs from CT table")
        if c["energy"] != unit_energy * (c["time"] // unit):
            raise ValueError("use class energy differs from CT table")


def kept_self(records):
    """Return per-use Booleans: a later self/world use at the same seat exists.

    Defined only as a property of received uses (I2 tuple source); for other
    uses it is reported but unused. Monotone under history growth as A2
    defines kept: True once the self-repeat is inside the history. Batch 8
    §8.3.3; preserves I1 by comparing seat and element together.
    """
    records = tuple(records)
    out = [False] * len(records)
    last_self = {}
    for i in range(len(records) - 1, -1, -1):
        r = records[i]
        key = (r["actor"], r["seat"], r["element"])
        out[i] = key in last_self
        if r["source"] in ("self", "world"):
            last_self[key] = i
    return tuple(out)


def margin(dcnh):
    """Return the lead of the greatest axis load over the runner-up, or N/A.

    Zero exactly when the greatest cell is tied; N/A when every load is zero.
    Reported, never interpreted (I5 loads unchanged). Batch 8 §8.3.5.
    """
    loads = sorted(dcnh["axis_loads"], reverse=True)
    if not any(loads):
        return "N/A"
    return loads[0] - loads[1]


def summarize(observation, classes):
    """Return Batch 8 per-actor and population measures from an observation.

    Additive to measures.summarize: conditioning/hold by class, kept_self and
    internalisation, observed supply and coverage, DCNH five ways with
    margins, and price of type. Enforces I5 (hop + content = all uses per
    actor) and I1 (seat/ring consistency through validate). Batch 8 §8.3.
    """
    records, locations = observation["records"], observation["locations"]
    classes = tuple(classes)
    validate(classes, records)
    self_kept = kept_self(records)
    received = observation["received"]
    content_before = {}
    for i, (r, c) in enumerate(zip(records, classes)):
        if c["kind"] == "content":
            content_before.setdefault((r["actor"], r["element"]), []).append(locations[i]["transaction"])
    actors = {}
    for actor, row in observation["actors"].items():
        tim, ids = row["tim"], row["all_ids"]
        by_kind = {k: tuple(i for i in ids if classes[i]["kind"] == k) for k in KINDS}
        if len(by_kind["hop"]) + len(by_kind["content"]) != len(ids):
            raise ValueError("use classes do not partition the actor's uses")
        weak = tuple(i for i in ids if records[i]["dim"] <= 2)
        incoming = row["incoming"]
        per_kind = {}
        for k in KINDS:
            kw = tuple(i for i in weak if classes[i]["kind"] == k)
            kr = tuple(i for i in incoming if classes[i]["kind"] == k)
            per_kind[k] = dict(conditioning=(len([i for i in kr if records[i]["dim"] <= 2]), len(kw)),
                               conditioning_ids=tuple(i for i in kr if records[i]["dim"] <= 2),
                               hold=(len([i for i in kr if records[i]["kept"]]), len(kr)),
                               hold_ids=tuple(i for i in kr if records[i]["kept"]))
        internal_ids = tuple(i for i in incoming if self_kept[i])
        internal_by_seat = {}
        for p in measures.WEAK:
            seat_in = tuple(i for i in incoming if records[i]["seat"] == p)
            internal_by_seat[p] = (len([i for i in seat_in if self_kept[i]]), len(seat_in))
        observed_ids, observed_suppliers = [], {p: {} for p in measures.WEAK}
        for i in row["conditioning_ids"]:
            r = records[i]
            for s in r["source"]:
                if any(t < locations[i]["transaction"] for t in content_before.get((s, r["element"]), ())):
                    observed_ids.append(i)
                    observed_suppliers[r["seat"]].setdefault(s, []).append(i)
        observed_ids = tuple(dict.fromkeys(observed_ids))
        views = {"all": ids, "received-kept": row["held"],
                 "content-only": by_kind["content"], "hop-only": by_kind["hop"]}
        dcnh = {}
        for view, sel in views.items():
            obs = measures.dcnh(actor, tim, (records[i] for i in sel))
            dcnh[view] = dict(obs, margin=margin(obs), ids=tuple(sel))
        if dcnh["all"] != dict(row["all_dcnh"], margin=dcnh["all"]["margin"], ids=tuple(ids)):
            raise ValueError("all-use DCNH differs from Batch 4 observation")
        price = dict(uses=len(ids), hops=len(by_kind["hop"]), content=len(by_kind["content"]),
                     time_total=sum(classes[i]["time"] for i in ids),
                     time_hop=sum(classes[i]["time"] for i in by_kind["hop"]),
                     time_content=sum(classes[i]["time"] for i in by_kind["content"]),
                     energy_total=sum(classes[i]["energy"] for i in ids))
        by_ring = {ring: dict(uses=0, hops=0, content=0, time=0, energy=0) for ring in RINGS}
        by_seat = {p: dict(element=model.element_at(tim, p), uses=0, hops=0, content=0, time=0, energy=0,
                           support_traffic=0) for p in range(1, 9)}
        for i in ids:
            c, p = classes[i], records[i]["seat"]
            for bucket in (by_ring[c["ring"]], by_seat[p]):
                bucket["uses"] += 1
                bucket["hops" if c["kind"] == "hop" else "content"] += 1
                bucket["time"] += c["time"]
                bucket["energy"] += c["energy"]
            if c["kind"] == "hop" and p == c["support_seat"]:
                by_seat[p]["support_traffic"] += 1
        actors[actor] = dict(tim=tim, active=row["active"], by_kind=by_kind, per_kind=per_kind,
                             internalisation=(len(internal_ids), len(incoming)), internal_ids=internal_ids,
                             internal_by_seat=internal_by_seat,
                             observed_ids=observed_ids, observed_suppliers=observed_suppliers,
                             dcnh=dcnh, price=price, by_ring=by_ring, by_seat=by_seat)
    qualifying = tuple(i for a in actors.values() for i in a["observed_ids"]
                       if any(model.fields(s)["dimensionality"] >= 3 for s in records[i]["source_seat"]))
    pairs = tuple(sorted({(records[i]["actor"], records[i]["seat"]) for i in qualifying}))
    denominator = observation["coverage"]["denominator"]
    if len(pairs) > observation["coverage"]["ratio"][0]:
        raise ValueError("observed coverage exceeds structural coverage")
    return dict(actors=actors, kept_self=self_kept,
                observed_coverage=dict(ratio=(len(pairs), len(denominator)), pairs=pairs, ids=qualifying),
                structural_coverage=observation["coverage"])


def history(h, reading="wide"):
    """Return Batch 8 measures for one loaded history under a reading.

    Reuses the loaded observation (wide) or the narrow observation; classes
    are reading-independent and computed once (I5). Batch 8 §8.3.
    """
    observation = h["observation"] if reading == "wide" else (
        h.get("narrow") or measures.history(h["transactions"], h["events"], "narrow"))
    classes = h.get("classes")
    if classes is None:
        classes = h["classes"] = classify(h["transactions"], h["observation"]["records"])
    return summarize(observation, classes)


def _name(a):
    return measures.actor_name(a)


def render(histories):
    """Return the three Batch 8 Markdown tables for a list of loaded histories.

    Existing Batch 4-7 tables are not touched (A5 preserved); every cell here
    is additive and traced by use IDs into per_actor's trace (I5). Batch 8 §8.4.
    """
    class_rows, trace_rows, seat_rows, obs_rows = [], [], [], []
    price_rows, seat_price_rows, dcnh_rows = [], [], []
    for h in histories:
        name = h["manifest"]["name"]
        wide, narrow = history(h, "wide"), history(h, "narrow")
        classes = h["classes"]
        for actor, w in wide["actors"].items():
            n = narrow["actors"][actor]
            label, status = _name(actor), "active" if w["active"] else "inactive"
            for k in KINDS:
                class_rows.append((name, label, w["tim"], status, k,
                                   tables.ratio(w["per_kind"][k]["conditioning"]), tables.ratio(n["per_kind"][k]["conditioning"]),
                                   tables.ratio(w["per_kind"][k]["hold"]), tables.ratio(n["per_kind"][k]["hold"]),
                                   tables.ids(w["per_kind"][k]["conditioning_ids"]), tables.ids(w["per_kind"][k]["hold_ids"])))
            class_rows.append((name, label, w["tim"], status, "internalisation",
                               tables.ratio(w["internalisation"]), tables.ratio(n["internalisation"]),
                               "", "", tables.ids(w["internal_ids"]), ""))
            for p in measures.WEAK:
                seat_rows.append((name, label, p, tables.ratio(w["internal_by_seat"][p]), tables.ratio(n["internal_by_seat"][p]),
                                  ", ".join(_name(s) + " x" + str(len(v)) for s, v in sorted(w["observed_suppliers"][p].items())) or "none"))
            price_rows.append((name, label, w["tim"], status, *(w["price"][k] for k in
                               ("uses", "hops", "content", "time_total", "time_hop", "time_content", "energy_total")),
                               *(w["by_ring"][r][k] for r in RINGS for k in ("uses", "hops", "content", "time", "energy"))))
            for p in range(1, 9):
                s = w["by_seat"][p]
                seat_price_rows.append((name, label, w["tim"], p, s["element"], model.fields(p)["dimensionality"],
                                        model.fields(p)["ring"], s["uses"], s["hops"], s["content"], s["time"],
                                        s["energy"], s["support_traffic"]))
            for view in ("all", "received-kept", "content-only", "hop-only"):
                for reading, data in (("wide", w), ("narrow", n)):
                    if view != "received-kept" and reading == "narrow":
                        continue
                    d = data["dcnh"][view]
                    dcnh_rows.append((name, label, w["tim"], status, view, reading if view == "received-kept" else "both",
                                      len(d["ids"]), ",".join(map(str, d["axis_loads"])), ",".join(d["axis_cells"]),
                                      ",".join(d["cells_with_greatest_load"]), d["margin"],
                                      ",".join(str(d["formula_sums"][c]) for c in "DCNH"), tables.ids(d["ids"])))
        for i, c in enumerate(classes):
            trace_rows.append((name, "u" + str(i), c["kind"], c["time"], c["energy"], c["ring"], c["support_seat"], c["support_at"]))
        obs_rows.append((name, tables.ratio(wide["structural_coverage"]["ratio"]), tables.ratio(wide["observed_coverage"]["ratio"]),
                         tables.ratio(narrow["structural_coverage"]["ratio"]), tables.ratio(narrow["observed_coverage"]["ratio"]),
                         tables.ids(wide["observed_coverage"]["ids"])))
    class_text = """# Use classes — Batch 8

A paid use is a hop (an arrival along route.{i}.path.{n}, n >= 1) or a content
block (the route's seat-content work). Conditioning by class is received weak
uses of that class / all weak uses of that class; hold by class is kept received
/ received of that class. Internalisation is received uses later followed by a
self- or world-sourced use at the same seat and element / received uses; it is
reported per weak seat below. Observed suppliers are listed only where the
supplier completed a content block at that element earlier in the history.
Use IDs refer to per_actor's trace in the same history. N/A is a zero denominator.

## Conditioning, hold and internalisation by class

""" + tables.table(("History", "Actor", "TIM", "Status", "Class", "Conditioning wide", "Conditioning narrow",
                     "Hold wide", "Hold narrow", "Conditioning numerator IDs", "Kept received IDs"), class_rows)
    class_text += "\n## Internalisation and observed suppliers per weak seat\n\n"
    class_text += tables.table(("History", "Actor", "Seat", "Internalisation wide", "Internalisation narrow", "Observed suppliers (wide)"), seat_rows)
    class_text += "\n## Structural versus observed coverage\n\nStructural coverage is the Batch 4 column (supplier holds the element at a strong seat). Observed coverage additionally requires an earlier content block by the supplier at that element.\n\n"
    class_text += tables.table(("History", "Structural wide", "Observed wide", "Structural narrow", "Observed narrow", "Observed use IDs"), obs_rows)
    class_text += "\n## Use class trace\n\nAligned with per_actor's use trace. Energy is CT Table 13 block energy (the grade-v1 debit), not the legacy-r4 wallet debit.\n\n"
    class_text += tables.table(("History", "Use ID", "Kind", "Time", "Energy", "Ring", "Support seat", "Support at"), trace_rows)
    price_text = """# Price of type — Batch 8

Per actor: uses, hops, content blocks, time (hop, content, total) and CT Table 13
block energy, then the same by ring. Per seat: the same with the seat's element,
dimensionality and ring, and support traffic (hops arriving at the route's own
support seat). Energy is the grade-v1 block debit regardless of resource model;
it is not the legacy-r4 wallet debit. These are observations of a supplied
program's cost; they assign nothing.

## Per actor

""" + tables.table(("History", "Actor", "TIM", "Status", "Uses", "Hops", "Content", "Time", "Time hop", "Time content", "Energy",
                     "Mental uses", "Mental hops", "Mental content", "Mental time", "Mental energy",
                     "Vital uses", "Vital hops", "Vital content", "Vital time", "Vital energy"), price_rows)
    price_text += "\n## Per seat\n\n" + tables.table(("History", "Actor", "TIM", "Seat", "Element", "Dim", "Ring", "Uses", "Hops", "Content", "Time", "Energy", "Support traffic"), seat_price_rows)
    dcnh_text = """# DCNH five ways — Batch 8

The Batch 4 two views (all uses; received and kept, per reading) are repeated
unchanged, followed by content-only and hop-only views. Margin is the greatest
axis load minus the runner-up: 0 when the greatest cell is tied, N/A when every
load is zero. All ties are retained; no threshold is applied; no subtype is
assigned. Axis order is (1,3), (2,4), (5,7), (6,8); formula order is D,C,N,H.

""" + tables.table(("History", "Actor", "TIM", "Status", "View", "Reading", "Uses", "Loads", "Axis cells",
                     "Greatest-load cells", "Margin", "Formula sums", "Use IDs"), dcnh_rows)
    return {"classes.md": class_text, "price_of_type.md": price_text, "dcnh_five_ways.md": dcnh_text}


def _short(value):
    n, d = value
    return "N/A" if d == 0 else str(n) + "/" + str(d)


def report_section(histories, delivery):
    """Return the Batch 8 report section (<= 300 words) for the given histories.

    Every number is read from the Batch 8 measures (I5 preserved); seeds that
    agree are collapsed and disagreement raises. Batch 8 §8.4.
    """
    groups = {}
    for h in histories:
        groups.setdefault(h["manifest"].get("composition", ""), []).append(h)
    rows, lines = [], []
    for composition, items in groups.items():
        summaries = [history(h, "wide") for h in items]
        keyed = [tuple((a, r["price"], r["per_kind"]["content"]["conditioning"], r["per_kind"]["hop"]["conditioning"],
                        r["internalisation"], {v: (d["cells_with_greatest_load"], d["margin"]) for v, d in r["dcnh"].items()})
                       for a, r in w["actors"].items()) + (w["structural_coverage"]["ratio"], w["observed_coverage"]["ratio"])
                 for w in summaries]
        if any(k != keyed[0] for k in keyed):
            raise ValueError("Batch 8 report rows differ across seeds")
        w = summaries[0]
        prefix = (composition,) if composition else ()
        inactive = [_name(a) for a, r in w["actors"].items() if not r["active"]]
        for a, r in w["actors"].items():
            if not r["active"]:
                continue
            cell = lambda v: ",".join(r["dcnh"][v]["cells_with_greatest_load"]) + " (" + str(r["dcnh"][v]["margin"]) + ")"
            rows.append((*prefix, _name(a), r["tim"], r["price"]["hops"], r["price"]["content"],
                         _short(r["per_kind"]["content"]["conditioning"]), _short(r["per_kind"]["hop"]["conditioning"]),
                         _short(r["internalisation"]), cell("all"), cell("content-only"), cell("hop-only"),
                         r["price"]["time_total"], r["price"]["energy_total"]))
        lines.append(((composition + " ") if composition else "") + "coverage: structural "
                     + _short(w["structural_coverage"]["ratio"]) + ", observed "
                     + _short(w["observed_coverage"]["ratio"]) + (
                     "; inactive (all N/A): " + ", ".join(inactive) if inactive else "") + ".")
    header = (("Composition",) if "" not in groups else ()) + (
        "Actor", "TIM", "Hops", "Content", "Cond. content", "Cond. hop", "Internalisation",
        "Greatest all (margin)", "Greatest content (margin)", "Greatest hop (margin)", "Time", "Energy")
    prefix = "pair_" if delivery else ""
    suffix = "_delivery" if delivery else ""
    text = "## 8. Use classes and price of type\n\nWide reading; rows hold at every seed; N/A is a zero denominator. Cond. by class: received weak uses of the class / all weak uses of the class. Internalisation: received uses later followed by a self/world use at the same seat / received uses. Margin: greatest axis load minus runner-up. Energy is CT Table 13 block energy, not a legacy-r4 wallet debit.\n\n"
    text += tables.table(header, rows)
    text += "\n" + " ".join(lines) + " Narrow finds no received uses, so its class indices and internalisation are 0 or N/A. "
    text += ("Sources: [classes](TABLES/" + prefix + "classes" + suffix + ".md), [price of type](TABLES/" + prefix
             + "price_of_type" + suffix + ".md), [DCNH five ways](TABLES/" + prefix + "dcnh_five_ways" + suffix + ".md)"
             + (", and the pair-sterile files" if delivery else "") + ".\n")
    return text


def main():
    """Write the Batch 8 tables and append the report section for one manifest.

    Existing TABLES and the report text above the Batch 8 heading are left
    byte-identical (A5); only Batch 8 files and the trailing section are
    written (I5 traced). Batch 8 §8.4.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--histories", default="HISTORIES.json")
    parser.add_argument("--report", default=None)
    args = parser.parse_args()
    histories = tables.load_histories(args.histories)
    suffix = "" if args.histories == "HISTORIES.json" else ("_delivery" if args.histories == "HISTORIES_DELIVERY.json" else "_" + pathlib.Path(args.histories).stem.split("_", 1)[1].lower())
    groups = {}
    for h in histories:
        groups.setdefault(h["manifest"].get("composition", ""), []).append(h)
    folder = PROJECT / "TABLES"
    for composition, items in groups.items():
        prefix = composition + "_" if composition else ""
        for name, text in render(items).items():
            if len(text.encode()) >= 200000:
                raise ValueError("table exceeds R3: " + name)
            out = prefix + pathlib.Path(name).stem + suffix + ".md"
            (folder / out).write_text(text, encoding="utf-8")
            print("TABLES/" + out + ": " + str(len(text.encode())) + " bytes", flush=True)
    report = args.report or ("REPORT.md" if args.histories == "HISTORIES.json" else
                             "REPORT_DELIVERY.md" if args.histories == "HISTORIES_DELIVERY.json" else None)
    if report:
        path = PROJECT / report
        text = path.read_text(encoding="utf-8")
        marker = "\n## 8. "
        if marker in text:
            text = text[:text.index(marker) + 1]
        section = report_section(histories, delivery=report != "REPORT.md")
        if len(section.split()) > 300:
            raise ValueError("Batch 8 section exceeds 300 words")
        text = text.rstrip("\n") + "\n\n" + section
        if len(text.encode()) >= 200000:
            raise ValueError("report exceeds R3")
        path.write_text(text, encoding="utf-8")
        print(report + ": Batch 8 section written", flush=True)


if __name__ == "__main__":
    main()
