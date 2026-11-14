#!/usr/bin/env python3
r"""
validate_rtm.py — sanity-check a Requirements Traceability Matrix (RTM) CSV.

What it checks
--------------
1. DUPLICATE_REQ_ID     — the same ReqID appears more than once.
2. MISSING_COVERAGE     — a requirement has a source but no linked test cases.
3. ORPHANED_REQ         — a requirement has neither a source nor any test case
                          (traceability is broken at both ends).
4. MALFORMED_TEST_ID    — a linked test case ID doesn't match the expected
                          pattern (default: TC-123, separated by ';' or ',').
5. MISSING_FIELD        — a required column is empty for that row.
6. BAD_PRIORITY         — priority isn't one of the allowed values.

Expected CSV columns
--------------------
    ReqID, Requirement, Source, Owner, Priority, TestCaseIDs, Status

    * TestCaseIDs may list several IDs separated by ';' or ','.
    * Lines starting with '#' are treated as comments.

Usage
-----
    python validate_rtm.py path/to/rtm.csv
    python validate_rtm.py path/to/rtm.csv --pattern 'TC-\d{3}' --quiet

Exit codes: 0 = clean, 1 = findings reported, 2 = file/column problem.
Stdlib only — no dependencies.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

REQUIRED_COLUMNS = ["ReqID", "Requirement", "Source", "Owner", "Priority", "TestCaseIDs", "Status"]
DEFAULT_TEST_ID_PATTERN = r"TC-\d{3}"
ALLOWED_PRIORITIES = {"must", "should", "could", "won't"}
SEPARATOR_RE = re.compile(r"[;,]")


class RTMError(Exception):
    """Raised when the CSV can't be parsed at all (missing columns, no header)."""


@dataclass
class Finding:
    code: str
    req_id: str
    message: str

    def __str__(self) -> str:
        return f"[{self.code}] {self.req_id or '(file)'}: {self.message}"


def load_rtm(path: str | Path) -> list[dict[str, str]]:
    """Read the RTM CSV into a list of row dicts (comments and blank lines skipped)."""
    path = Path(path)
    if not path.exists():
        raise RTMError(f"file not found: {path}")

    with path.open(newline="", encoding="utf-8-sig") as fh:
        lines = [ln for ln in fh if ln.strip() and not ln.lstrip().startswith("#")]
    if not lines:
        raise RTMError(f"{path} has no data rows")

    reader = csv.DictReader(lines)
    header = reader.fieldnames or []
    missing = [c for c in REQUIRED_COLUMNS if c not in header]
    if missing:
        raise RTMError(f"{path} is missing required column(s): {', '.join(missing)}")

    rows = []
    for i, row in enumerate(reader, start=2):
        rows.append({k: (v or "").strip() for k, v in row.items() if k is not None} | {"_line": str(i)})
    return rows


def _split_test_ids(raw: str) -> list[str]:
    return [t.strip() for t in SEPARATOR_RE.split(raw) if t.strip()]


def validate_rtm(rows: list[dict[str, str]], test_id_pattern: str = DEFAULT_TEST_ID_PATTERN) -> list[Finding]:
    """Return a list of Findings. Empty list = the RTM is clean."""
    findings: list[Finding] = []
    id_re = re.compile(f"^{test_id_pattern}$")

    # 1. duplicates + per-row checks
    counts = Counter(r["ReqID"] for r in rows if r["ReqID"])
    for req_id, n in counts.items():
        if n > 1:
            findings.append(Finding("DUPLICATE_REQ_ID", req_id, f"appears {n} times; ReqID must be unique"))

    for row in rows:
        req_id = row.get("ReqID", "")
        line = row.get("_line", "?")

        for col in ("ReqID", "Requirement"):
            if not row.get(col):
                findings.append(Finding("MISSING_FIELD", req_id or f"(line {line})", f"required column '{col}' is empty"))

        if not req_id:
            continue

        source = row.get("Source", "")
        test_ids = _split_test_ids(row.get("TestCaseIDs", ""))

        # 2/3. traceability
        if not test_ids:
            if source:
                findings.append(Finding("MISSING_COVERAGE", req_id, "no linked test case — this requirement is untested"))
            else:
                findings.append(Finding("ORPHANED_REQ", req_id, "no source and no test case — lost at both ends of the trace"))

        # 4. test ID format
        for tid in test_ids:
            if not id_re.match(tid):
                findings.append(Finding("MALFORMED_TEST_ID", req_id, f"'{tid}' doesn't match pattern {test_id_pattern}"))

        # 6. priority vocabulary
        priority = row.get("Priority", "").lower()
        if priority and priority not in ALLOWED_PRIORITIES:
            allowed = ", ".join(sorted(ALLOWED_PRIORITIES))
            findings.append(Finding("BAD_PRIORITY", req_id, f"'{row.get('Priority')}' — expected one of: {allowed}"))

    return findings


def coverage_stats(rows: list[dict[str, str]]) -> dict[str, int | float]:
    """Basic coverage numbers for the summary line."""
    with_source = [r for r in rows if r.get("Source")]
    covered = [r for r in rows if _split_test_ids(r.get("TestCaseIDs", ""))]
    total = len(rows)
    return {
        "requirements": total,
        "covered": len(covered),
        "uncovered": total - len(covered),
        "coverage_pct": round(100 * len(covered) / total, 1) if total else 0.0,
        "with_source": len(with_source),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Requirements Traceability Matrix CSV.")
    parser.add_argument("csv_path", help="path to the RTM CSV file")
    parser.add_argument("--pattern", default=DEFAULT_TEST_ID_PATTERN, help="regex a test case ID must match (default: %(default)s)")
    parser.add_argument("--quiet", action="store_true", help="only print the summary line")
    args = parser.parse_args(argv)

    try:
        rows = load_rtm(args.csv_path)
    except RTMError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    findings = validate_rtm(rows, test_id_pattern=args.pattern)
    stats = coverage_stats(rows)

    if findings and not args.quiet:
        for f in findings:
            print(f)
        print()

    print(
        f"{stats['requirements']} requirement(s) | "
        f"{stats['covered']} covered | "
        f"{stats['uncovered']} uncovered | "
        f"coverage {stats['coverage_pct']}% | "
        f"{len(findings)} finding(s)"
    )
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
