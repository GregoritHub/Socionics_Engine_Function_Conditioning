import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
json = __import__("json")
hashlib = __import__("hashlib")
Fraction = __import__("fractions").Fraction
argparse = __import__("argparse")
Population = __import__("hle_unified.population", fromlist=["Population"]).Population
OperationStore = __import__("hle_unified.operations", fromlist=["OperationStore"]).OperationStore
ObjectId = __import__("hle_unified.records", fromlist=["ObjectId"]).ObjectId
measures = __import__("conditioning_v2.measures", fromlist=["history"])
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def ratio(value):
    """Format an integer numerator/denominator; preserve I5 counts (Batch 4/7 A1)."""
    n, d = value
    return f"{n}/{d} (N/A)" if d == 0 else f"{n}/{d} = {Fraction(n, d)}"


def ids(values):
    """Format occurrence indices as trace IDs; preserve I5 identity (Batch 4)."""
    return ", ".join("u" + str(i) for i in values) or "none"


def table(header, rows):
    """Render headings and rows as Markdown; preserve I5 cell values (Batch 4)."""
    def line(values):
        return "| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in values) + " |"
    return "\n".join([line(header), line(["---"] * len(header)), *(line(r) for r in rows)]) + "\n"


def load_histories(manifest_path="HISTORIES.json"):
    """Restore a manifest and return histories with wide/narrow observations.

    Enforce I1-I5 through measures.history plus manifest/codec identity; Batch 4,
    A4 and Batch 7 A2/A5. Engine checkpoints are read, never edited.
    """
    result = []
    document = json.loads((PROJECT / manifest_path).read_text())
    entries = document["histories"] if isinstance(document, dict) else document
    for manifest in entries:
        raw = (PROJECT / "OUT" / (manifest["name"] + ".checkpoint")).read_bytes()
        if hashlib.sha256(raw).hexdigest() != manifest["checkpoint_sha256"]:
            raise ValueError("checkpoint differs from accepted manifest")
        if manifest.get("checkpoint_codec") == "OperationStore":
            world = OperationStore.restore(raw.decode())
            if world.checkpoint().encode() != raw:
                raise ValueError("checkpoint restore changed bytes")
            transactions = world.journal()
            event_records = (document["event_sets"][manifest["events_ref"]]
                             if "events_ref" in manifest else manifest["events"])
            if "events_ref" in manifest and hashlib.sha256(
                    json.dumps(event_records, sort_keys=True).encode()).hexdigest() != manifest["events_ref"]:
                raise ValueError("episode event set differs from manifest hash")
            events = tuple(dict(actor=ObjectId(*e["actor"].split(":", 1)),
                                key=e["key"], episode=e["episode"])
                           for e in event_records)
        else:
            population = Population.restore(raw.decode())
            if population.checkpoint().encode() != raw:
                raise ValueError("checkpoint restore changed bytes")
            transactions, events = population.engine.world.journal(), population.events
        observation = measures.history(transactions, events)
        actors = {measures.actor_name(a): t for a, t in observation["profiles"].items()}
        if len(transactions) != manifest["transactions"] or actors != manifest["actors"]:
            raise ValueError("history population differs from accepted manifest")
        narrow = measures.history(transactions, events, "narrow")
        result.append(dict(manifest=manifest, observation=observation, narrow=narrow,
                           transactions=transactions, events=tuple(events)))
    return result


