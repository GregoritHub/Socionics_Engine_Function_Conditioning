import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

# Historical A4 byte-identity guard for the pre-Batch-7 snapshot.
# tools/reproduce.py supersedes this script for outside review.
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
json = __import__("json")
hashlib = __import__("hashlib")
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
measures = tables.measures
PROJECT = pathlib.Path(__file__).resolve().parents[1]
ACCEPTED = {'TABLES/per_actor.md': 'a43741f2ebaaa1627c74a9077ca750247c6b81eb4983b0bf41208e0c192bda3b', 'TABLES/per_population.md': '26e68f49197c80c9934055061a07a9b986afd496815b99c88b7211a187035913', 'TABLES/dcnh_two_ways.md': '1934a9d4ab9dcfdc382ff74d7c7a6e1491424c989097da1a98324c0037bb63ab', 'REPORT.md': '530f1bd6c16e800362f130d1020ef2ed7f50d779f2ea1524a6323b6c1e4bf55a', 'generate/histories.py': 'bcd7c9d43d19787ff5f3bf6c8df96b66d07f1fbfa0940bbad7cc9240315f618f', 'HISTORIES.json': 'b32c47a6f73e2517b3bce5db35db4e249e40352c17a94548858ee15aa4353d7d', 'conditioning_v2/retention.py': '8960570d5b14eeabdbaad59a4db4866b93cd2dd7d33841db4867b73dd675be1c'}
HEADERS = ['| Model | Fixture seeds | Actors per history | Transactions per history |\n| --- | --- | --- | --- |\n', '| Actor | TIM | All-use count | Received-and-kept count | DCNH comparison |\n| --- | --- | --- | --- | --- |\n', '| History | Final coverage | Through episode 0 | Through episode 1 |\n| --- | --- | --- | --- |\n', '| Source | Receiver | Relation | Forward uses | Reverse uses |\n| --- | --- | --- | --- | --- |\n', '| Source | Receiver | Relation | Pair-subset uses within triad | Triad benefit-family uses | Standalone pair uses |\n| --- | --- | --- | --- | --- | --- |\n']
REPORT_TEMPLATE = "# Function Conditioning Ledger — final report\n\n## 1. What was generated\n\nThe accepted `HISTORIES.json` contains matched fixture seeds under the following\nresource models. Each history contains Alice (`workshop:alice`, IEE), Bob\n(`workshop:bob`, SLI), and Eve (`workshop:eve`, LIE).\n\n@@TABLE_0@@\n\nSources: [accepted input rows](TABLES/per_population.md#accepted-inputs), keyed\nby model and seed; [DCNH rows](TABLES/dcnh_two_ways.md), keyed by history and actor,\nfor actor identities and TIMs. These are generated histories, not historical archives.\n\n## 2. Cross-actor delivery\n\n**No cross-actor delivery observed in generated histories.** Every history's\n`Received uses` cell is **@@RECEIVED@@**. The use-profile and trace rows identify the\nobserved sources as `world`, which does not count as actor-supplied delivery.\nThis retains the accepted provenance finding.\n\nSources: [population summary](TABLES/per_population.md#population-summary),\nevery history row; [use profile](TABLES/per_actor.md#use-profile) and\n[use trace](TABLES/per_actor.md#use-trace).\n\n## 3. DCNH all-use versus received-and-kept\n\nThe comparison is **diverge** for each actor in every generated history.\nThe following rows apply under every model and seed listed above.\n\n@@TABLE_1@@\n\nSource: [DCNH two ways](TABLES/dcnh_two_ways.md), each history's paired\n`all uses` and `received and kept` rows for the named actor, including their\n`Uses` and `Comparison` cells. The source table supplies the corresponding\naxis loads, tilts, and greatest-load cells.\n\n## 4. Coverage per population and episode\n\n@@TABLE_2@@\n\nThe denominator includes every committed actor's weak seats, including any\ninactive actor. Episode coverage is cumulative through each actor-local\nepisode index, pooled across actors; it is not a wall-clock snapshot.\n\nSources: [population summary](TABLES/per_population.md#population-summary),\nmatching history's `Coverage` cell; [coverage by episode index](TABLES/per_population.md#coverage-by-episode-index),\nmatching history and `Through episode` row.\n\n## 5. Sterile ordered pairs\n\nThese ordered pairs are sterile in every generated history. Forward means\nsource to receiver; sterility requires no received uses in either direction.\n\n@@TABLE_3@@\n\nSource: [ordered pairs](TABLES/per_population.md#ordered-pairs), matching\nsource/receiver rows in every history. Their `Sterile` cells are `True`;\nrelation names retain the pinned kernel's direction convention.\n\n## 6. Benefit pair versus triad\n\nThe following values apply in every generated history.\n\n@@TABLE_4@@\n\nSource: [benefit pairs within the triad versus triad total](TABLES/per_population.md#benefit-pairs-within-the-triad-versus-triad-total),\nmatching source/receiver rows in each history. The triad total includes both\nbenefit directions. Pair-subset counts describe the same triad; they are not\nstandalone pair experiments. A standalone pair-versus-triad comparison is\ntherefore unavailable, not an observed equality.\n\n## 7. Limits\n\nGenerated histories only; no historical archive was used. Test-only positive\ndelivery examples are not findings from these histories. No feedback, energy\nregeneration, practice pricing, demand formation, or executor change was added.\nThe read repository remains unchanged. Nothing about the theory is closed.\n\nThe [actor-index rows](TABLES/per_actor.md#actor-indices) report conditioning\nand hold as **@@EMPTY@@** throughout. The [population-summary rows](TABLES/per_population.md#population-summary)\nreport supplier concentration as **@@EMPTY@@**. Undefined ratios are distinct\nfrom measured zero delivery or coverage.\n\nThe reported conditioning index applies Amendment A1's literal actor-source\nrestriction to both numerator and denominator, making it degenerate whenever\ndefined. This report preserves the explicitly labeled calculation; it does\nnot resolve the source-scope question or silently restore the older denominator.\nThe missing standalone pair experiment remains unavailable. No generator\nreplacement or additional experiment is authorized by these findings.\n"


