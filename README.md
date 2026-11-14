# Business Process Mapping & Gap Analysis Toolkit

*A working BA's reusable artifact library — the templates, examples and workshop notes I use to take a process from "everyone describes it differently" to "agreed, funded, and testable".*

Most of a business analyst's job isn't analysis — it's producing the same ten documents over and over, under time pressure, while everyone argues about what "dispatch" means. This repo is the artifact library I wish I'd had from day one: templates that are actually filled in with guidance (not empty shells), two worked examples that chain together so you can see how a workshop complaint becomes a change request, a couple of practitioner guides, and one small Python tool that catches the mistakes I kept making in traceability matrices.

Everything here is meant to be copied, butchered and made yours. A template you have to fight is a template you'll abandon by week two.

---

## The chain the toolkit supports

The artefacts aren't ten separate documents — they're one chain. Each one feeds the next:

```
Workshop  →  Process map  →  Gap analysis  →  Change requests  →  Requirements
(docs)      (templates)     (templates)      (templates)         (BRD/FRD/stories)
   │                            │                                        │
   └────────────────────────────┴───────────────→ RTM ←── UAT plan ←─────┘
                                                   │
                                          tools/validate_rtm.py
                                          (keeps it honest)
```

The examples follow one scenario end-to-end — a homeware retailer's order fulfilment process — so you can watch a pain point in a workshop map become GAP-006, then CR-2026-0021, then requirements and test cases. That chain is the bit that's hard to learn from templates alone.

---

## What's in this repo

```
process-mapping-toolkit/
├── templates/               # 10 ready-to-use artefact templates
├── examples/                # 3 fully-worked examples (one connected scenario)
├── docs/                    # 2 practitioner guides
├── tools/                   # validate_rtm.py + sample data + tests
├── requirements.txt         # pytest only (the tool itself is stdlib)
├── CONTRIBUTING.md
└── LICENSE                  # MIT
```

## Templates

Copy one per artefact and fill in every box — anything you can't fill in is itself a finding.

| Template | Use it when | Filled-out example |
|---|---|---|
| [AS-IS → TO-BE process](templates/as-is-to-be-process-template.md) | You need to document how a process works now and design how it *should* work — with swimlane guidance | [Retail Order Fulfilment](examples/retail-order-fulfilment-as-is-to-be.md) |
| [Gap analysis](templates/gap-analysis-template.md) | The map is validated and you need a prioritised, fundable list of what's missing | [Retail fulfilment gap analysis](examples/retail-order-fulfilment-gap-analysis.md) |
| [Change request](templates/change-request-template.md) | Scope/requirements are baselined and something needs to change | [CR-2026-0021](examples/sample-change-request-CR-2026-0021.md) |
| [Use case](templates/use-case-template.md) | The interaction has exceptions that won't fit in a story card | — |
| [User story](templates/user-story-template.md) | Sprint-sized requirements, with Given/When/Then patterns and a worked scenario | — |
| [BRD outline](templates/brd-outline.md) | You're writing the "what and why" doc that gets a solution funded | — |
| [FRD outline](templates/frd-outline.md) | You're writing the "how it must work" doc the build team implements from | — |
| [RTM](templates/rtm-template.md) | You need to prove every requirement is tested — and every test traces to a requirement | [Sample RTM CSV](tools/sample_data/rtm_sample.csv) |
| [UAT test plan](templates/uat-test-plan-template.md) | The business is about to prove the solution works for real | Sample test case included |
| [Stakeholder analysis](templates/stakeholder-analysis-template.md) | Week one, and whenever the org chart moves (power/interest grid) | — |

Every template carries its own "tips from experience" section — the stuff I learned by getting it wrong first.

## Examples

Three documents, one scenario, all cross-linked so you can follow the IDs:

