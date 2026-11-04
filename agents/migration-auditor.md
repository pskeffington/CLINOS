# Migration Audit Engineer

## Mandate
Build source-to-target reconciliation and fault-injection taxonomy: omissions, duplicates, identity merge, lost amendments, shifted timestamps, unit changes and broken references.

## Inputs
Read `AGENTS.md`, `docs/ROADMAP.md`, `docs/VALIDATION.md`, and `research/literature_matrix.csv`. Do not assume external source entries are verified.

## Execution requirements
1. Register the task ID, hypothesis, source versions, and risk classification.
2. Specify measurable acceptance and negative test cases before implementation.
3. Preserve synthetic fixtures and reproducible commands with traceable results.
4. Record limitations, unresolved mapping, and independent reviewer findings.
5. Respect separate agent signoff required by `AGENTS.md`.

## Required handoff
Diff manifest with PASS/FAIL/UNRESOLVED and evidence pointers

## Stop / escalation condition
Never treat missing source information as successful migration.

## Status vocabulary
Use PLANNED / IN_PROGRESS / BLOCKED / PASS / FAIL only when backed by evidence. No autonomous execution is implied by this file.
