# AS-IS → TO-BE Process Template

*A working template for documenting a current process and designing its future state. Use it after a process-mapping workshop (see [docs/how-to-run-a-process-mapping-workshop.md](../docs/how-to-run-a-process-mapping-workshop.md)) and before you write the gap analysis.*

> **How to use this file:** copy it, rename it to the process you're mapping, and fill in every section. Anything you can't fill in is itself a finding — write "UNKNOWN" and chase it down. Keep AS-IS and TO-BE on the same page; the whole point is comparing them.

---

## 1. Header

| | |
|---|---|
| **Process name** | |
| **Process owner** | *(who actually owns this, not who sponsors the project)* |
| **Mapped on** | *(date)* |
| **Mapped by** | *(facilitator / BA)* |
| **Participants** | *(names + roles who validated the map)* |
| **Version** | v0.1 *(draft) → v1.0 (validated)* |

## 2. Scope

- **Trigger** — what starts this process? *(e.g. "customer places an order")*
- **End point** — what counts as done? *(e.g. "goods delivered and signed for")*
- **In scope:**
- **Out of scope:** *(be ruthless here — scope creep starts in this box)*
- **Systems involved:**
- **Volumes / frequency:** *(e.g. "~400 orders/day, peak 900 on promo days")*

## 3. AS-IS process

> Map what **actually happens**, not what the procedure document says happens. If the official process and reality differ, map reality and note the difference — that's usually where the gold is.

### Swimlane view

**Swimlane guidance:** one lane per *role* (not per person, not per system — systems can be noted inside a step). Every step goes in exactly one lane: the lane of whoever *does* it. Cross-lane handoffs are where delays and dropped balls live, so make handoffs visible as arrows that cross lane boundaries, and count them.

```
Lane: Customer        Lane: Sales Admin     Lane: Warehouse       Lane: Courier
────────────────      ────────────────      ────────────────      ────────────────
[Places order]  ───▶  [Checks stock]
                      │ in stock            │
                      ├──────────────────▶  [Picks & packs]
                      │                     │
                      │  ⚠ manual email     │
                      │◀──────────────────  [Raises dispatch note]
                      [Emails customer] ───▶│
                                            [Hand to courier] ──▶ [Delivers]
                                                                 [Gets POD photo]
                                                                 ⚠ POD stays on
                                                                   courier app
```

### Step list

| # | Lane (role) | Step | System | Input → Output | Pain points / waits / rework loops |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

**Handoff count:** *(how many times work crosses a lane — the thing to minimise)*
**Average lead time (AS-IS):** *(trigger to end, even if it's an estimate — "2–4 days" beats nothing)*

## 4. TO-BE process

### Design principles

*State the 2–4 rules the new process obeys, so future decisions are easy. Example: "every handoff must be a system event, not a person remembering to send an email."*

1.
2.

### Swimlane view (TO-BE)

```
(same lane structure as AS-IS so the two are visually comparable)
```

### Step list (TO-BE)

| # | Lane (role) | Step | System | Input → Output | What changed vs AS-IS |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

**Handoff count (TO-BE):**
**Target lead time:**

## 5. Change summary

| # | AS-IS step | TO-BE step | Change type *(automate / eliminate / combine / resequence / add)* | Rationale |
|---|---|---|---|---|
| 1 | | | | |

## 6. Assumptions & open questions

| # | Assumption / question | Owner | Needed by |
|---|---|---|---|

---

### Tips from experience

- **Map AS-IS in the room, TO-BE afterwards.** Designing the future while documenting the present produces a map of everyone's wishlist, not reality.
- **Count handoffs before and after.** "We reduced handoffs from 7 to 3" is the one number stakeholders remember.
- **The pain-point column is the bridge** to your gap analysis — every ⚠ in it is a candidate gap.
- **Validate the map with the people who do the work**, separately from the sponsor. They'll tell you about the exception path everyone pretends doesn't exist.
- **Include at least one exception path** (out-of-stock, cancellation, failed delivery). Happy-path-only maps are fiction.

*See [examples/retail-order-fulfilment-as-is-to-be.md](../examples/retail-order-fulfilment-as-is-to-be.md) for a fully filled-in version of this template.*
