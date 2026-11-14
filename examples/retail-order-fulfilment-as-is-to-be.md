# Example: Retail Order Fulfilment — AS-IS → TO-BE

*A fully worked example of the [AS-IS → TO-BE template](../templates/as-is-to-be-process-template.md), filled in with a realistic scenario: order fulfilment at a mid-size homeware retailer running ~400 orders/day. Everything here is fictional but shaped like real projects I've seen — including the parts that don't fit neatly on a map.*

*The companion [gap analysis](retail-order-fulfilment-gap-analysis.md) and [change request](sample-change-request-CR-2026-0021.md) examples follow directly from this map, so you can see the full chain: process map → gap → CR → requirements.*

---

## 1. Header

| | |
|---|---|
| **Process name** | Order fulfilment — order placed → delivered |
| **Process owner** | Sarah Ndlovu, Warehouse Operations Manager |
| **Mapped on** | 12–13 March 2026 (2 × 2-hour workshops) |
| **Mapped by** | Ashutosh Aher (BA) |
| **Participants** | Sarah Ndlovu (Warehouse Ops), Tom Bradley (Sales Admin lead), Priya Menon (Customer Service lead), Dev Rao (Inventory systems), + 2 warehouse team leads (AS-IS session only) |
| **Version** | v1.0 — validated 20 March 2026 |

## 2. Scope

- **Trigger** — customer places an order on the website or by phone.
- **End point** — goods delivered with proof of delivery (POD) captured and the order closed.
- **In scope:** order entry → stock allocation → pick/pack → dispatch → delivery → POD → order closure.
- **Out of scope:** returns and refunds (separate mapping exercise, backlog item), supplier replenishment, payment fraud tooling (interfaces only).
- **Systems:** website checkout (ShopFront), order spreadsheet + email (yes, really), Warehouse Management System (WMS), carrier portal (manual entry), accounting system (AccPac).
- **Volumes:** ~400 orders/day steady, 900+ on promo days. ~12% of orders contain 10+ line items.

## 3. AS-IS process

What actually happens, confirmed with the two warehouse team leads *after* the sponsor-approved version of the process was presented. The difference between the two was itself a finding.

### Swimlane view (AS-IS)

```
Lane: Customer        Lane: Sales Admin (Tom)   Lane: Warehouse (Sarah)     Lane: Courier        Lane: Customer Service
────────────────      ─────────────────────     ──────────────────────      ──────────────       ─────────────────────
[Places order]  ───▶  [Receives order email]
                      [Checks stock in WMS]
                      │ manual lookup, 3-5 min
                      │ ✂ cut here if stock short:
                      │ [Emails customer re. wait] ⚠ back-and-forth (avg 2.1 emails)
                      [Prints pick list]  ───▶   [Picks & packs]
                                                 [Writes dispatch note]
                                                 │ ⚠ paper form
                                                 │◀─────────────────────┐
                      [Emails dispatch note] ◀───┘                      │
                      [Keys order into carrier portal]                  │
                      │ ⚠ re-keying, ~2 min/order                      │
                      │───────────────────────────────────────────────▶ [Collects next day]
                                                                        [Delivers]
                                                                        [POD photo on app] ⚠ never
                      [Chases POD when customer                    ◀───  leaves courier system
                       complains]  ────────────────────────────────────▶ [Emails POD on request]
                                                                          ⚠ 2–5 days later
                      [Closes order in       [Confirms delivery with
                       spreadsheet]           carrier] ⚠ phone call
```

### Step list (AS-IS)

| # | Lane | Step | System | Input → Output | Pain points / waits / rework |
|---|---|---|---|---|---|
| 1 | Customer | Places order | ShopFront | Basket → order email | — |
| 2 | Sales Admin | Opens order email, checks stock per line | WMS (manual lookup) | Order → stock position | 3–5 min/order; no batch view |
| 3 | Sales Admin | If short: emails customer, offers options | Email | Shortage → customer reply | ⚠ Average 2.1 back-and-forth emails; order sits in limbo meanwhile |
| 4 | Sales Admin | Prints pick list | WMS | Order → paper pick list | |
| 5 | Warehouse | Picks and packs | WMS + paper | Pick list → packed parcel | Promote days: 1-day pick backlog |
| 6 | Warehouse | Writes dispatch note (paper) | Paper form | Parcel → dispatch note | ⚠ Note often completes in batches from memory |
| 7 | Warehouse | Hands dispatch notes to Sales Admin | — | Paper handoff | ⚠ Handoff at end of shift; note can lag parcel by a day |
| 8 | Sales Admin | Emails dispatch note to customer | Email | Note → customer | ⚠ The email is the trigger for everything downstream |
| 9 | Sales Admin | Re-keys order into carrier portal | Carrier portal | Order → shipment | ⚠ ~2 min/order; typographical errors → mis-deliveries |
| 10 | Courier | Collects, delivers, captures POD | Courier app | Shipment → delivery | |
| 11 | Customer Service | Chases POD when customer asks | Phone + email | Complaint → POD | ⚠ POD requested manually from courier, 2–5 days |
| 12 | Sales Admin | Closes order in spreadsheet | Spreadsheet | Delivery conf. → closed | ⚠ Two sources of truth (WMS + spreadsheet) |

**Handoff count (AS-IS):** 7 cross-lane handoffs.
**Average lead time (AS-IS):** 2.4 days order → dispatch (target was 1 day); 8.1% of orders dispatched late in Q1 2026.

