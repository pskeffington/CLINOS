# CLINOS execution task queue

**Updated:** 2026-11-04. CLINOS-004 is IN_PROGRESS on a stacked prototype branch; all claims of compilation, CI and clinical compatibility remain NOT_TESTED until independently verified.

| ID | Work order | Priority | Depends on | Primary agent | Status |
|---|---|---|---|---|---|
| [CLINOS-001](https://github.com/pskeffington/CLINOS/issues/2) | [Standards/Epic EHI audit](../codex/orders/CLINOS-001-standards-ehi-audit.md) | P0 | none | Research Director | PLANNED |
| [CLINOS-002](https://github.com/pskeffington/CLINOS/issues/3) | [OSS/competitive/license audit](../codex/orders/CLINOS-002-oss-competitive-audit.md) | P0 | none | Research Director | PLANNED |
| [CLINOS-003](https://github.com/pskeffington/CLINOS/issues/4) | [Synthetic clinical ground truth](../codex/orders/CLINOS-003-synthetic-ground-truth.md) | P0 | CLINOS-001 + semantic approval | Informatics + Workflow | BLOCKED-DEPENDENCY |
| [CLINOS-004](https://github.com/pskeffington/CLINOS/issues/5) | [Rust workspace/CI](../codex/orders/CLINOS-004-rust-workspace-ci.md) | P0 | G0 architecture baseline | Rust Systems | IN_PROGRESS (draft, G0 merge blocked) |
| [CLINOS-005](https://github.com/pskeffington/CLINOS/issues/6) | [Reconciliation schema](../codex/orders/CLINOS-005-reconciliation-schema.md) | P0 | CLINOS-001 + CLINOS-003 | Migration Audit | BLOCKED-DEPENDENCY |
| [CLINOS-006](https://github.com/pskeffington/CLINOS/issues/7) | [Adversarial QA](../codex/orders/CLINOS-006-qa-adversarial.md) | P0 | CLINOS-003 + CLINOS-005 + test harness | Independent Validator | BLOCKED-DEPENDENCY |
| CLINOS-007 | FHIR R4 parse/normalize | P1 | CLINOS-003/004/005 | Rust + Informatics | PLANNED-LATER |
| CLINOS-008 | Semantic integrity diff | P1 | CLINOS-005/006/007 | Migration Audit + Rust | PLANNED-LATER |
| CLINOS-009 | Epic EHI export adapter | P1 | CLINOS-001/007/008 | Adapter engineering | PLANNED-LATER |
| CLINOS-010 | Cross-EHR comparison | P2 | CLINOS-002/007/008 | Interoperability | PLANNED-LATER |
| CLINOS-011 | Hospital workflow simulator | P2 | CLINOS-003/006 | Workflow | PLANNED-LATER |
| CLINOS-012 | Oncology synthetic research suite | P2 | CLINOS-003/006 + clinical review | Informatics | PLANNED-LATER |
| CLINOS-013 | Evidence dashboard/release governance | P2 | CLINOS-006/008 | Evidence + security | PLANNED-LATER |

## Workflow status rules
- PLANNED: task defined, not started.
- BLOCKED-DEPENDENCY: cannot begin until preceding evidence is approved.
- IN_PROGRESS: work underway in a named branch/PR.
- IN_REVIEW: independent evaluator checking evidence.
- PASS: implementation plus independent verification complete.
- FAIL: observed test failure with reproduction evidence.
- BLOCKED: cannot proceed; precise reason and next decision documented.
- PLANNED-LATER: roadmap intent; requires a scoped order before execution.

## Dispatch queue
- Ready for the first **invoked Codex runs**: CLINOS-001 and CLINOS-002, preferably in separate task branches after G0 scaffold PR merges.
- No other task should be marked unblocked solely because the corresponding work-order file exists.
- Once G0 is reviewed, the orchestrator checks branch state and source audit outputs before scheduling next wave.

## Evidence linkage
For each task add: issue URL (if created), branch, PR, owner, independent reviewer, evidence path, last checked commit SHA and reproducibility command. Do not report PASS without both execution and independent review.

## GitHub issue index
- [CLINOS-001 standards/EHI audit](https://github.com/pskeffington/CLINOS/issues/2)
- [CLINOS-002 OSS/competitive audit](https://github.com/pskeffington/CLINOS/issues/3)
- [CLINOS-003 synthetic ground truth](https://github.com/pskeffington/CLINOS/issues/4)
- [CLINOS-004 Rust workspace/CI](https://github.com/pskeffington/CLINOS/issues/5)
- [CLINOS-005 reconciliation schema](https://github.com/pskeffington/CLINOS/issues/6)
- [CLINOS-006 independent QA](https://github.com/pskeffington/CLINOS/issues/7)

## First build branch
- CLINOS-004 prototype: `codex/clinos-004-rust-foundation` (parent `codex/g0-agent-roadmap-literature-scaffold`).
- Initial code authored: five Rust workspace crates, synthetic JSON structural preflight CLI, sample fixtures and CI workflow.
- Build/test/CI evidence: NOT_TESTED at authoring time; see `evidence/CLINOS-004/SUMMARY.md`.
- Follow `codex/START_BUILD.md` for the actual invoked Codex build and verification pass; continue to gate merge on G0 source and governance review.
