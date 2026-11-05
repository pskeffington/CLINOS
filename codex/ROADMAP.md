# CLINOS Codex implementation roadmap

## Operating model
- **Wave 0 — Governance/research**: CLINOS-001 standards and Epic EHI public specification audit; CLINOS-002 open-source landscape, licenses and semantic gap register. Parallel research is permitted; no production integrations.
- **Wave 1 — Data contract**: CLINOS-003 synthetic corpus plus ground-truth invariant specification; CLINOS-005 reconciliation and error classification schema. Clinical Informatics and Terminology Steward must approve contracts.
- **Wave 2 — Build substrate**: CLINOS-004 Rust workspace, CLI skeleton and minimal CI. Implement no clinical inference until Wave 1 contracts are approved; safe scaffolding may proceed in parallel.
- **Wave 3 — Validation harness**: CLINOS-006 adversarial fixtures, independent QA and report design. Use synthetic inputs and explicit false-positive/negative accounting.
- **Wave 4 — Implement core**: CLINOS-007 FHIR R4 parse/normalize; CLINOS-008 semantic integrity diff engine. Requires reviewed G1–G3 contract and completed baseline tests.
- **Wave 5 — Restricted adapters**: CLINOS-009 Epic EHI export adapter on authorized/publicly documented synthetic samples; CLINOS-010 vendor-neutral EHR comparisons (OpenEMR, OpenMRS, Medplum). No undocumented access.
- **Wave 6 — Research extensions**: CLINOS-011 hospital workflow digital twin and CLINOS-012 oncology synthetic research suite, each separately clinically reviewed.
- **Wave 7 — Reporting/release**: CLINOS-013 evidence/reproducibility dashboard, threat model, SBOM and governance. No production clinical readiness claim.

## Dependency DAG
```text
CLINOS-001 ─────┐
CLINOS-002 ─────┴─> G0 review ──────────────> CLINOS-004 (workspace substrate)

CLINOS-001 + terminology approval ─────────> CLINOS-003 (synthetic contract)
CLINOS-001 + CLINOS-003 ───────────────────> CLINOS-005 (reconciliation contract)
CLINOS-003 + CLINOS-005 + runnable harness > CLINOS-006 (QA)
CLINOS-003 + CLINOS-004 + CLINOS-005 ──────> CLINOS-007 (FHIR)
CLINOS-005 + CLINOS-006 + CLINOS-007 ──────> CLINOS-008 (diff engine)
CLINOS-001 + CLINOS-007 + CLINOS-008 ──────> CLINOS-009 (Epic EHI adapter)
```
CLINOS-001 and CLINOS-002 may execute independently and in parallel. This diagram is an overview; `docs/TASK_QUEUE.md` and the individual orders define the blocking dependencies. Later cross-EHR, workflow, oncology and reporting phases require their own gate reviews.

## Gate release contract
| Gate | Completion evidence | Minimum independent review |
|---|---|---|
| G0 | Reviewed source matrix, licensing register, agent charters, ordered tasks | Research Director + independent reviewer |
| G1 | Reproducible synthetic ground truth, provenance and edge cases | Informatics + Privacy |
| G2 | Standards-based parser tests, deterministic output and unsupported-case handling | Rust + Informatics + QA |
| G3 | Corruption detection scores, explicit UNRESOLVED and regression evidence | Migration Auditor + independent QA |
| G4 | Documented EHI export coverage matrix; lawful fixtures; no undocumented interfaces | Research + Privacy + QA |
| G5–G6 | Synthetic workflow/onco invariants and limits of clinical interpretation | Informatics + QA |
| G7–G9 | Reproducible reports, threat model, governance approvals | Security + Independent QA |

## Stop and escalate
Stop on source license ambiguity, privacy leakage, PHI discovery, unmapped clinical terminology, unsupported Epic formats, non-reproducible tests, and any request to use live clinical systems. Use `BLOCKED` with source and remediation.

## Scope acceptance policy
Do not interpret a FHIR-valid bundle as proof of lossless migration. Do not advertise Epic equivalence, Epic support, certification, or clinical correctness without independently reproduced and scoped evidence.

## Continuity during blocked waves
The Block Resolution Agent may keep research moving on independent sources when hosted CI fails. For example, an INFRA startup_failure on CLINOS-004 does not block public-specification audit CLINOS-001 or OSS audit CLINOS-002; it also does not authorize CLINOS-003 semantic approval or bypass CLINOS-004 CI. Refer to `codex/CONTINUITY_POLICY.md`. Each fallback must be explicitly unblocked and must generate separate evidence.

## Current Codex order
The current next-pass directive is `codex/NEXT_EXECUTION_ORDER.md`. It separates standards and OSS source audits from the CLINOS-004 hosted-CI blocker; it provides acceptance criteria for conditional synthetic data contracts without prematurely authorizing semantic implementation.

## CLINOS-014 GPT consultation hardening
The optional consultation agent is an engineering tooling task separate from clinical semantics. See `codex/NEXT_PASS_004.md` and `codex/orders/CLINOS-014-gpt-consult-hardening.md`. It can be developed with synthetic/public inputs while source and clinical mapping reviews remain open, but its output remains untrusted and cannot bypass a gate.
