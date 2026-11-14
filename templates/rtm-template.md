# Requirements Traceability Matrix (RTM) Template

*The spreadsheet that answers "if we change/drop/break this requirement, what else is affected?" — and, at release time, "is everything actually tested?" A quiet RTM is the difference between a confident go-live and a hopeful one.*

> **How to use this file:** maintain the RTM as a CSV during the project (the format `tools/validate_rtm.py` checks), and paste it into this Markdown view for reviews. One row per requirement. Update it *when the requirement changes*, not at the end of the project — an RTM updated in a panic before go-live is an audit finding waiting to be raised.

---

## 1. Matrix header

| | |
|---|---|
| **Project / release** | |
| **RTM owner** | *(usually the BA — the name in this row is the person who gets asked about coverage)* |
| **Source documents** | *(BRD v, FRD v — pin the versions)* |
| **Last updated** | *(date + who)* |
| **Update cadence** | *(e.g. "sprint review + after every CR")* |

## 2. The matrix

One row per requirement. Direction of traceability: **up** to where the requirement came from, **down** to where it's proved.

| ReqID | Requirement (short title) | Source (BR / gap / CR / policy) | Upstream ID | Design / build ref | TestCaseIDs | Test status | Priority | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| BA-001 | Order validates stock at placement | Workshop 2026-03-12 | BR-001 | OrderSvc.validate() | TC-001; TC-002 | Passed | Must | A. Patel | Approved |
| BA-005 | Partial shipments for 10+ line orders | Interview — CS lead | BR-006 | *tbd* | *(none yet)* | Not covered | Could | R. Khan | In review |

**Column notes:**

- **Source / Upstream ID** — where the requirement came from *and* its ID there (BR-xxx, GAP-xxx, CR-2026-xxxx, policy clause). Two columns because "Workshop" is a source but `BR-001` is a pointer.
- **TestCaseIDs** — several allowed, separated by `;`. Keep the `TC-nnn` convention so `validate_rtm.py` can check the file for you.
- **Test status** — one of: `Not covered · Not run · Passed · Failed · Blocked · N/A`.
- **Status** — the requirement's own lifecycle: `Draft · In review · Approved · Deferred · Dropped`.

## 3. Coverage summary

| Measure | Count |
|---|---|
| Total requirements | |
| Covered by ≥1 passing test | |
| Covered but tests not run / failing | |
| **Not covered** | |
| Coverage % | |

*Run `python tools/validate_rtm.py your_matrix.csv` to get these numbers and catch the silent gaps.*

## 4. Reverse trace checks (do these at every milestone)

The forward direction (requirement → test) is the easy one. The reverse catches the different problems:

| Check | Question it answers | Done? |
|---|---|---|
| Test → requirement | Does every test case trace to a requirement? *(orphan tests = wasted effort or missing requirements)* | ☐ |
| Requirement → business need | Does every requirement trace up to a BR/gap/policy? *(orphan requirements are scope creep with a straight face)* | ☐ |
| Change impact | When a CR lands, which test cases and design elements does it touch? | ☐ |
| Defect → requirement | Does every open defect map to a requirement whose status is now suspect? | ☐ |

## 5. Defects affecting release readiness

| Defect ID | Related ReqID | Severity | Status | Blocking release? |
|---|---|---|---|---|

## 6. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|

---

### Tips from experience

- **The "Not covered" count is the only number your steering group needs.** Everything else is detail.
- **Trace to test *cases*, not to test *cycles*.** "Tested in SIT" isn't traceability.
- **Dropped requirements stay in the matrix**, marked `Dropped` with the CR number that killed them. Deleting rows breaks the audit trail and your credibility.
- **Keep the CSV the master.** This Markdown view is for humans at review time; the CSV is what the tool checks and what survives copy-paste into Excel.
- **Five minutes at sprint review beats five hours before go-live.** Update cadence is a habit, not a task.
