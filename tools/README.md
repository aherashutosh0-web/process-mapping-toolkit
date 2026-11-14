# tools/ — the one bit of automation

`validate_rtm.py` is a small, dependency-free script that sanity-checks a
Requirements Traceability Matrix before you paste it into a steering pack and
get asked why half the requirements have no test cases.

It's deliberately boring: stdlib only, one file, no config. If you need
anything fancier you've probably outgrown a spreadsheet anyway.

## What it checks

| Code | Meaning |
|---|---|
| `DUPLICATE_REQ_ID` | Same ReqID twice — traceability will double-count it |
| `MISSING_COVERAGE` | Requirement has a source but **no linked test case** |
| `ORPHANED_REQ` | No source *and* no test case — lost at both ends of the trace |
| `MALFORMED_TEST_ID` | Linked test ID doesn't match `TC-\d{3}` (pattern is configurable) |
| `MISSING_FIELD` | A required column is empty for that row |
| `BAD_PRIORITY` | Priority isn't one of `must / should / could / won't` |

## Usage

```bash
# from the repo root
python tools/validate_rtm.py tools/sample_data/rtm_sample.csv

# custom test-ID pattern, minimal output
python tools/validate_rtm.py my_rtm.csv --pattern 'TC_\d{4}' --quiet
```

Exit codes: `0` clean · `1` findings reported · `2` file/column problem — so it
drops straight into a pre-commit hook or CI step if you want it there.

## Sample output

Against `sample_data/rtm_sample.csv` (which has a few problems seeded on purpose):

```
[MISSING_COVERAGE] BA-005: no linked test case — this requirement is untested
[MISSING_FIELD] BA-011: required column 'Requirement' is empty
[ORPHANED_REQ] BA-011: no source and no test case — lost at both ends of the trace
[MALFORMED_TEST_ID] BA-013: 'TC-17A' doesn't match pattern TC-\d{3}

14 requirement(s) | 12 covered | 2 uncovered | coverage 85.7% | 4 finding(s)
```

## Expected CSV shape

```csv
ReqID,Requirement,Source,Owner,Priority,TestCaseIDs,Status
BA-001,The system shall ...,Workshop 2026-03-12,A. Patel,must,TC-001;TC-002,Approved
```

- `TestCaseIDs` takes several IDs separated by `;` or `,`
- Lines starting with `#` are comments (handy for notes in the CSV)
- `Priority` must be one of `must / should / could / won't` (MoSCoW)

## Tests

```bash
python -m pytest        # from the repo root
```

The tests cover each check, the sample file's known findings, and the CLI exit
codes. They run in well under a second.
