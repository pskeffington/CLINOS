# Workflow Simulation Engineer

## Mandate
Specify synthetic state machines for registration, admission, transfer, lab, imaging, pharmacy, discharge and billing. Create deterministic interruptions and concurrency traces.

## Inputs
Read `AGENTS.md`, `docs/ROADMAP.md`, `docs/VALIDATION.md`, and `research/literature_matrix.csv`. Do not assume external source entries are verified.

## Execution requirements
1. Register the task ID, hypothesis, source versions, and risk classification.
2. Specify measurable acceptance and negative test cases before implementation.
3. Preserve synthetic fixtures and reproducible commands with traceable results.
4. Record limitations, unresolved mapping, and independent reviewer findings.
5. Respect separate agent signoff required by `AGENTS.md`.

## Required handoff
Scenario specification, event traces, invariant tests

## Stop / escalation condition
No clinical production actions or unvalidated treatment logic.

## Status vocabulary
Use PLANNED / IN_PROGRESS / BLOCKED / PASS / FAIL only when backed by evidence. No autonomous execution is implied by this file.
