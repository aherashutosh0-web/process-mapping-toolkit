# Contributing

Thanks for looking at this with a view to improving it. This repo is a working toolkit, so the best contributions come from real project scars.

## What's welcome

- **Template fixes and additions.** If a template is missing a field you needed on a real project, that's the ideal PR. Templates should stay generic enough to reuse but specific enough to fill in under pressure.
- **"Tips from experience."** Each template has a tips section. A tip earned from getting something wrong is worth more than a style change.
- **Corrections to the docs.** Especially `docs/` — the workshop and notation guides are opinionated field notes, and I'd rather be corrected than consistent.
- **Tool improvements.** `tools/validate_rtm.py` is deliberately small (stdlib only, one file). New checks are welcome if they stay fast and dependency-free. Tests required.

## What's probably out of scope

- Full BPMN-formal notation rewrites (see the honest note in [docs/process-mapping-notations.md](docs/process-mapping-notations.md) — BPMN-lite is a deliberate trade)
- Large methodology frameworks; this is a toolkit, not a certification guide
- Anything that makes a template longer without making it easier to fill in

## Ground rules

1. **Don't break the examples' chain.** The three files in `examples/` cross-reference the same IDs (GAP-006, CR-2026-0021, BA-xxx). If you change one, chase the references.
2. **Every PR that touches `tools/` must keep `python -m pytest` green.** Add tests for new checks.
3. **Keep the voice.** These docs are written like a person talking, contractions and all. "Leverage synergies" PRs will be politely declined.
4. **Real content only.** No stub templates, no placeholder sections — if it's in the repo, someone should be able to use it tomorrow morning.

## Submitting

- Fork, branch, PR with a short note on *which project situation* motivated the change. That context usually improves the change itself.
- For template changes, a before/after example of it being filled in is gold.

## Reporting problems

Open an issue with: which artefact, what went wrong (or was missing), and what you had to invent instead. "I had to add a field" issues are my favourite kind.

— Ashutosh
