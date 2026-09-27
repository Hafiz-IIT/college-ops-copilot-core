# College Ops Copilot Core

> **Route student administrative requests with explicit evidence requirements, ownership, and SLA hints.**

The older College AI Copilot / ERP ideas covered a huge surface area. This repository narrows them to a defensible operations problem: classify a student administrative request, check required information, identify the responsible office, and expose missing evidence instead of hallucinating resolution.

## Implemented
- administrative request categories
- office routing rules
- required-field checks
- missing-information response
- SLA hints
- ticket event history
- ROUTE/ASK outcome

## Run
```bash
python -m unittest discover -s tests -v
python college_ops_copilot_core.py
```

## Repository map
- `college_ops_copilot_core.py` — core implementation
- `tests/` — deterministic tests
- `examples/` — example request
- `docs/architecture.md` — architecture
- `docs/research-agenda.md` — experiments and research lineage
- `STATUS.md` — exact claims boundary
- `CITATION.cff` — citation metadata

## Pipeline
**student request → category → required fields → missing-info check → office owner → SLA → route/ask**

## Research lineage
This grows out of the earlier College AI Copilot/ERP and education-system capstone discussions while avoiding claims about a full student-information platform.

## Evaluation direction
Generate balanced and ambiguous request sets; measure correct office routing, missing-field detection, unknown-category behavior, and rule coverage.

## Maturity
**Research prototype.** Administrative prototype only. No real student records, admissions decisions, grading, financial aid, institutional integration, or deployed ERP is claimed.
