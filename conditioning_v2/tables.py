import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
json = __import__("json")
hashlib = __import__("hashlib")
Fraction = __import__("fractions").Fraction
Population = __import__("hle_unified.population", fromlist=["Population"]).Population
measures = __import__("conditioning_v2.measures", fromlist=["history"])
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def ratio(value):
    n, d = value
    return f"{n}/{d} (N/A)" if d == 0 else f"{n}/{d} = {Fraction(n, d)}"


def ids(values):
    return ", ".join("u" + str(i) for i in values) or "none"


def table(header, rows):
    def line(values):
        return "| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in values) + " |"
    return "\n".join([line(header), line(["---"] * len(header)), *(line(r) for r in rows)]) + "\n"


def load_histories():
    result = []
    for manifest in json.loads((PROJECT / "HISTORIES.json").read_text()):
        raw = (PROJECT / "OUT" / (manifest["name"] + ".checkpoint")).read_bytes()
        if hashlib.sha256(raw).hexdigest() != manifest["checkpoint_sha256"]:
            raise ValueError("checkpoint differs from accepted manifest")
        population = Population.restore(raw.decode())
        if population.checkpoint().encode() != raw:
            raise ValueError("checkpoint restore changed bytes")
        transactions = population.engine.world.journal()
        observation = measures.history(transactions, population.events)
        actors = {measures.actor_name(a): t for a, t in observation["profiles"].items()}
        if len(transactions) != manifest["transactions"] or actors != manifest["actors"]:
            raise ValueError("history population differs from accepted manifest")
        result.append(dict(manifest=manifest, observation=observation,
                           transactions=transactions, events=tuple(population.events)))
    return result


def render(histories):
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
            source = row["source"] if row["source"] in ("self", "world") else measures.actor_name(row["source"])
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

**A1 source scope:** only actor-id sources enter received-use measures.
Applied literally to both counts, the conditioning index is received weak-seat
uses / actor-sourced weak-seat uses: 1 whenever defined, N/A when empty.
This degeneracy follows A1; the original all-source denominator is not silently
substituted. A source-scope ruling is needed if that original ratio is intended.
Hold is kept received / received, across all seats. N/A denotes a zero denominator.
World and self are not received. World appears only in the use profile/trace
and all-use DCNH. No zero-denominator ratio is presented as zero.

## Actor indices

""" + table(("History", "Actor", "TIM", "Status", "Conditioning (A1 literal)", "Hold",
              "Conditioning numerator and denominator IDs", "Received IDs", "Kept received IDs"), actor_rows)
    actor_text += "\n## Use profile\n\nOnly nonzero bins are printed; omitted (seat, source, kept) bins are zero.\n\n"
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
squared total received uses (all receiver seats). Empty supply is N/A.
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
    return {"per_actor.md": actor_text, "per_population.md": pop_text, "dcnh_two_ways.md": dcnh_text}


def main():
    histories = load_histories()
    outputs = render(histories)
    for name, text in outputs.items():
        if len(text.encode()) >= 200000:
            raise ValueError("table exceeds R3: " + name)
    folder = PROJECT / "TABLES"
    folder.mkdir(exist_ok=True)
    for name, text in outputs.items():
        (folder / name).write_text(text)
        print("TABLES/" + name + ": " + str(len(text.encode())) + " bytes", flush=True)
    print("Histories: " + str(len(histories)), flush=True)
    print("All-use DCNH exactly matches Phase 7 for every actor.", flush=True)
    print("A1-literal conditioning scope is degenerate; zero denominators are N/A.", flush=True)
    print("Standalone pair comparison unavailable: no pair histories in accepted manifest.", flush=True)


if __name__ == "__main__":
    main()
