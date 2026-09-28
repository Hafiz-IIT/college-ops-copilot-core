# College Ops Copilot Core

> Administrative college-operations copilot core for request classification, evidence checking, office routing and SLA hints.

## Status
**Reproducible prototype** with executable code, tests, CI, architecture, evaluation and roadmap documentation.

## Problem
Student administrative requests are often delayed because the wrong office receives incomplete information. A routing core can surface required fields before handoff.

## Architecture
Student request → administrative category → required-field check → destination office + SLA → ASK or ROUTE → audit event.

## Run
```bash
python -m unittest discover -s tests -v
python college_ops_copilot_core.py
```

## Implemented
- Administrative category rules
- Required-document/field checks
- Office routing
- SLA hints
- ASK/ROUTE outcome
- Unknown-category handling
- Audit events
- Tests and CI

## Research lineage
- *Blockchain-Enhanced Education Ecosystems*
- *Adaptive Learning Platforms with Multimodal Interfaces*
- *Human-Centered AI Design for Inclusive Digital Platforms*

## Evaluation
Tests cover complete requests, missing information and unknown categories.

## Limitations
- No student database
- No admissions decision logic
- No academic grading logic
- No production ERP integration

## License
MIT.

## Extended implementation

- `service_catalog.py` moves administrative routing rules into a configurable service catalog instead of hard-coding every workflow.