def _render_reading(histories):
    actor_rows, profile_rows, supplier_rows, trace_rows = [], [], [], []
    population_rows, episode_rows, pair_rows, benefit_rows, input_rows = [], [], [], [], []
    dcnh_rows = []
    for history in histories:
        manifest, data = history["manifest"], history["observation"]
        name = manifest["name"]
        input_rows.append((name, manifest["model"], manifest["seeds"]["fixture"],
                           len(data["profiles"]), manifest["transactions"], manifest["checkpoint_sha256"]))
        for actor, row in data["actors"].items():
            label = measures.actor_name(actor)
            status = "active" if row["active"] else "inactive"
            actor_rows.append((name, label, row["tim"], status,
                               ratio(row["conditioning"]), ratio(row["hold"]),
                               ids(row["conditioning_ids"]), ids(row["incoming"]), ids(row["held"])))
            for (seat, source, kept), trace in sorted(row["profile"].items()):
                profile_rows.append((name, label, seat, source, kept, len(trace), ids(trace)))
            for seat, suppliers in row["suppliers"].items():
                if not suppliers:
                    supplier_rows.append((name, label, seat, "none", 0, "none"))
                for source, trace in sorted(suppliers.items()):
                    supplier_rows.append((name, label, seat, measures.actor_name(source), len(trace), ids(trace)))
            for mode, dcnh, trace in (("all uses", row["all_dcnh"], row["all_ids"]),
                                      ("received and kept", row["received_kept_dcnh"], row["held"])):
                compare = "agree" if row["all_dcnh"] == row["received_kept_dcnh"] else "diverge"
                dcnh_rows.append((name, label, row["tim"], status, mode, len(trace),
                                  ",".join(map(str, dcnh["axis_loads"])),
                                  ",".join(map(str, dcnh["axis_tilts"])),
                                  ",".join(dcnh["axis_cells"]),
                                  ",".join(dcnh["cells_with_greatest_load"]),
                                  ",".join(str(dcnh["formula_sums"][c]) for c in 'DCNH'),
                                  compare, ids(trace)))
        for i, (row, loc) in enumerate(zip(data["records"], data["locations"])):
            source = (row["source"] if row["source"] in ("self", "world")
                      else "(" + ", ".join(measures.actor_name(s) for s in row["source"]) + ")")
            ref = loc["operation"]
            trace_rows.append((name, "u" + str(i), loc["transaction"],
                               measures.actor_name(ref.identity) + "@" + str(ref.revision),
                               loc["block_end"], measures.actor_name(row["actor"]),
                               row["element"], row["seat"], row["dim"], source,
                               row["kept"], loc["episode"]))
        population_rows.append((name, len(data["profiles"]),
                                sum(not r["active"] for r in data["actors"].values()),
                                len(data["received"]), ratio(data["coverage"]["ratio"]),
                                ratio(data["concentration"]),
                                sum(p["sterile"] for p in data["pairs"]),
                                len(data["benefit_ids"]), ids(data["coverage"]["ids"])))
        for episode, cov in data["episode_coverage"].items():
            episode_rows.append((name, episode, ratio(cov["ratio"]), ids(cov["ids"])))
        for pair in data["pairs"]:
            sender, receiver = measures.actor_name(pair["sender"]), measures.actor_name(pair["receiver"])
            pair_rows.append((name, sender, receiver, pair["relation"], len(pair["forward"]),
                              len(pair["reverse"]), pair["sterile"], ids(pair["forward"]), ids(pair["reverse"])))
            if pair["relation"] in measures.BENEFIT:
                benefit_rows.append((name, sender, receiver, pair["relation"], len(pair["forward"]),
                                     len(data["benefit_ids"]), "N/A: not generated", ids(pair["forward"])))

    actor_text = """# Per-actor measures — Batch 4

Use IDs uN are zero-based occurrences in Batch 3's unchanged record sequence,
scoped to the History column. The use trace below links each to its committed
transaction, exact operation revision, and block completion boundary. Empty
ID lists mean zero observed uses, not missing histories. Inactive means zero
completed paid uses; such actors remain in population denominators.

**Batch 7 conditioning index:** received uses at dim <= 2 divided by ALL
uses at dim <= 2, per actor. The numerator IDs are listed; denominator IDs
are every row for that actor with Dim <= 2 in the use trace below.
Hold is kept received / received, across all seats. N/A denotes a zero denominator.
World and self are not received; they contribute to the weak-use denominator,
use profile/trace and all-use DCNH. No zero-denominator ratio is presented as zero.

## Actor indices

""" + table(("History", "Actor", "TIM", "Status", "Conditioning", "Hold",
              "Conditioning numerator IDs", "Received IDs", "Kept received IDs"), actor_rows)
    actor_text += "\n## Use profile\n\nBins present in either reading are printed; omitted (seat, source, kept) bins are zero in both.\n\n"
    actor_text += table(("History", "Actor", "Seat", "Source class", "Kept", "Count", "Use IDs"), profile_rows)
    actor_text += "\n## Weak-seat supplier map\n\nEach dim <= 2 seat is listed, including empty supplier sets.\n\n"
    actor_text += table(("History", "Receiver", "Seat", "Supplier", "Count", "Use IDs"), supplier_rows)
    actor_text += "\n## Use trace\n\nTransaction and episode indices are zero-based.\n\n"
    actor_text += table(("History", "Use ID", "Transaction", "Operation revision", "Block end",
                         "Actor", "Element", "Seat", "Dim", "Source", "Kept", "Episode"), trace_rows)

    pop_text = """# Per-population measures — Batch 4

Only actor-id sources count as received. Coverage counts distinct receiver/seat
pairs at dim <= 2 supplied by a producer holding that element at dim >= 3,
divided by every committed actor's dim <= 2 seats, including inactive actors.
Supplier concentration is HHI: sum of squared supplier received-use counts /
squared total supplier incidences (all receiver seats). Empty supply is N/A.
Sterile ordered pairs require zero received uses in BOTH directions; both
ordered directions are listed, with the kernel's directional relation labels.
Relation names are read from the pinned kernel label file and their landing
permutations are checked against hle.relations. No labels are inferred.

## Accepted inputs

""" + table(("History", "Model", "Seed", "Actors", "Transactions", "Checkpoint SHA-256"), input_rows)
    pop_text += "\n## Population summary\n\n" + table(("History", "Actors", "Inactive", "Received uses", "Coverage",
                  "Supplier HHI", "Sterile ordered pairs", "Benefit-family uses", "Coverage use IDs"), population_rows)
    pop_text += "\n## Coverage by episode index\n\nCumulative through each actor-local episode index, pooled across actors; not a wall-clock snapshot. The denominator is fixed, including inactive actors.\n\n"
    pop_text += table(("History", "Through episode", "Coverage", "Qualifying use IDs"), episode_rows)
    pop_text += "\n## Ordered pairs\n\nForward means source -> receiver. An empty ID set is an observed zero.\n\n"
    pop_text += table(("History", "Source", "Receiver", "Relation", "Forward uses", "Reverse uses", "Sterile", "Forward IDs", "Reverse IDs"), pair_rows)
    pop_text += "\n## Benefit pairs within the triad versus triad total\n\nPair-subset counts are observations WITHIN the same triad, not independent two-actor experiments. Benefit-family totals include benefit and benefit_inverse directions. The accepted manifest has no standalone pair histories; their comparison is unavailable, not zero.\n\n"
    pop_text += table(("History", "Source", "Receiver", "Relation", "Pair-subset uses", "Triad benefit-family uses", "Standalone pair uses", "Pair-subset IDs"), benefit_rows)

    dcnh_text = """# DCNH two ways — Batch 4

All-use rows are reconstructed from Batch 3 records and checked for exact
equality to the full Phase 7 conditioning_audit.observations row per actor.
The other view includes actor-sourced AND kept uses only, across all seats.
Axis order is (1,3), (2,4), (5,7), (6,8); formula order is D,C,N,H. All ties
are retained. A zero received-and-kept vector ties every cell and is absence
of input, not evidence of a subtype. No subtype assignment is made.
Agreement compares the complete observation, not just the largest-load label.
Use IDs refer to per_actor.md's trace in the same history.

""" + table(("History", "Actor", "TIM", "Status", "View", "Uses", "Loads", "Tilts", "Axis cells",
              "Greatest-load cells", "Formula sums", "Comparison", "Use IDs"), dcnh_rows)
    outputs = {"per_actor.md": actor_text, "per_population.md": pop_text, "dcnh_two_ways.md": dcnh_text}
    if histories and "composition" in histories[0]["manifest"]:
        for name, text in outputs.items():
            text = text.replace("Batch 4", "Batch 6").replace("actor-id sources", "non-empty actor tuples")
            text = text.replace("squared total supplier incidences (all receiver seats)",
                                "squared total supplier incidences (all receiver seats)")
            text = text.replace("Cumulative through each actor-local episode index, pooled across actors; not a wall-clock snapshot.",
                                "Cumulative through explicitly recorded harness episodes, including preparation; not scheduler episodes.")
            text = text.replace("Benefit pairs within the triad versus triad total", "Benefit-family pairs within the composition")
            text = text.replace("Pair-subset counts are observations WITHIN the same triad, not independent two-actor experiments. Benefit-family totals include benefit and benefit_inverse directions. The accepted manifest has no standalone pair histories; their comparison is unavailable, not zero.",
                                "Pair counts are within the recorded composition. The requested IEE/SLI/LIE triad is not producible; a standalone pair-versus-that-triad comparison is unavailable, not zero.")
            text = text.replace("Triad benefit-family uses", "Composition benefit-family uses")
            text = text.replace("Use IDs refer to per_actor.md's trace", "Use IDs refer to the matching composition's per-actor trace")
            outputs[name] = text + "\nWide (A3/A4): any exact operation input counts, including collective evidence. A use counts once in its receiver profile and once per listed supplier in supplier/pair counts.\n"
    return outputs



