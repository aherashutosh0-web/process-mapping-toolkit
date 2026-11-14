# Business Requirements Document (BRD) — Outline

*Section-by-section outline of a BRD: the "what and why" document that gets a solution agreed and funded. The FRD (see [frd-outline.md](frd-outline.md)) handles the "how"; don't let the BRD drift into UI design.*

> **How to use this outline:** fill sections in this order — 1, 2, 3, 5, 6, 7, 8, then circle back to the executive summary *last* (you only know the summary once the body exists). Keep it in this template's structure so reviewers always know where to look. Length target: 15–30 pages. A 90-page BRD is an unreviewed BRD.

---

## 1. Executive summary *(write last)*

One page. For the steering group member who reads only this: the business problem, what's being proposed, the headline benefits, cost/time envelope, and the decision being asked for. If they remember one sentence, what should it be?

## 2. Document control

| | |
|---|---|
| **Project / programme** | |
| **Version history** | *(v0.1 draft — date — author — summary of change; one row per version)* |
| **Approvals** | *(role, name, decision, date — mirror the sign-off table at the end)* |
| **Distribution** | |
| **Related documents** | *(process maps, gap analysis, market research, policy docs — link everything)* |

## 3. Business context & problem statement

- **Background** — how we got here, in 2–3 paragraphs.
- **Problem statement** — the current pain, quantified. *Numbers > adjectives: "8% of orders ship late" beats "fulfilment is inefficient".*
- **Cost of doing nothing** — what happens over the next 12 months if nobody funds this. This is the section that wins budgets.
- **Strategic alignment** — which business objectives this serves (quote them, with their IDs if they exist).

## 4. Scope

- **In scope** — the capabilities/processes this project will deliver or change.
- **Out of scope** — what people will *assume* is included and isn't. Write this box early and defend it.
- **Phasing** — if delivery is staged, what's in which phase.
- **Interfaces / adjacent systems** — even if not changing, what the solution must live alongside.

## 5. Stakeholders & users

*Summary only — the full analysis lives in the [stakeholder analysis](../templates/stakeholder-analysis-template.md).*

| Stakeholder group | Role in project | Key concern | How engaged |
|---|---|---|---|

*Include a short "who does the work today" description — the end users are usually under-represented in their own projects.*

## 6. Business requirements

The heart of the document. Numbered `BR-nn`, each requirement traceable forward into the RTM.

For each requirement (or group):

- **ID & statement** — "The business must be able to…". One requirement per statement.
- **Rationale** — why, linked to the problem statement.
- **Priority** — MoSCoW (must / should / could / won't).
- **Measure of success** — how we'll know it's met (baseline → target).

| ID | Requirement | Rationale | Priority | Success measure | Source |
|---|---|---|---|---|---|
| BR-001 | | | Must | | Workshop 12 Mar |

## 7. Business rules & policies

Rules that constrain the solution regardless of design — eligibility, calculations, approvals, retention. Numbered `BRULE-nn`; the FRD will reference these, not redefine them.

## 8. Process impacts

*The AS-IS → TO-BE map lives outside this doc; here, summarise:*

- Which processes change and how (link the map).
- Role/org impacts (new roles, removed handoffs, training needs).
- Volumes expected to change.

## 9. Data & reporting requirements

What data must exist, be captured, be reported on, and for how long. Include the KPIs the business will use to judge success (these double as UAT measures).

## 10. Non-functional requirements (business-level)

Only business-level NFRs here (compliance, retention, availability expectations, accessibility standard required, response-time expectations at a business level). Technical NFRs belong in the FRD/architecture docs.

## 11. Constraints, assumptions, dependencies

| # | Item | Type | Impact if wrong | Owner |
|---|---|---|---|---|

## 12. Options appraisal *(if this is an investment decision)*

| Option | Description | Benefits | Costs (order of magnitude) | Risks | Verdict |
|---|---|---|---|---|---|
| A — Do nothing | | | | | |
| B — | | | | | |

## 13. Benefit map & success measures

| Benefit | Baseline | Target | By when | Measured how | Owner |
|---|---|---|---|---|---|

*Benefits without baselines are hopes. If the baseline is unknown, "measure baseline" is the first deliverable.*

## 14. Delivery approach & high-level timeline

Milestones and decision points only — not a project plan. Include the release/training/cut-over shape.

## 15. Risks & issues

| ID | Risk / issue | Probability | Impact | Response | Owner |
|---|---|---|---|---|---|

## 16. Sign-off

| Role | Name | Decision (approve / approve with conditions / reject) | Date | Comment |
|---|---|---|---|---|
| Business owner | | | | |
| Sponsor | | | | |
| *(Finance, compliance as needed)* | | | | |

---

### Tips from experience

- **Sections 3 and 6 do 80% of the work.** A sharp problem statement and clean requirement statements carry a BRD; the rest is scaffolding.
- **Every requirement needs a source column value.** "Workshop 12 Mar", "Policy SD-14", "Interview — fulfilment lead". No source = opinion = someone will challenge it in review.
- **"Won't (this time)" is a real MoSCoW category** and the most valuable one in a scope fight. Use it visibly.
- **Approve the BRD before the FRD is written.** Getting sign-off after design starts means the sign-off is fiction.
