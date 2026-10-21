import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
audit = __import__("conditioning_v2.audit", fromlist=["uses"])


class DuplicateTransactionError(ValueError):
    """A committed revision was replayed instead of new paid work occurring."""


class TransactionOrderError(ValueError):
    """The input is not a native committed journal or a prefix of one."""


def _validate_history(transactions):
    # Detect replay before checking order, so duplicates have a named error.
    seen = set()
    for tx in transactions:
        for version in tx.versions:
            if version.ref in seen:
                raise DuplicateTransactionError("duplicate committed transaction revision")
            seen.add(version.ref)
    for index, tx in enumerate(transactions):
        if tx.at.tick != index or tx.at.order != 0:
            raise TransactionOrderError("transaction order differs from committed journal")


def uses(transactions, reading="wide"):
    """Return use dictionaries with kept from a journal/prefix and reading.

    Enforce I4 history-growth monotonicity, preserving I1-I3 and I5 from audit
    (Batch 3, Amendment A2; reading selection from Batch 7 section A2).
    Accept a complete native history or its prefix, in committed order. Within
    each transaction the Batch 2 audit preserves canonical paid-block order.
    A later block at the same seat can retain an earlier block; the last use is
    always False. Appending transactions can only turn existing False to True.
    No input records, transactions, or engine state are modified.
    """
    transactions = tuple(transactions)
    _validate_history(transactions)
    records = audit.uses(transactions, reading)
    later = set()
    result = []
    for record in reversed(records):
        key = (record["actor"], record["seat"], record["element"])
        result.append(dict(record, kept=key in later))
        later.add(key)
    result.reverse()
    return result
