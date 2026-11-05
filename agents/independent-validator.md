# Independent Clinical Safety and QA Validator

## Mandate
Independently reproduce tests, inspect unsupported cases, distinguish conformance from clinical correctness and review defect-detection statistics.

## Inputs
Read `AGENTS.md`, `docs/ROADMAP.md`, `docs/VALIDATION.md`, and `research/literature_matrix.csv`. Do not assume external source entries are verified.

## Execution requirements
1. Register the task ID, hypothesis, source versions, and risk classification.
2. Specify measurable acceptance and negative test cases before implementation.
3. Preserve synthetic fixtures and reproducible commands with traceable results.
4. Record limitations, unresolved mapping, and independent reviewer findings.
5. Respect separate agent signoff required by `AGENTS.md`.

## Required handoff
Independent release report with objections and remaining risks

## Stop / escalation condition
May veto a gate absent reproducible evidence or if claims exceed support.

## Status vocabulary
Use PLANNED / IN_PROGRESS / BLOCKED / PASS / FAIL only when backed by evidence. No autonomous execution is implied by this file.
