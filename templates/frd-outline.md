# Functional Requirements Document (FRD) — Outline

*The "how it must work" document. Where the BRD says "the business must be able to cancel orders before dispatch", the FRD specifies the screens, rules, validations, interfaces and behaviours a build team can implement without guessing.*

> **How to use this outline:** the FRD inherits its scope from the approved BRD — every functional requirement here traces back to a business requirement. If you're inventing business requirements in the FRD, stop and amend the BRD first. Keep requirements atomic: one behaviour per ID, testable in isolation.

---

## 1. Document control

| | |
|---|---|
| **Project / system** | |
| **Parent BRD** | *(link + version)* |
| **Version history** | *(v, date, author, change — tie changes to CR numbers where they exist)* |
| **Approvals** | *(product owner, tech lead, QA lead — FRDs are signed by the people who build and test from them)* |

## 2. Introduction & scope

- **Purpose** — what this document specifies and for whom.
- **In scope / out of scope** — typically narrower than the BRD (this release, this system).
- **Glossary of terms** — *put it here, not buried in an appendix. Terms like "order", "shipment", "dispatch" get three definitions across three teams otherwise.*
- **Related documents** — BRD, process maps, use cases, wireframes, interface specs.

## 3. System context

- **Users & roles** — every actor role and its permissions summary (detail in section 7).
- **System landscape** — what this system talks to (name the systems, direction of flow, protocol at a high level).
- **Context diagram** *(optional but excellent — one box per system, arrows labelled with the data that flows).*

```
        [Customer]           [Support Agent]
             │                      │
             ▼                      ▼
        ┌─────────────────────────────────┐
        │         Order System            │
        └───────┬───────────────┬─────────┘
                │ stock check   │ dispatch events
                ▼               ▼
         [Inventory Svc]   [Warehouse Mgmt]
```

## 4. Functional requirements

The core. Numbered `FR-nn`, grouped by feature/module. For each requirement write **one behaviour per ID** and include, where they apply:

| Field | What to write |
|---|---|
| **FR ID & statement** | "The system shall …" — one sentence, one behaviour |
| **Traces to** | BR ID / gap ID / use case ID (keep the [RTM](rtm-template.md) fed) |
| **Priority** | MoSCoW |
| **Trigger / precondition** | when this behaviour applies |
| **Behaviour** | inputs, processing, outputs — including the failure path |
| **Business rules applied** | `BRULE-nn` references, not rewrites |
| **Data** | fields touched, validations (type, range, mandatory), defaults |
| **UI reference** | wireframe/screen ID if relevant |
| **Frequency / volume** | "runs nightly", "peak 30 req/s" — behaviour and performance meet here |

| FR ID | Statement | Traces to | Priority | Notes |
|---|---|---|---|---|
| FR-001 | The system shall prevent cancellation of an order whose status is "Dispatched" or later. | BR-003, UC-004 ext. 3a | Must | Rule BRULE-012 |

## 5. Screen / report specifications

One subsection per screen or report:

- **Purpose & users**
- **Layout reference** *(wireframe link or ASCII sketch)*
- **Fields** — name, type, validation, mandatory, default, editability by role
- **Actions** — buttons/links, enabled/disabled conditions
- **States** — empty, loading, error, read-only, populated
- **Sorting / filtering / pagination** *(reports: parameters, schedule, recipients, retention)*

## 6. Interface specifications

One subsection per external interface:

| Field | Detail |
|---|---|
| **Direction & system** | outbound → Inventory Service |
| **Trigger** | on order confirmation |
| **Data payload** | field list, types, mandatory |
| **Frequency / mode** | real-time API / batch 15-min / event |
| **Error handling** | retry policy, dead-letter behaviour, manual fallback |
| **Owner on the other side** | team + contact for the interface agreement |

## 7. Roles & permissions

Role-permission matrix. Build teams love this table and testers live in it.

| Permission | Customer | Support Agent | Ops Manager | System Admin |
|---|---|---|---|---|
| View order | own only | all | all | all |
| Cancel order (pre-dispatch) | ✔ | ✔ | ✔ | ✔ |
| Override SLA flag | ✖ | ✖ | ✔ | ✔ |

## 8. Business rules detail

Expand the `BRULE-nn` references from the BRD where the FRD needs calculation/decision detail: formulas, thresholds, precedence, effective dates.

## 9. Data requirements

- **Entities & key attributes** *(a simple entity list — full model lives in design docs)*
- **Volumes & growth** *(rows/day, retention needs)*
- **Migration / conversion** — what comes over from the old system, cleansing rules, cut-over handling
- **Retention & archival** — cite the policy clause

## 10. Non-functional requirements

| ID | Category | Requirement | Measure |
|---|---|---|---|
| NFR-001 | Performance | Order confirmation screen returns in ≤ 2s | 95th percentile, 200 concurrent users |
| NFR-002 | Availability | Core ordering available 99.5% monthly | excludes agreed maintenance windows |
| NFR-003 | Security | All actions on orders written to audit log | retained 7 years |
| NFR-004 | Accessibility | Customer screens meet WCAG 2.1 AA | external audit |

*Categories: performance, availability, security, accessibility, scalability, maintainability, disaster recovery, compliance.*

## 11. Assumptions, constraints & dependencies

| # | Item | Type | Impact if wrong | Owner |
|---|---|---|---|---|

## 12. Open items & out-of-scope follow-ups

| # | Item | Raised | Owner | Target resolution |
|---|---|---|---|---|

## 13. Acceptance & sign-off

- **Acceptance approach** — FRs are the source for test cases; UAT plan references the FRD version it tested against.
- **Sign-off table** *(product owner, tech lead, QA lead, business analyst).*

---

### Tips from experience

- **"The system shall…" keeps you honest** — it forces a testable behaviour. "The system should be user-friendly" can't be tested and doesn't belong in an FRD.
- **Interface sections save projects.** Half of integration pain is requirements-time silence about error handling. Specify retries and fallbacks in writing.
- **Version the FRD against change requests.** When CR-2026-0021 changes FR-014, the version history row says so, and the RTM tells you which test cases need rework.
- **Glossaries feel pedantic until they save a workshop.** "Dispatch" meaning two different things to Sales and Warehouse is a real, recurring, expensive problem.
