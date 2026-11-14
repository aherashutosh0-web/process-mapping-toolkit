# Change Request (CR) Template

*The form to use when something needs to change after requirements are baselined — scope, design, timeline, or a production process. A good CR is boring: it makes the change so clear that the approval decision is obvious.*

> **How to use this file:** copy it per request, number it, and don't start work until it's approved — or, if the work genuinely can't wait, mark it "retrospective" and say why. Half the value of this form is the discipline of writing it.

---

## CR form

### 1. Identification

| | |
|---|---|
| **CR number** | CR-YYYY-NNN *(e.g. CR-2026-0021 — never renumber, never reuse)* |
| **Title** | *(≤10 words, specific: "Add partial shipment support to order confirmation" not "Order changes")* |
| **Date raised** | |
| **Raised by** | *(name + role)* |
| **Project / system** | |
| **Related artefacts** | *(links: requirements IDs, process map, gap IDs, defect tickets)* |
| **Priority** | ☐ Critical ☐ High ☐ Medium ☐ Low |
| **Status** | ☐ Draft → ☐ Submitted → ☐ Under review → ☐ Approved / Rejected / Deferred → ☐ Implemented → ☐ Verified |

### 2. Description of change

*What is changing, in plain language. A reader who knows nothing about the project should understand this section.*

### 3. Reason / driver

*Why now? One of: business need changed · regulatory · defect fix · technical necessity · risk reduction · opportunity. Be honest — "the sponsor saw it at the demo" is a real reason and hiding it wastes everyone's time.*

### 4. Options considered

| Option | Description | Pros | Cons | Recommendation |
|---|---|---|---|---|
| A — Do nothing | | | | |
| B — | | | | |
| C — | | | | |

### 5. Impact assessment

| Dimension | Impact | Detail |
|---|---|---|
| **Scope** | None / Minor / Major | |
| **Requirements** | | *(which ReqIDs are added / changed / removed)* |
| **Process / people** | | *(any AS-IS/TO-BE step or role affected?)* |
| **Schedule** | | *(days added, milestones affected — name them)* |
| **Cost** | | *(one-off + ongoing, in money or effort-days)* |
| **Quality / risk** | | *(new risks introduced, risks retired)* |
| **Data / reporting** | | |
| **Compliance** | | *(if regulatory: cite the clause)* |
| **Other live changes** | | *(will this conflict with other approved CRs?)* |

### 6. Risks of *not* doing this

*The section approvers actually read. Quantify where you can.*

### 7. Rollback / contingency

*If this change goes wrong, how do we get back? "Not reversible — migration discards field X after cut-over" is a valid and important answer.*

### 8. Recommendation

☐ Approve · ☐ Approve with conditions · ☐ Reject · ☐ Defer to *(release/date)*

*One paragraph: your call and why.*

### 9. Approval

| Role | Name | Decision | Date | Signature / comment |
|---|---|---|---|---|
| Business owner | | | | |
| Product owner | | | | |
| Technical lead | | | | |
| *(QA / compliance if relevant)* | | | | |

### 10. Implementation & closure

| | |
|---|---|
| **Assigned to** | |
| **Target date** | |
| **Implementation notes** | *(what was actually done — filled in at closure)* |
| **Verification** | *(how it was confirmed: test IDs, sign-off)* |
| **Closed on** | |
| **Closed by** | |

---

### Tips from experience

- **Attach the change to IDs.** "Affects BA-003, BA-007; resolves GAP-002" turns a vague request into a traceable one — and makes updating the RTM mechanical.
- **Options considered is the section people skip and approvers notice.** Even "A: do nothing (rejected because...)" shows the analysis happened.
- **Size the impact honestly.** A CR that says "no schedule impact" and then slips a milestone destroys your credibility on the next ten CRs.
- **Batch tiny related CRs** into one form — nobody wants to approve twelve one-line changes — but never batch unrelated ones.

*See [examples/sample-change-request-CR-2026-0021.md](../examples/sample-change-request-CR-2026-0021.md) for a filled-in example.*
