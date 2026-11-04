# Codex execution control plane

CLINOS is a **synthetic-data, vendor-neutral clinical integrity research project**, not an Epic clone or production medical device.

## Start here
1. Read repository `AGENTS.md` and `agents/codex-orchestrator.md`.
2. Inspect `docs/TASK_QUEUE.md`, `docs/ROADMAP.md`, `docs/VALIDATION.md`, `codex/ROADMAP.md` and `research/literature_matrix.csv`.
3. Select exactly one unblocked task in `codex/orders/`; verify upstream evidence.
4. Use `codex/CODEX_PROMPT.md` for implementation instructions.
5. Create a separate `codex/<task-id>-<slug>` branch for each executable task after G0 is merged.
6. Commit only scoped changes, attach evidence, and create a draft PR; request independent review.

## Repository execution policy
- Do not claim that authored agent files automatically execute tasks. These files guide human/Codex runs when invoked.
- No production PHI, live EHR data, production authorization, live orders, or patient care.
- No reverse engineering of protected binaries, bypassing Epic access controls, or copying proprietary code.
- Every mapping must have provenance; missing information becomes `UNRESOLVED`, not fabricated equivalence.
- Clinical safety and certification are separate from JSON/FHIR conformance.
- Never merge a PR solely from a green compile; independently reproduce task acceptance tests.
- Prioritize correctness, observability, reproducibility, privacy and data governance over throughput.

## Work packet layout
Each order specifies purpose, dependencies, roles, inputs, proposed changes, tests, evidence, stop criteria and definition of done. Reports go in `evidence/<task-id>/` (new work only), including a summary and the exact commands; redact host identifiers and secrets.

## Work that can start immediately
`CLINOS-001` standards/EHI research and `CLINOS-002` OSS landscape/license audit are non-code G0 tasks and can be run separately after this bootstrap is reviewed. `CLINOS-003` synthetic corpus design needs terminology and invariant agreement. All compatibility findings initially remain unverified.
