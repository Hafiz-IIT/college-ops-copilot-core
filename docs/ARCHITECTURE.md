# Architecture

Student request → administrative category → required-field check → destination office + SLA → ASK or ROUTE → audit event.

## Invariants
1. Missing required fields must be surfaced before routing.
2. Unknown categories must not be silently guessed.
3. Routing rules remain explicit/configurable.
