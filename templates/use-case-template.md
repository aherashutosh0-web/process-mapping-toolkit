# Use Case Template

*For capturing a single interaction between an actor and the system, with all the ugly branches spelled out. Use cases earn their keep on processes with lots of exceptions — happy paths fit in a user story; error paths don't.*

> **How to use this file:** one use case per copy. Write the main success scenario first (5–10 steps, verb-first), then add extensions — every "but what if..." from the workshop goes there. If an extension needs its own screens and rules, it may deserve its own use case.

---

## Use case: *(UC-NNN: verb-first title, e.g. "UC-004: Place order with backordered items")*

### 1. Summary

| | |
|---|---|
| **Use case ID** | UC- |
| **Name** | |
| **Related requirements** | *(ReqIDs this use case satisfies — keep the RTM honest)* |
| **Related process step** | *(step # from the AS-IS/TO-BE map)* |
| **Version / date** | |
| **Author** | |

### 2. Actors

| Actor | Type | Description |
|---|---|---|
| *(primary actor — who triggers this)* | Primary | |
| *(supporting actors — other people/systems involved)* | Supporting | |
| *(offstage actors — compliance, finance, etc. who care but don't interact)* | Offstage | |

### 3. Preconditions

*What must be true before this starts. Testable facts only — "the user is logged in and has at least one in-stock item in the basket."*

1.
2.

### 4. Trigger

*The event that starts the use case. ("Customer clicks 'Place order'.")*

### 5. Main success scenario (basic flow)

*Short declarative steps. Actor does X → system does Y. No branching here.*

| # | Actor action | System response |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

### 6. Postconditions (guarantees)

*What's true after a successful run — this is what makes the use case "done". Include what's committed/persisted and any notifications sent.*

- **Success guarantee:**
- **Minimal guarantee** *(what's true even if it fails — no partial charges, no orphaned records):*

### 7. Extensions (alternative & exception flows)

Number them as `X.Y` where X is the step they branch from.

| Ext. | Branches from | Condition | Response |
|---|---|---|---|
| 1a | Step 1 | | |
| 2a | Step 2 | | |
| 2b | Step 2 | | |

### 8. Business rules referenced

| Rule ID | Rule |
|---|---|
| BR- | |

### 9. Data requirements

| Data item | Description | Validation | Source |
|---|---|---|---|

### 10. Non-functional requirements touched

*Performance ("response within 2s at 200 concurrent users"), security, retention, accessibility — quote the NFR IDs.*

### 11. Open questions

| # | Question | Owner | Raised | Resolved |
|---|---|---|---|---|

---

### Tips from experience

- **Steps should number in single digits for the main flow.** If you're at step 14, that's two use cases wearing a trench coat.
- **Extensions are where the requirements actually live.** Developers build the main flow on day one; the extension table is what they'll ping you about in week three.
- **The minimal guarantee is underrated** — it's the promise the system makes when things go wrong, and it's usually what auditors ask about.
- **Don't force every requirement into a use case.** Data retention and reporting requirements belong in the FRD/BRD; only interactive behaviour belongs here.
