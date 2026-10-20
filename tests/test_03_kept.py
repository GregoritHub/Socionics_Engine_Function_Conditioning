import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
json = __import__("json")
hashlib = __import__("hashlib")
replace = __import__("dataclasses").replace
Population = __import__("hle_unified.population", fromlist=["Population"]).Population
energy = __import__("hle_unified.energy_audit", fromlist=["blocks", "data", "debit"])
material = __import__("hle_unified.material", fromlist=["attributes"])
model_a = __import__("hle.model_a", fromlist=["position_of"])
v2 = __import__("conditioning_v2.audit", fromlist=["uses"])
retention = __import__("conditioning_v2.retention", fromlist=["uses"])

PROJECT = pathlib.Path(__file__).resolve().parents[1]


def key(row):
    return row["actor"], row["seat"], row["element"]


def completed_events(transactions):
    """Locate paid blocks using only declared progress and canonical blocks."""
    heads, events = {}, []
    for index, tx in enumerate(transactions):
        for version in tx.versions:
            d = energy.data(version)
            if d.get("record_type") == "operation":
                old = heads.get(version.ref.identity)
                previous = {} if old is None else energy.data(old)
                for _, end, _, element in energy.blocks(d):
                    if element is not None and previous.get("completed", 0) < end <= d["completed"]:
                        events.append((index, d["actor"],
                                       model_a.position_of(d["tim"], element), element, end))
            heads[version.ref.identity] = version
    return events


def unique_seat_prefix(transactions):
    """Test-only paid prefix, cut at the second distinct seat's first use.

    Keep the accepted initialization and first paid transaction's revisions;
    reduce that transaction's completion and its exact wallet debit together.
    This is an in-memory witness, never a replacement history/checkpoint.
    """
    events = completed_events(transactions)
    first, second = events[:2]
    if first[0] != second[0] or first[1:4] == second[1:4]:
        raise AssertionError("expected two distinct seats in the first paid transaction")
    index, _, _, _, boundary = second
    prefix = list(transactions[:index])
    heads = {v.ref.identity: v for tx in prefix for v in tx.versions}
    tx = transactions[index]
    operation = next(v for v in tx.versions
                     if energy.data(v).get("record_type") == "operation")
    previous = energy.data(heads[operation.ref.identity])
    d = energy.data(operation)
    d.update(completed=boundary, spent=boundary)
    elapsed = boundary - previous.get("completed", 0)
    debit = energy.debit(d, previous) if energy.resource_model(transactions) == "grade-v1" else elapsed
    versions = []
    for version in tx.versions:
        attrs = energy.data(version)
        if version == operation:
            version = replace(version, attributes=material.attributes(d))
        elif attrs.get("record_type") == "wallet":
            old_wallet = energy.data(heads[version.ref.identity])
            attrs.update(time=old_wallet["time"] - elapsed,
                         energy=old_wallet["energy"] - debit)
            version = replace(version, attributes=material.attributes(attrs))
        versions.append(version)
    prefix.append(replace(tx, versions=tuple(versions)))
    return tuple(prefix)


class KeptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.histories = []
        for row in json.loads((PROJECT / "HISTORIES.json").read_text()):
            raw = (PROJECT / "OUT" / (row["name"] + ".checkpoint")).read_bytes()
            if hashlib.sha256(raw).hexdigest() != row["checkpoint_sha256"]:
                raise AssertionError("checkpoint differs from accepted Batch 1")
            population = Population.restore(raw.decode())
            if population.checkpoint().encode() != raw:
                raise AssertionError("checkpoint restore changed bytes")
            transactions = population.engine.world.journal()
            if len(transactions) != row["transactions"]:
                raise AssertionError("transaction count differs from accepted Batch 1")
            cls.histories.append((row["name"], transactions))

    def assert_prefix_monotone(self, prefix_transactions, whole):
        prefix = retention.uses(prefix_transactions)
        self.assertLessEqual(len(prefix), len(whole))
        # Compare each occurrence by its preserved sequence position, including
        # all Batch 2 fields. Equal-valued repeat records are still distinct uses.
        for index, before in enumerate(prefix):
            after = whole[index]
            self.assertEqual({k: v for k, v in before.items() if k != "kept"},
                             {k: v for k, v in after.items() if k != "kept"})
            if before["kept"]:
                self.assertIs(after["kept"], True)
        return prefix

    def test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history(self):
        for name, transactions in self.histories:
            with self.subTest(history=name):
                whole = retention.uses(transactions)
                self.assert_prefix_monotone(transactions[:len(transactions) // 2], whole)
                # The generated first halves contain setup only. Also exercise
                # already-True retention and an actual False -> True transition.
                first_paid_index = completed_events(transactions)[0][0]
                paid_prefix = self.assert_prefix_monotone(transactions[:first_paid_index + 1], whole)
                self.assertTrue(any(row["kept"] for row in paid_prefix))
                self.assertTrue(any(not row["kept"] and whole[i]["kept"]
                                    for i, row in enumerate(paid_prefix)))

    def test_02_repeated_seats_are_true_except_last_and_preserve_batch2(self):
        for name, transactions in self.histories:
            with self.subTest(history=name):
                original = v2.uses(transactions)
                rows = retention.uses(transactions)
                self.assertEqual([{k: v for k, v in row.items() if k != "kept"}
                                  for row in rows], original)
                groups = {}
                for row in rows:
                    self.assertIs(type(row["kept"]), bool)
                    groups.setdefault(key(row), []).append(row["kept"])
                self.assertTrue(any(len(values) > 1 for values in groups.values()))
                for values in groups.values():
                    self.assertEqual(values, [True] * (len(values) - 1) + [False])
                # Independent forward existential reading of the fixed rule.
                for i, row in enumerate(rows):
                    self.assertEqual(row["kept"], any(key(later) == key(row)
                                                     for later in original[i + 1:]))

    def test_03_unique_seats_are_false_and_missing_payment_is_rejected(self):
        for name, transactions in self.histories:
            with self.subTest(history=name):
                prefix = unique_seat_prefix(transactions)
                rows = retention.uses(prefix)
                self.assertEqual(len(rows), 2)
                self.assertEqual(len({key(row) for row in rows}), len(rows))
                self.assertTrue(all(row["kept"] is False for row in rows))
                last = prefix[-1]
                unpaid = replace(last, versions=tuple(v for v in last.versions
                                 if energy.data(v).get("record_type") != "wallet"))
                with self.assertRaisesRegex(ValueError, "completed work lacks exact raw wallet evidence"):
                    retention.uses((*prefix[:-1], unpaid))

    def test_04_forged_duplicate_transaction_is_rejected(self):
        for name, transactions in self.histories:
            with self.subTest(history=name):
                index = completed_events(transactions)[0][0]
                forged = (*transactions[:index + 1], transactions[index], *transactions[index + 1:])
                with self.assertRaisesRegex(retention.DuplicateTransactionError,
                                            "duplicate committed transaction revision"):
                    retention.uses(forged)

    def test_05_repeat_moved_before_earlier_use_is_rejected(self):
        for name, transactions in self.histories:
            with self.subTest(history=name):
                events = completed_events(transactions)
                earlier, repeat = next((a, b) for a in events for b in events
                                       if a[0] < b[0] and a[1:4] == b[1:4])
                self.assertEqual(earlier[1:4], repeat[1:4])
                forged = list(transactions)
                moved = forged.pop(repeat[0])
                forged.insert(earlier[0], moved)
                self.assertEqual(len(forged), len(transactions))
                with self.assertRaisesRegex(retention.TransactionOrderError,
                                            "transaction order differs from committed journal"):
                    retention.uses(forged)

    def test_06_declared_moment_fields_and_forged_moments(self):
        for name, transactions in self.histories:
            with self.subTest(history=name):
                for index, tx in enumerate(transactions):
                    self.assertEqual((tx.at.tick, tx.at.order), (index, 0))
                for moment in (replace(transactions[-1].at, tick=len(transactions)),
                               replace(transactions[-1].at, order=1)):
                    forged = (*transactions[:-1], replace(transactions[-1], at=moment))
                    with self.assertRaises(retention.TransactionOrderError):
                        retention.uses(forged)


if __name__ == "__main__":
    unittest.main()
