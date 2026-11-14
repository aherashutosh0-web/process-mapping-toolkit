# Example: CR-2026-0021 — Partial shipment support

*A fully worked example of the [change request template](../templates/change-request-template.md). This is the kind of CR that actually lands mid-project: the requirements were baselined, UAT is six weeks out, and the business discovers a gap it can live with — but would rather not. Context: the [Retail Order Fulfilment](retail-order-fulfilment-as-is-to-be.md) programme.*

---

## CR form

### 1. Identification

| | |
|---|---|
| **CR number** | CR-2026-0021 |
| **Title** | Add partial shipment support for orders over 10 line items |
| **Date raised** | 18 May 2026 |
| **Raised by** | Priya Menon, Customer Service Lead (compiled by Ashutosh Aher, BA) |
| **Project / system** | Order Fulfilment Programme — WMS / ShopFront |
| **Related artefacts** | GAP-006 (gap analysis v1.0) · Requirement BA-005 (RTM) · FR-014, FR-015 (FRD v0.9) · Defect-adjacent: 3 CS escalation calls/week logged as "order stuck" |
| **Priority** | ☐ Critical ☐ High ☑ Medium ☐ Low |
| **Status** | Draft → Submitted (18 May) → Under review (21 May) → **Approved with conditions (28 May)** → *Pending implementation* |

### 2. Description of change

Today, a multi-line order ships only when **every** line is pickable. For orders over 10 line items (≈12% of orders), one unavailable item holds the whole order — currently 4–9 extra days on average.

This CR changes order handling so that, for orders with more than 10 lines:

- available lines are picked and shipped as soon as they're ready;
- the remaining lines follow as one backorder shipment when stock arrives;
- the customer chooses at checkout: **"Ship together"** (default, current behaviour) or **"Ship in stock items first"**;
- one delivery charge applies, regardless of the number of shipments;
- the dispatch notification and tracking page show per-shipment status.

Out of this CR: partial shipments for orders of 10 lines or fewer (rejected — packaging economics don't hold), split by warehouse, and split by supplier.

### 3. Reason / driver

Business need discovered during UAT prep interviews: "order stuck" is the single most common CS escalation category (≈3/week), and it's almost always the last missing item in a large order. GAP-006 flagged this in March but it wasn't funded in the Q2 scope; the customer impact is now better quantified and the fix is smaller than originally assumed because the carrier API work (CR-2026-0014) already delivers multi-parcel tracking.

### 4. Options considered

| Option | Description | Pros | Cons | Recommendation |
|---|---|---|---|---|
| A — Do nothing | Keep all-or-nothing shipping | Zero cost/schedule impact | ~3 escalations/week continue; 4–9 day waits on large orders; undermines the "≤1 day dispatch" programme benefit | ✗ Rejected |
| B — Manual split at warehouse discretion | Allow team leads to split problem orders by exception | ~2 days of config | Uncontrolled, untracked, doesn't scale in peak; no customer choice | ✗ Rejected |
| C — Automatic partial shipment for >10-line orders, customer opt-in at checkout | As described in section 2 | Removes the escalation class entirely; reuses CR-0014 tracking work; measurable (split-ship rate, CS calls) | Requires WMS order-split change + checkout + notification updates | ☑ **Recommended** |
| D — Automatic split for all orders | Same as C without the 10-line threshold | Maximum flexibility | Per-shipment packaging & carriage cost doubles on small orders; Finance estimate £18–24K/yr extra | ✗ Rejected for now; revisit after 3 months of C data |

### 5. Impact assessment

| Dimension | Impact | Detail |
|---|---|---|
| **Scope** | Minor | Adds one behaviour to the order lifecycle; no new workstreams |
| **Requirements** | Changes BA-005 (In review → reworded & split into BA-005a/b); adds BA-015 (delivery charge rule) & BA-016 (per-shipment tracking display) | RTM updated 19 May; `validate_rtm.py` run clean after adding test placeholders |
| **Process / people** | Minor | TO-BE map step 4 gains a "split decision" branch; warehouse pick wave logic gets one new rule; CS macros updated (1 hour) |
| **Schedule** | +8 working days (dev 5, test 3) | Slips UAT start 19 Jun → 1 Jul; go-live 14 Jul unchanged (float consumed) |
| **Cost** | ~9 person-days (dev 5, QA 3, BA 1); no licence cost | Within Q2 contingency (12 days remaining) |
| **Quality / risk** | New risks: split-shipment doubles touch labour on split orders; notification logic is the highest-defect-risk area | Mitigations below; extra test cases added (TC-019…TC-024) |
| **Data / reporting** | Order→shipment is now 1:N; the SLA report must count *shipments*, not orders | Reporting change included in the 8 days |
| **Compliance** | None | Delivery-charge transparency already covered by existing policy (BRULE-007) |
| **Other live changes** | Builds directly on CR-2026-0014 (carrier API) — sequential dependency; must land after it | Sequenced in the plan 26 May |

### 6. Risks of *not* doing this

The programme's headline benefit is "≤1 day to dispatch on 95% of orders". With all-or-nothing shipping, the 12% of orders that are 10+ lines can never hit that target — the benefit claim would be false for roughly 1 in 8 orders, and the CS escalation load (≈150 calls/yr, ~£9K in handling cost) stays. It also quietly undermines UAT sign-off: Priya has stated she'll accept sign-off "with a named exception" rather than block — but a named exception on the main benefit is exactly what the steering group will remember.

### 7. Rollback / contingency

Split behaviour is behind a config flag (`split_ship.enabled`, default **off**). If post-go-live defect rates spike, the flag disables splitting in one config change; orders revert to ship-together with no data migration. Per-shipment delivery-charge logic has been tested against the "ship together" path to ensure no double-charging on rollback.

### 8. Recommendation

☑ **Approve with conditions** — conditions: (1) reporting change (order→shipment SLA counting) must be in the same release, not deferred; (2) the 10-line threshold is reviewed after 3 months of split-ship data, with Option D revisited at that point. The cost is modest, the schedule float exists, and the change retires the top CS escalation category.

### 9. Approval

| Role | Name | Decision | Date | Comment |
|---|---|---|---|---|
| Business owner | Sarah Ndlovu | Approve with conditions | 28 May 2026 | "Threshold review at 3 months is important — peak season will tell us." |
| Product owner | (name) | Approve | 28 May 2026 | |
| Technical lead | Dev Rao | Approve | 27 May 2026 | "Flag-first rollout agreed; config stays until 2 weeks of clean data." |
| Finance (delivery-charge rule) | (name) | Approve | 27 May 2026 | Confirms single-charge rule is acceptable |

### 10. Implementation & closure

| | |
|---|---|
| **Assigned to** | Dev Rao (WMS) + checkout squad |
| **Target date** | 12 June 2026 (before UAT start 1 July) |
| **Implementation notes** | *(to fill at closure)* |
| **Verification** | TC-019…TC-024 (partial shipment cases); regression on TC-001…TC-003 (stock/hold paths); `python tools/validate_rtm.py` clean on updated RTM |
| **Closed on** | *(open)* |
| **Closed by** | *(open)* |

---
*This CR is the last link in the chain shown across the examples: workshop → [process map](retail-order-fulfilment-as-is-to-be.md) (pain point ⚠) → [gap analysis](retail-order-fulfilment-gap-analysis.md) (GAP-006) → CR → requirements (BA-005a/b, BA-015, BA-016) → test cases (TC-019…024) → RTM rows.*