def _paired_tables(wide, narrow):
    # Keep existing wide rows/cells, add narrow measurements alongside them.
    # Shared trace columns avoid repeating the expensive operation identifiers.
    wlines, nlines = wide.splitlines(), narrow.splitlines()
    def blocks(lines):
        result, index = [], 0
        while index < len(lines):
            if lines[index].startswith("| "):
                end = index
                while end < len(lines) and lines[end].startswith("| "):
                    end += 1
                cells = [[v.strip() for v in line.strip().strip("|").split("|")]
                         for line in lines[index:end]]
                result.append((index, end, cells[0], cells[2:]))
                index = end
            else:
                index += 1
        return result
    wb, nb = blocks(wlines), blocks(nlines)
    if len(wb) != len(nb):
        raise ValueError("reading table structures differ")
    for (start, end, header, rows), (_, _, nh, nr) in reversed(list(zip(wb, nb))):
        if header != nh:
            raise ValueError("reading headers differ")
        if "Checkpoint SHA-256" in header:
            if rows != nr:
                raise ValueError("reading inputs differ")
            continue
        if "Use ID" in header:
            if len(rows) != len(nr):
                raise ValueError("reading use counts differ")
            idx = header.index("Source")
            merged = []
            for w, n in zip(rows, nr):
                if w[:idx] + w[idx+1:] != n[:idx] + n[idx+1:]:
                    raise ValueError("reading changed source-independent use")
                merged.append(w[:idx] + [w[idx], n[idx]] + w[idx+1:])
            names = header[:idx] + ["Source wide", "Source narrow"] + header[idx+1:]
            names[names.index("Kept")] = "Kept (both)"
        elif "View" in header:
            names = [*header, "Reading"]
            merged = [row + [reading] for w, n in zip(rows, nr)
                      for row, reading in ((w, "wide"), (n, "narrow"))]
        else:
            shared = (5 if "Source class" in header else
                      4 if "Supplier" in header or "Relation" in header or "TIM" in header else
                      3 if "Inactive" in header else 2)
            wm = {tuple(r[:shared]): r[shared:] for r in rows}
            nm = {tuple(r[:shared]): r[shared:] for r in nr}
            keys = list(wm) + [k for k in nm if k not in wm]
            empty = ["0", "none"]
            if any(k not in wm or k not in nm for k in keys) and header[shared:] != ["Count", "Use IDs"]:
                raise ValueError("unexpected missing reading row")
            names = header[:shared] + [h + " wide" for h in header[shared:]] + [h + " narrow" for h in header[shared:]]
            merged = [list(k) + wm.get(k, empty) + nm.get(k, empty) for k in keys]
            if "Kept" in names:
                names[names.index("Kept")] = "Kept (both)"
        wlines[start:end] = table(names, merged).rstrip().splitlines()
    text = "\n".join(wlines) + "\n"
    intro = ("\n**Readings:** wide = source.N + source_input + input.N (A3/A4); "
             "narrow = source.N + source_input only (Batch 7). Shared columns, "
             "including kept, are identical under both readings. New zero bins "
             "show where only the other reading has observations.\n")
    text = text.replace("— Batch 4", "— Batch 7").replace("— Batch 6", "— Batch 7")
    first = text.index("\n")
    return text[:first+1] + intro + text[first+1:]