1. **[Retail Order Fulfilment — AS-IS → TO-BE](examples/retail-order-fulfilment-as-is-to-be.md)** — a 400-orders-a-day retailer, seven handoffs, a paper dispatch note, and two sources of truth. Includes the exception path the procedure pretends doesn't exist.
2. **[Gap analysis for the same process](examples/retail-order-fulfilment-gap-analysis.md)** — 8 gaps rolled up into 2 root causes, with the "impact if unresolved" written in language that funds work ("~8% of orders dispatch late", not "process inefficiency").
3. **[CR-2026-0021 — partial shipment support](examples/sample-change-request-CR-2026-0021.md)** — the change request that GAP-006 became: options considered, honest impact assessment, a rollback plan, and conditions on approval.

## Docs

- **[How to run a process mapping workshop](docs/how-to-run-a-process-mapping-workshop.md)** — my field notes: who to invite, the questions that dig out reality ("and then what *actually* happens?"), the hour-by-hour shape, the facilitation traps I've fallen into, and a checklist you can steal.
- **[Process mapping notations](docs/process-mapping-notations.md)** — BPMN-lite: the seven shapes you actually need, swimlane rules, annotation conventions, and the mistakes that make maps unreadable.

## The one tool: `validate_rtm.py`

A small, stdlib-only script that sanity-checks a Requirements Traceability Matrix CSV before you paste it into a steering pack and get asked why half the requirements have no test case:

```bash
python tools/validate_rtm.py tools/sample_data/rtm_sample.csv
```

```
[MISSING_COVERAGE] BA-005: no linked test case — this requirement is untested
[MISSING_FIELD] BA-011: required column 'Requirement' is empty
[ORPHANED_REQ] BA-011: no source and no test case — lost at both ends of the trace
[MALFORMED_TEST_ID] BA-013: 'TC-17A' doesn't match pattern TC-\d{3}

14 requirement(s) | 12 covered | 2 uncovered | coverage 85.7% | 4 finding(s)
```

It checks for orphaned requirements, missing test coverage, duplicate IDs, malformed test-case references and bad priorities — and it exits non-zero when it finds problems, so it drops into a pre-commit hook or CI step. Details in [tools/README.md](tools/README.md).

### Tests

```bash
python -m pytest        # 11 tests, should all pass
```

The tests cover each check, the seeded problems in the sample data, custom patterns, and the CLI exit codes. If the tool ever changes behaviour, they'll tell you.

## A note on the examples

The retailer, the names and the numbers in `examples/` are fictional — but the *shapes* are real: the 2.1-email average shortage loop, the dispatch note that lags the parcel by a day, the POD that lives in someone else's app. If any of it feels familiar, that's the point.

## Limitations (being honest)

- The templates carry my biases: they suit mid-size business/system change projects in regulated-ish industries (retail, logistics, finance ops). If you're doing pure agile delivery, product discovery, or safety-critical process work, take the shapes and rewrite the framing.
- The examples are one scenario deep. A government benefits process or a manufacturing line would stress these templates differently — I haven't shown that.
- The notation guide is deliberately BPMN-lite. A BPMN-certified reviewer will find things a formal spec would call sloppy; that's a trade I make on purpose for readability, but it *is* a trade.
- `validate_rtm.py` validates the *matrix*, not the *requirements* — it can tell you a requirement has no test case, not whether the requirement is any good. That judgement is still the job.
- Nothing here is a methodology. I don't cover BABOK formally, and the priority scales are practical, not academically weighted.

## What I'd do next

- A **BRD + FRD worked example** continuing the retail scenario — the templates have guidance, but the chain currently stops at the CR.
- A second scenario in a **different domain** (I'd pick insurance claims — heavy exception paths) to stress-test the use case and UAT templates properly.
- Extend `validate_rtm.py` with a **reverse check**: a second CSV of test cases, so it can flag test cases that trace to no requirement. That's the check I do by eye today.
- A one-page **"BA first 2 weeks on a project" checklist** — the templates are the artefacts; the sequencing is still only in my head.

## License & contributing

MIT — take it, use it on real projects, no attribution gymnastics needed. Improvements welcome via [CONTRIBUTING.md](CONTRIBUTING.md); the templates especially should evolve from other people's scars, not just mine.

---

If you've used this on a real project and something was missing or wrong, I'd genuinely like to hear about it — the "tips from experience" sections only grow that way.

— Ashutosh
