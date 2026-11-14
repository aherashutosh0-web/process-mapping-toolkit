# UAT Test Plan Template

*The plan for proving the solution works **for the business** before it goes live. UAT isn't a second round of system testing — it's the business confirming the thing fits how people actually work. Write it early; approve it before build finishes.*

> **How to use this file:** fill sections 1–9 while development is still running, get business sign-off on the plan *before* UAT starts (approving the plan after seeing the results is how "we'll just check it works" becomes three weeks of chaos), and keep the daily results in section 11 as you go.

---

## 1. Overview

| | |
|---|---|
| **Project / release** | |
| **Plan version / date** | *(and the FRD/BRD versions being tested)* |
| **UAT window** | *(dates, including buffer)* |
| **Author / UAT lead** | |
| **Business testers** | *(names + the real-world role they play)* |
| **Approvals** | *(business owner signs that the plan is sufficient — not that the results are good)* |

## 2. Objective & entry criteria

**Objective:** *one paragraph. Example: "Confirm the new order fulfilment process supports daily warehouse operations at target volumes, including exception paths, before cut-over on 14 June."*

**Entry criteria** (all must be true before UAT day 1 — no exceptions "just for now"):

- [ ] System testing complete; no open severity 1–2 defects
- [ ] UAT environment refreshed with representative data
- [ ] This plan signed off by the business owner
- [ ] Test cases reviewed and mapped in the [RTM](rtm-template.md) (zero `Not covered` for Must requirements)
- [ ] Business testers trained on the UAT process and defect logging

## 3. Exit criteria

- [ ] 100% of Must test cases executed; ≥ 95% passed (remaining failures have agreed workarounds)
- [ ] Should test cases ≥ 90% executed
- [ ] No open severity 1 defects; severity 2 defects have business-accepted plans
- [ ] Sign-off obtained (section 12)
- [ ] Known-issues list published to all users before go-live

## 4. Scope

**In scope:**
**Out of scope:** *(interfaces tested in SIT, performance testing, etc. — name them so nobody assumes coverage)*

## 5. Test approach

- **Who tests:** real users of the process (warehouse staff, support agents) — not the project team proxying for them.
- **How:** scripted test cases (section 10) plus 1–2 days of free-form scenario testing on realistic daily work.
- **Defect process:** where to log (tool + project), severity definitions (below), who triages, daily defect huddle at *(time)*.
- **Test data:** who prepares it, refresh policy, and the golden rule — *UAT data must look like production data*, including the messy addresses and the 200-line orders.

**Severity definitions:**

| Severity | Meaning | Response |
|---|---|---|
| 1 — Critical | Process cannot complete; no workaround | Stop; escalate same day |
| 2 — High | Major function impaired; poor workaround | Fix before go-live or accept explicitly |
| 3 — Medium | Minor function impaired; workaround exists | Fix if time allows |
| 4 — Low | Cosmetic / wording | Park for post-go-live |

## 6. Environment & data

| | |
|---|---|
| **Environment / URL** | |
| **Data refresh** | *(when, from what source, masked?)* |
| **Test accounts** | *(roles set up: buyer, ops manager, support agent…)* |
| **Known environment limits** | *(email won't send to real addresses, carrier sandbox is slow…)* |

## 7. Roles & responsibilities

| Role | Person | Responsibility |
|---|---|---|
| UAT lead | | schedule, daily report, escalation |
| Business tester | | execute cases, log defects with evidence |
| Defect triager | | severity decision, fix/defer calls |
| BA (you) | | answer requirement questions, update RTM/CRs |
| Tech support | | environment, data fixes, investigation |

## 8. Schedule

| Day | Focus | Who |
|---|---|---|
| Day 0 | smoke check + tester walkthrough | UAT lead + all |
| Days 1–3 | scripted cases (Must) | business testers |
| Day 4 | exception paths + free-form scenarios | business testers |
| Day 5 | retest of fixes + Should cases | testers + BA |
| Day 6 | buffer / regression spot-checks | all |

## 9. Risks to UAT

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Testers pulled back to day jobs | High | High | agreed % of time with line managers; UAT calendar booked early |
| Environment instability | Medium | High | dedicated env; daily health check |
| Test data lacks edge cases | Medium | Medium | seed the ugly cases on day 0 |

## 10. Test cases

### 10.1 Test case fields

| Field | Meaning |
|---|---|
| **TC ID** | `TC-nnn` — same IDs as in the RTM |
| **Traces to** | ReqID(s) satisfied |
| **Title / objective** | what this proves |
| **Preconditions** | state before execution |
| **Steps** | numbered, unambiguous |
| **Expected result** | observable, per step |
| **Actual result** | filled during execution |
| **Status** | Pass / Fail / Blocked / Not run |
| **Tester / date** | |

### 10.2 Sample test case (fully worked)

| | |
|---|---|
| **TC ID** | TC-001 |
| **Traces to** | BA-001 (order requires available stock) |
| **Title** | Reject order placement when stock is unavailable |
| **Preconditions** | Product P-1042 has on-hand stock = 0; customer "M. Okafor" is logged in with P-1042 in basket (qty 1) |
| **Priority** | Must |

| # | Steps | Expected result |
|---|---|---|
| 1 | Open basket, select P-1042, click "Checkout" | Stock check runs; "Continue to payment" is **disabled** |
| 2 | Read the inline message | Message: "P-1042 is out of stock — remove it or use 'Notify me'" *(exact wording per FR-008)* |
| 3 | Click "Notify me" | Notification preference saved; confirmation shown; basket unchanged |
| 4 | Reduce quantity to 0 and remove item | Item removed; checkout returns to enabled state for remaining lines |

| | |
|---|---|
| **Actual result** | *(filled in during UAT)* |
| **Status** | *(Pass / Fail)* |
| **Tester / date** | |

*(Add your real cases in this table format — or keep them as CSV rows in the RTM tooling and link them here.)*

## 11. Defect log

| Defect ID | TC ID | Severity | Description | Raised by / date | Status | Fix version / CR |
|---|---|---|---|---|---|---|

## 12. Results & sign-off

| Measure | Result |
|---|---|
| Test cases planned / executed / passed / failed | |
| Coverage of Must requirements | |
| Open defects at exit (by severity) | |
| Defects deferred with acceptance | |

| Role | Name | Decision | Date | Comment |
|---|---|---|---|---|
| Business owner | | ☐ Accept ☐ Accept with conditions ☐ Reject | | |
| UAT lead | | | | |
| Project manager | | | | |

---

### Tips from experience

- **Book testers' time with their line managers in writing.** UAT fails from absence far more often than from bugs.
- **Severity is a business judgement, triage is a joint one.** The BA owns "what does the requirement say"; the business owner owns "can we live with this on Monday".
- **Free-form day is where you find the real problems** — give testers a realistic workload ("process today's 40 orders") instead of only scripts.
- **Log a defect against the requirement, not just the test case**, and update the RTM status the same day. That keeps the coverage report honest all the way to sign-off.
- **Keep the known-issues list.** Go-live confidence comes from *honest* known issues, not from a defect count of zero.