def render(histories):
    """Return three Markdown tables from histories, with both readings adjacent.

    Preserve I1-I5 and wide cells except the corrected conditioning column;
    A5 checks this projection against Batch 6. Batch 7 A1/A2 defines new cells.
    """
    wide = _render_reading(histories)
    narrow_histories = [dict(h, observation=h.get("narrow") or
                       measures.history(h["transactions"], h["events"], "narrow"))
                       for h in histories]
    narrow = _render_reading(narrow_histories)
    return {name: _paired_tables(text, narrow[name]) for name, text in wide.items()}

def main():
    """Render both readings and the report for a CLI manifest; verify I1-I5.

    Outputs deterministic small UTF-8 artifacts (Batch 7 A/B; A5 guard).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--histories", default="HISTORIES.json")
    parser.add_argument("--suffix", default=None)
    args = parser.parse_args()
    histories = load_histories(args.histories)
    suffix = args.suffix if args.suffix is not None else ("" if args.histories == "HISTORIES.json" else "_delivery")
    if any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for c in suffix):
        raise ValueError("invalid output suffix")
    groups = {}
    for history in histories:
        groups.setdefault(history["manifest"].get("composition", ""), []).append(history)
    outputs = {}
    for composition, items in groups.items():
        prefix = composition + "_" if composition else ""
        for name, text in render(items).items():
            outputs[prefix + pathlib.Path(name).stem + suffix + ".md"] = text
    for name, text in outputs.items():
        if len(text.encode()) >= 200000:
            raise ValueError("table exceeds R3: " + name)
    folder = PROJECT / "TABLES"
    folder.mkdir(exist_ok=True)
    for name, text in outputs.items():
        (folder / name).write_text(text)
        print("TABLES/" + name + ": " + str(len(text.encode())) + " bytes", flush=True)
    reports = __import__("conditioning_v2.reports", fromlist=["write"])
    reports.write(histories, delivery=args.histories != "HISTORIES.json")
    print("Histories: " + str(len(histories)), flush=True)
    print("All-use DCNH exactly matches Phase 7 for every actor.", flush=True)
    print("Wide and narrow provenance; conditioning = received weak / all weak; empty denominators are N/A.", flush=True)
    if args.histories == "HISTORIES.json":
        print("Standalone pair comparison unavailable: no pair histories in accepted manifest.", flush=True)
    else:
        print("Delivery tables are separated by composition; unavailable compositions remain in the manifest.", flush=True)


if __name__ == "__main__":
    main()