def render_report(histories):
    """Regenerate the accepted report's numeric rows from restored histories.

    Prose is the accepted Batch 5 wording; every observational prose claim is
    also asserted below, rather than reading REPORT.md as an input template.
    """
    first = histories[0]["observation"]
    rows = [[] for _ in HEADERS]
    for model in dict.fromkeys(h["manifest"]["model"] for h in histories):
        items = [h for h in histories if h["manifest"]["model"] == model]
        counts = {(len(h["observation"]["profiles"]), h["manifest"]["transactions"]) for h in items}
        assert len(counts) == 1
        actors, transactions = counts.pop()
        rows[0].append((model, ", ".join(str(h["manifest"]["seeds"]["fixture"]) for h in items), actors, transactions))
    for actor, data in first["actors"].items():
        rows[1].append((measures.actor_name(actor), data["tim"], len(data["all_ids"]), len(data["held"]),
                        "agree" if data["all_dcnh"] == data["received_kept_dcnh"] else "diverge"))
    for h in histories:
        obs = h["observation"]
        assert obs["profiles"] == first["profiles"]
        assert all(r["source"] == "world" for r in obs["records"])
        assert not obs["received"] and obs["concentration"] == (0, 0)
        assert obs["pairs"] == first["pairs"] and obs["benefit_ids"] == first["benefit_ids"]
        assert set(obs["episode_coverage"]) == {0, 1}
        for a, r in obs["actors"].items():
            assert r["conditioning"] == r["hold"] == (0, 0)
            assert r["all_dcnh"] == first["actors"][a]["all_dcnh"]
            assert r["received_kept_dcnh"] == first["actors"][a]["received_kept_dcnh"]
            assert r["all_dcnh"] != r["received_kept_dcnh"]
        def fraction(cov):
            n, d = cov["ratio"]
            return str(n) + "/" + str(d)
        rows[2].append((h["manifest"]["name"], fraction(obs["coverage"]),
                        *(fraction(obs["episode_coverage"][e]) for e in (0, 1))))
    for pair in first["pairs"]:
        assert pair["sterile"]
        common = (measures.actor_name(pair["sender"]), measures.actor_name(pair["receiver"]), pair["relation"])
        rows[3].append((*common, len(pair["forward"]), len(pair["reverse"])))
        if pair["relation"] in measures.BENEFIT:
            assert first["standalone_pair"] is None
            rows[4].append((*common, len(pair["forward"]), len(first["benefit_ids"]), "N/A: not generated"))
    text = REPORT_TEMPLATE
    for i, body in enumerate(rows):
        block = HEADERS[i] + "".join("| " + " | ".join(map(str, row)) + " |\n" for row in body)
        text = text.replace("@@TABLE_" + str(i) + "@@\n", block)
    return text.replace("@@RECEIVED@@", str(len(first["received"]))).replace("@@EMPTY@@", tables.ratio(first["concentration"]))


def verify(histories=None):
    for name, digest in ACCEPTED.items():
        assert hashlib.sha256((PROJECT / name).read_bytes()).hexdigest() == digest, name
    histories = tables.load_histories() if histories is None else histories
    regenerated = {"TABLES/" + name: value for name, value in tables.render(histories).items()}
    regenerated["REPORT.md"] = render_report(histories)
    for name, text in regenerated.items():
        raw = text.encode()
        assert hashlib.sha256(raw).hexdigest() == ACCEPTED[name], name
        assert raw == (PROJECT / name).read_bytes(), name
        print("BYTE-IDENTICAL: " + name + " " + ACCEPTED[name], flush=True)
    for h in histories:
        obs = h["observation"]
        profiles, counts = measures.conditioning.completed_use(h["transactions"])
        observed = {a: dict.fromkeys(measures.conditioning.ELEMENTS, 0) for a in profiles}
        for row in obs["records"]:
            assert row["source"] in ("self", "world")
            observed[row["actor"]][row["element"]] += 1
        assert observed == counts
        assert {measures.actor_name(a): sum(c.values()) for a, c in counts.items()} == h["manifest"]["completed_paid_uses"]
    print("PASS: 8 accepted histories retain self/world-only sources and exact I5 counts.", flush=True)
    print("PASS: accepted generator, manifest, retention, tables and report bytes unchanged.", flush=True)
    return histories


if __name__ == "__main__":
    verify()
