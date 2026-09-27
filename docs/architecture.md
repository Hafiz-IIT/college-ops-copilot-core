# Architecture

```mermaid
flowchart LR
    N0[student request] --> N1
    N1[category] --> N2
    N2[required fields] --> N3
    N3[missing-info check] --> N4
    N4[office owner] --> N5
    N5[SLA] --> N6
    N6[route/ask]
```

## Rule map
Each supported category maps to an owning office, required fields, and SLA hint.

## Ticket
Carries category, supplied fields, and an event trail.

## Evidence check
Missing required information produces ASK rather than routing an incomplete case.

## Routing
Complete supported requests return the responsible administrative office.

## Design principle
Administrative copilots should surface missing information and ownership instead of fabricating institutional answers.
