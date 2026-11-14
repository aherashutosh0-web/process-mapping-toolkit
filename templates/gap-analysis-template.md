# Gap Analysis Template

*For turning "here's how it works now, here's how we want it to work" into a prioritised list of changes someone can fund. Use it once the [AS-IS → TO-BE map](as-is-to-be-process-template.md) is validated.*

> **How to use this file:** one row per gap. A gap is a specific, named difference between current and future state — not a complaint, not a solution. If you can't describe the gap without naming a product or vendor, you've skipped ahead to solutioning; go back.

---

## 1. Header

| | |
|---|---|
| **Process / domain** | |
| **Linked process map** | *(link to the AS-IS → TO-BE doc)* |
| **Date** | |
| **Author** | |
| **Reviewers** | *(process owner + at least one doer)* |

## 2. Method in one paragraph

*So the next person knows how this list was built. Example: "Gaps were identified by comparing the validated AS-IS map against the TO-BE design, plus every pain point raised in the workshop. Each gap was reviewed with the process owner on 12 May."*

## 3. Gap register

One row per gap. IDs are stable forever — reference them in the BRD, the change requests, everything.

| Gap ID | Current state (AS-IS) | Future state (TO-BE) | Gap (what's missing / wrong) | Impact if unresolved | Affected stakeholders | Priority | Candidate response |
|---|---|---|---|---|---|---|---|
| GAP-001 | Dispatch notes emailed manually by sales admin per order | Dispatch note generated automatically at pick completion | No automated trigger; process depends on one person remembering | Late dispatch notes → ~8% of orders ship late; single point of failure | Warehouse, Sales admin, Customers | High | System change: auto-generate on pick confirmation |
| GAP-002 | | | | | | | |

**Priority scale** (pick one scheme and stick to it):

- **High** — blocks the TO-BE state entirely, or has a compliance/revenue impact now
- **Medium** — degrades the TO-BE state but there's a workable manual workaround
- **Low** — optimisation; the process works without it

*(Alternatively score Impact × Likelihood 1–5 and sort; just don't invent a new scale per project.)*

## 4. Categorised summary

Roll the register up so a steering group can see the shape of the work at a glance:

| Category | Count | High priority | Notes |
|---|---|---|---|
| Process / procedure gaps (fixed by changing how people work) | | | |
| System / technology gaps (fixed by build/config) | | | |
| Data / information gaps | | | |
| People / skills / capacity gaps | | | |
| Policy / compliance gaps | | | |

*The category matters more than it looks: process and people gaps are cheap to close but get ignored because they're not a funded "workstream", while system gaps get all the budget. Call this out explicitly.*

## 5. Cross-cutting themes

*2–4 sentences on what the gaps collectively say. Example: "Most gaps (6 of 9) are handoff failures between Sales Admin and Warehouse — suggesting the priority is a shared order status, not new warehouse tooling."*

## 6. Assumptions, constraints, dependencies

| # | Item | Type *(assumption / constraint / dependency)* | Owner |
|---|---|---|---|

## 7. Sign-off

| Role | Name | Date | Agreed? |
|---|---|---|---|
| Process owner | | | |
| Project / programme lead | | | |

---

### Tips from experience

- **"Impact if unresolved" is what buys the work.** Write it in the stakeholder's language ("8% of orders ship late") not the analyst's ("process inefficiency").
- **Keep gaps and solutions apart.** The "candidate response" column is a hint, not a commitment — that's what the change request and BRD are for.
- **A gap with no owner is a wish.** If a gap doesn't have someone who cares about it closing, downgrade it or drop it.
- **Revisit after UAT.** Some gaps turn out not to matter, and some new ones appear. Version the register, don't rewrite history.

*See [examples/retail-order-fulfilment-gap-analysis.md](../examples/retail-order-fulfilment-gap-analysis.md) for a worked example.*
