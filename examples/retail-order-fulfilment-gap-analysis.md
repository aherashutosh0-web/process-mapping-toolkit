# Example: Retail Order Fulfilment — Gap Analysis

*A fully worked example of the [gap analysis template](../templates/gap-analysis-template.md), continuing the [Retail Order Fulfilment](retail-order-fulfilment-as-is-to-be.md) process map. If you've read the map, this is the natural next document — the ⚠ marks from the map turned into a funded worklist.*

---

## 1. Header

| | |
|---|---|
| **Process / domain** | Order fulfilment — order placed → delivered |
| **Linked process map** | [retail-order-fulfilment-as-is-to-be.md](retail-order-fulfilment-as-is-to-be.md) v1.0 |
| **Date** | 25 March 2026 |
| **Author** | Ashutosh Aher (BA) |
| **Reviewers** | Sarah Ndlovu (process owner), Tom Bradley (Sales Admin lead), Dev Rao (inventory systems) |

## 2. Method in one paragraph

Gaps were identified by comparing the validated AS-IS map (v1.0) against the TO-BE design, plus every pain point raised in the two workshops and the follow-up interviews with warehouse team leads. Each gap was then reviewed line-by-line with Sarah Ndlovu and Tom Bradley on 24 March — two candidate gaps (quality checks at pack, supplier delivery slots) were cut as out-of-scope for this programme, which is why the numbering has holes.

## 3. Gap register

| Gap ID | Current state (AS-IS) | Future state (TO-BE) | Gap | Impact if unresolved | Affected stakeholders | Priority | Candidate response |
|---|---|---|---|---|---|---|---|
| GAP-001 | Stock checked manually per order after placement; shortages handled by email loop (map steps 2–3) | Stock validated & reserved at checkout (TO-BE steps 1–2) | No stock-check at order placement; no reservation mechanism | 3–5 min admin/order (~28 hrs/week); 2.1-email average shortage loop; oversell on promo days (14 incidents in Q1) | Sales Admin, Customers, Finance (refunds) | High | System change: ShopFront–WMS stock check + 30-min reservation (BA-001, BA-002) |
| GAP-002 | Dispatch note written on paper, passed by hand at shift end, emailed manually (steps 6–8) | Auto-generated & sent on pick confirmation (TO-BE step 5) | No system trigger; process depends on one person's memory; handoff lags parcel by up to a day | ~8% of orders dispatch late (Q1 2026); single point of failure — process stalls when Tom is on leave (happened twice in Feb) | Sales Admin, Warehouse, Customers | High | System change: auto-generate dispatch note on pick-confirm event (BA-004) |
| GAP-003 | Order re-keyed manually into carrier portal (step 9) | Shipment auto-booked via carrier API (TO-BE step 6) | No integration with carrier; duplicate data entry | ~2 min/order (~22 hrs/week); keying errors caused 6 mis-deliveries in Q1 | Sales Admin, Customers, Courier | High | Integration: carrier booking API (BA-012) |
| GAP-004 | POD lives in the courier's app; retrieved by phone/email chase (step 11) | POD synced to order record within 1 hour (TO-BE step 8) | No POD data flow back into our systems | CS spends ~4 hrs/week chasing PODs; 2–5 day wait for customers; disputes hard to defend without evidence | Customer Service, Customers | Medium | Integration: carrier POD sync (BA-012) |
| GAP-005 | Order status lives in both WMS and a shared spreadsheet (step 12) | WMS is the single source of truth (TO-BE step 9) | Two sources of truth; no reconciliation process | Weekly reconciliation arguments (observed in workshop); CS answers status questions from the *wrong* system ~daily | Sales Admin, Customer Service | Medium | Process + system: retire spreadsheet once status is customer-visible; add CS shared view (BA-006) |
| GAP-006 | No partial shipments: a 12-line order waits for the last item | Partial shipments allowed for orders over 10 lines (backorder item ships when available) | WMS treats an order as all-or-nothing | Large orders sit 4–9 extra days; ~3 escalation calls/week; the "last missing item" is the single most common CS complaint category | Customer Service, Customers, Warehouse | Medium | System change: split-shipment support *(see [CR-2026-0021](sample-change-request-CR-2026-0021.md), currently the response for BA-005)* |
| GAP-007 | No training material for new warehouse staff on the pick/confirm process | Standard work + training pack for the TO-BE process | Knowledge lives with two team leads; nothing written down | New starters take ~3 weeks to full productivity; TO-BE process will be a hard cut-over for temps during peak season | Warehouse team leads, Temps | Low | Process: standard-work pack + 1-hour training, built during UAT week |
| GAP-008 | Failed-delivery refunds handled ad hoc; no 24-hour rule | Refunds raised within 24h of failed delivery per consumer law | No trigger or SLA on refund raising | Compliance exposure (consumer law); 2 refunds in Q1 breached informal expectations | Customer Service, Finance, Compliance | High | Policy + system: refund trigger on failed-delivery status (BA-007) |

## 4. Categorised summary

| Category | Count | High priority | Notes |
|---|---|---|---|
| Process / procedure gaps | 2 (GAP-005, GAP-007) | 0 | Cheap; fold into the change management work |
| System / technology gaps | 4 (GAP-001, 002, 003, 006) | 3 | The funded core of the programme |
| Data / information gaps | 1 (GAP-004) | 0 | Same integration as GAP-003 — do both in one carrier-API work package |
| People / skills / capacity gaps | 1 (GAP-007) | 0 | |
| Policy / compliance gaps | 1 (GAP-008) | 1 | Small build, disproportionate risk if ignored |

## 5. Cross-cutting themes

Eight gaps, but only two root causes. **Four of them are handoff failures between Sales Admin and everything else** — the process currently routes through one person's inbox and memory, and every gap in that cluster (GAP-001/002/003) is fixed by moving the trigger from "person remembers" to "system event". The second theme is **data that leaves and never comes back** (POD, carrier status) — fixed by one integration work package rather than two projects. If someone asks for the short version: *fund the system-event work and the carrier integration; handle the rest with process discipline.*

## 6. Assumptions, constraints, dependencies

| # | Item | Type | Owner |
|---|---|---|---|
| 1 | Carrier API covers both booking and POD on our current contract tier | Dependency | Dev Rao |
| 2 | No WMS upgrade lands before Q4 2026 (the TO-BE must build on the current version) | Constraint | Sarah Ndlovu |
| 3 | Sales Admin headcount stays flat — the TO-BE frees ~50 hrs/week, assumed redeployed to customer follow-ups, not cut | Assumption | Sponsor (to confirm) |
| 4 | Peak-season freeze: no releases 15 Nov – 15 Jan | Constraint | PM |

## 7. Sign-off

| Role | Name | Date | Agreed? |
|---|---|---|---|
| Process owner | Sarah Ndlovu | 27 Mar 2026 | ✅ Yes |
| Programme lead | (sponsor) | 29 Mar 2026 | ✅ Yes — GAP-001/002/003/008 funded for Q2; 006 via CR |

---
*Requirement IDs in brackets (BA-xxx) match the sample RTM at [tools/sample_data/rtm_sample.csv](../tools/sample_data/rtm_sample.csv). GAP-006 became [CR-2026-0021](sample-change-request-CR-2026-0021.md) — the full chain from workshop to change request, one document at a time.*