**Exception path (AS-IS, the one the procedure forgot):** if a line is short-stocked after pick starts (step 5), the warehouse tells Sales Admin verbally. There is no record. Customer Service discovers the problem when the customer calls.

## 4. TO-BE process

### Design principles

1. **Every handoff is a system event**, not a person remembering to pass something on.
2. **Stock is checked once, at order placement** — the customer knows before they pay.
3. **One source of truth for order status** — the WMS; the spreadsheet retires.
4. **POD is captured into our systems automatically**, within 1 hour of delivery.

### Swimlane view (TO-BE)

```
Lane: Customer        Lane: System (ShopFront/WMS)   Lane: Warehouse        Lane: Courier
────────────────      ────────────────────────────   ──────────────────     ──────────────
[Places order]  ───▶  [Validates stock per line]
                      │ ✂ short line? block or
                      │   offer backorder at checkout
                      [Creates order + reservation] ──▶ [Receives digital pick]
                                                        [Picks & packs]
                                                        [Confirms pick] ───▶ [Auto-dispatch note]
                                                                             [Auto-booked with carrier]
                                                                             [Collects same day]
                                                                             [Delivers]
                      [POD synced ≤1h]  ◀──────────────────────────────────  [POD on app → API]
                      [Order auto-closed]
                      [Status visible to customer]
                      & Customer Service (shared view)
```

### Step list (TO-BE)

| # | Lane | Step | System | Input → Output | What changed vs AS-IS |
|---|---|---|---|---|---|
| 1 | Customer | Places order; stock validated at checkout | ShopFront → WMS | Basket → validated order | **New** — was step 2–3 manual check + email loop (BA-001, BA-003) |
| 2 | System | Stock reserved for 30 min at checkout | WMS | Reservation | **New** — prevents sell-what-we-don't-have (BA-002) |
| 3 | System | Order flows to WMS; digital pick task created | WMS | Order → pick task | Replaces printed list + email (step 4) |
| 4 | Warehouse | Picks, packs, confirms in WMS | WMS | Pick task → packed | Adds a confirmation event — the trigger for everything after (BA-004) |
| 5 | System | Dispatch note generated & sent automatically | WMS + email | Confirmation → customer note | **Eliminates steps 6–8** (handoff + re-key) (BA-004) |
| 6 | System | Shipment auto-booked with carrier | Carrier API | Order → shipment + tracking | **Eliminates** manual portal entry (step 9) (BA-012) |
| 7 | Courier | Collects & delivers | Courier | Shipment → delivery | Same day collection because booking happens at pack, not at admin's desk |
| 8 | System | POD synced to order record within 1 hour | Carrier API → WMS | POD → order record | **New** — replaces manual chase (step 11) (BA-012) |
| 9 | System | Order auto-closed; single status visible to CS | WMS | Delivery → closed | Spreadsheet retires; CS self-serves (step 12 eliminated) |

**Handoff count (TO-BE):** 3 (customer → system, warehouse → system, system → courier).
**Target lead time:** ≤ 1 day to dispatch on ≥ 95% of orders.

## 5. Change summary

| # | AS-IS step(s) | TO-BE step | Change type | Rationale |
|---|---|---|---|---|
| 1 | 2–3 (manual stock check + shortage email loop) | 1–2 (validate & reserve at checkout) | Automate + resequence | Removes 3–5 min/order of admin and the 2.1-email average loop; customer decides with full information |
| 2 | 4 (printed pick list) | 3 (digital pick task) | Automate | Paper lists break on promo days |
| 3 | 6–8 (paper note → handoff → email) | 5 (auto dispatch note on pick confirmation) | Eliminate + automate | Kills the end-of-shift handoff; the ⚠ email trigger becomes a system event |
| 4 | 9 (carrier re-keying) | 6 (carrier API booking) | Automate | ~2 min/order returned; typo-driven mis-deliveries disappear |
| 5 | 11 (manual POD chase) | 8 (POD sync ≤1h) | Automate | CS phone calls about PODs are ~15/week today |
| 6 | 12 + spreadsheet (dual order truth) | 9 (WMS as single source) | Eliminate | Two sources of truth caused every reconciliation argument in the workshop |

## 6. Assumptions & open questions

| # | Assumption / question | Owner | Needed by |
|---|---|---|---|
| 1 | Carrier offers a POD-sync API on our current plan *(assumed yes — contract clause 7.2 suggests yes, Dev to confirm)* | Dev Rao | 3 Apr 2026 |
| 2 | ShopFront checkout can reserve stock for 30 min without a re-platform | Dev Rao | 3 Apr 2026 |
| 3 | Q: what happens to in-flight orders at cut-over? *(open — feeds the UAT plan's cut-over scenario)* | Ashutosh | Before UAT |
| 4 | Q: do we still need a *human* fraud review step before pick? *(fraud policy SD-14 says yes; the map shows it nowhere — deliberately out of scope, feeds backlog)* | Priya Menon | Backlog grooming |

---
*This example is referenced by the [gap analysis](retail-order-fulfilment-gap-analysis.md), the [sample change request](sample-change-request-CR-2026-0021.md), and the sample RTM in [tools/sample_data/](../tools/sample_data/rtm_sample.csv) — the BA-001…BA-014 requirement IDs line up across all of them.*
