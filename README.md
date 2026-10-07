# College Ops Copilot Core

<p align="center"><strong>Evidence-Aware Administrative Routing</strong><br/><sub>Classify requests, identify missing information, route to the right office.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-reproducible%20prototype-blue" alt="Prototype"/> <img src="https://img.shields.io/badge/focus-administrative%20AI-orange" alt="Administrative AI"/></p>

## Question

**Can a college operations assistant avoid routing incomplete requests to the wrong office?**

```
Student request
    ↓
Category recognition
    ↓
Required-field check
    ├── ASK
    └── ROUTE
          ↓
      Office + SLA
```

## Try it

```bash
python college_ops_copilot_core.py
python -m unittest discover -s tests -v
```

`service_catalog.py` makes routing rules configurable rather than hard-coded into one workflow.

## Implemented

- administrative categories
- required-field checks
- office routing
- SLA hints
- ASK / ROUTE outcomes
- unknown-category handling
- audit events
- configurable service catalog
- deterministic CI

## Boundary

Administrative workflow prototype only. It does not make academic, legal, financial or disciplinary decisions.

Related: [Hospital Operations Helpdesk](https://github.com/Hafiz-IIT/hospital-ops-helpdesk) · [Agency QA Orchestrator](https://github.com/Hafiz-IIT/agency-qa-orchestrator)
