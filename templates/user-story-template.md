# User Story Template (with acceptance criteria patterns)

*For requirements sized to fit in a sprint and testable without a translator. The story is a token; the acceptance criteria are the actual requirement.*

> **How to use this file:** copy the card per story. Keep the story sentence under one line — if it needs two, split it. The acceptance criteria (AC) are where your effort goes: each one should be independently testable and written so a tester can turn it into a test case without asking you anything.

---

## Story card

| | |
|---|---|
| **Story ID** | US-NNN |
| **Title** | *(short noun-verb: "Cancel order before dispatch")* |
| **Epic / feature** | |
| **Related ReqIDs / gap IDs** | *(traceability is not optional — this feeds the [RTM](rtm-template.md))* |
| **Priority** | ☐ Must ☐ Should ☐ Could ☐ Won't (this time) |
| **Story points / estimate** | |
| **Sprint / status** | |

### Story

> **As a** *[specific role — a person, not a department]*
> **I want** *[capability — one thing]*
> **So that** *[the value, in the stakeholder's words]*

*Example: "As a **customer**, I want to **cancel my order before it's dispatched**, so that **I don't have to pay return postage for something I no longer want**."*

### Notes / context

*Links to the process step, mockups, the workshop discussion — anything a developer or tester would otherwise ask you for.*

---

## Acceptance criteria

Write 3–7 criteria. Three patterns cover almost everything; mix them.

### Pattern 1 — Scenario (Given / When / Then)

*Use for behaviour with distinct outcomes. One scenario per outcome.*

```gherkin
Scenario: <outcome name>
  Given <precondition / starting state>
  And <additional context>
  When <the single action under test>
  Then <observable outcome>
  And <additional outcome>
```

**Worked example:**

```gherkin
Scenario: Cancel an order that has not been dispatched
  Given I am logged in as the customer who placed order ORD-1234
  And ORD-1234 has status "Picking complete, not dispatched"
  When I select "Cancel order" and confirm
  Then the order status changes to "Cancelled"
  And the reserved stock is released within 5 minutes
  And I receive a cancellation confirmation email within 15 minutes

Scenario: Attempt to cancel an order already dispatched
  Given order ORD-5678 has status "Dispatched"
  When I select "Cancel order"
  Then the cancel option is not available
  And I see the message "This order has been dispatched — start a return instead"
```

### Pattern 2 — Rule table (business rules / validation)

*Use when the logic is a lookup or calculation — a table beats five scenarios.*

| Condition | Expected result |
|---|---|
| | |

### Pattern 3 — Checklist (non-behavioural criteria)

*Use for the things scenarios make clunky: permissions, NFRs, edge data.*

- [ ] Only the account holder (or a support agent with "cancel" permission) can cancel
- [ ] Action is written to the order audit log with user, timestamp, previous status
- [ ] Page responds within 2 seconds at 100 concurrent users

---

## Definition of Ready (before it enters a sprint)

- [ ] Story sentence fits on one line and the "so that" is real value
- [ ] Every AC is testable — someone can write a pass/fail test from it
- [ ] Acceptance criteria cover at least the main failure path
- [ ] Traceable to a ReqID / epic, and any dependent stories are linked
- [ ] UX artefacts attached (or explicitly "none needed")
- [ ] No unresolved open question that changes the behaviour

## Definition of Done (before it leaves)

- [ ] All AC pass in the test environment
- [ ] Acceptance criteria turned into test cases and logged in the RTM
- [ ] No new defects raised against the story
- [ ] Process map / documentation updated if the process changed

---

### Tips from experience

- **"So that" is the first thing to review.** If the value sentence is "so that the system can do X", it's a technical task wearing a story hat.
- **One action per scenario.** "When I cancel and pay and receive a refund" is three tests.
- **Write the failure scenario first.** Happy paths get written at 5pm on a Friday; the failure paths are where bugs breed.
- **Avoid UI verbs in the "I want"** ("I want a dropdown…"). Describe the capability; let UX decide the dropdown.
- **Vague AC words to hunt down:** "quickly", "user-friendly", "appropriate", "etc.", "and so on". Each one is a future defect ticket.
