# CLINOS execution task queue

**Updated:** 2026-11-05. Statuses below reflect current branch and PR evidence; task specifications alone do not establish execution or approval.

| ID | Work order | Priority | Depends on | Primary agent | Status |
|---|---|---|---|---|---|
| [CLINOS-001](https://github.com/pskeffington/CLINOS/issues/2) | [Standards/Epic EHI audit](../codex/orders/CLINOS-001-standards-ehi-audit.md) | P0 | none | Research Director | IN_PROGRESS (primary-source inventory drafted; draft PR #9; branch `codex/clinos-001-standards-audit`; Informatics/Terminology review pending; evidence `evidence/CLINOS-001/SUMMARY.md`) |
| [CLINOS-002](https://github.com/pskeffington/CLINOS/issues/3) | [OSS/competitive/license audit](../codex/orders/CLINOS-002-oss-competitive-audit.md) | P0 | none | Research Director | IN_PROGRESS (nine public repositories inventoried; draft PR #10; branch `codex/clinos-002-oss-audit`; independent Validator/Terminology review pending; evidence `evidence/CLINOS-002/SUMMARY.md`) |
| [CLINOS-003](https://github.com/pskeffington/CLINOS/issues/4) | [Synthetic clinical ground truth](../codex/orders/CLINOS-003-synthetic-ground-truth.md) | P0 | CLINOS-001 + semantic approval | Informatics + Workflow | BLOCKED-DEPENDENCY |
| [CLINOS-004](https://github.com/pskeffington/CLINOS/issues/5) | [Rust workspace/CI](../codex/orders/CLINOS-004-rust-workspace-ci.md) | P0 | G0 architecture baseline | Rust Systems | IN_PROGRESS (local Rust evidence recorded; hosted CI blocked by `startup_failure`, latest run 41942369785; independent QA/security review pending) |
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
- CLINOS-001 and CLINOS-002 are independently in progress on separate branches with draft PRs #9 and #10. Their branches use the G0 draft as base under `codex/NEXT_EXECUTION_ORDER.md`; G0 PR #1 remains unmerged and its governance gate remains open.
- The research tasks can proceed independently of CLINOS-004 hosted CI. No review, merge, retarget, or governance approval is implied by their execution.
- CLINOS-003, CLINOS-005, and CLINOS-006 remain dependency-gated; CLINOS-007 normalization and later semantics remain unstarted.

## Evidence linkage
For each task add: issue URL (if created), branch, PR, owner, independent reviewer, evidence path, last checked commit SHA and reproducibility command. Do not report PASS without both execution and independent review.

## GitHub issue index
- [CLINOS-001 standards/EHI audit](https://github.com/pskeffington/CLINOS/issues/2)
- [CLINOS-002 OSS/competitive audit](https://github.com/pskeffington/CLINOS/issues/3)
- [CLINOS-003 synthetic ground truth](https://github.com/pskeffington/CLINOS/issues/4)
- [CLINOS-004 Rust workspace/CI](https://github.com/pskeffington/CLINOS/issues/5)
- [CLINOS-005 reconciliation schema](https://github.com/pskeffington/CLINOS/issues/6)
- [CLINOS-006 independent QA](https://github.com/pskeffington/CLINOS/issues/7)

## Continuity and blocker owner
The **Block Resolution and Continuity Agent** (`agents/block-resolution.md`) classifies blockers and recommends a permitted next task using `codex/CONTINUITY_POLICY.md`. The original CLINOS-004 hosted-CI blocker remains open pending job allocation or diagnostic logs. Independent fallback research CLINOS-001 and CLINOS-002 is now in progress on separate draft PR branches under `codex/NEXT_EXECUTION_ORDER.md`. No autonomous approval, safety-gate clearance, or merge is implied.
