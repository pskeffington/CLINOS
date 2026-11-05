# CLINOS — Next Codex Execution Order (G0 research + continuity)

**Created:** 2026-11-04
**Execution target:** `pskeffington/CLINOS`
**Governance branch:** `codex/g0-agent-roadmap-literature-scaffold` (draft PR #1)
**Current build branch:** `codex/clinos-004-rust-foundation` (draft PR #8, stacked on G0)
**Primary tasks:** CLINOS-001 (#2), CLINOS-002 (#3)
**Blocked task:** CLINOS-004 (#5), pending hosted CI and independent review

## Mission
Move CLINOS from a locally tested structural prototype to a validated research foundation. Do **not** add FHIR semantics, Epic export parsing, or migration equivalence implementation before standard and terminology contracts are supported by independent evidence. Keep work moving when a dependency is blocked by routing through Tier 1 Block Resolution and Tier 2 Resolution Decision.

## Startup instructions
1. Inspect `main`, G0 PR #1, stacked build PR #8, and exact current commit SHAs before branching.
2. Read `AGENTS.md`, `agents/codex-orchestrator.md`, `agents/block-resolution.md`, `agents/resolution-decision.md`, `codex/ESCALATION_CHAIN.md`, `codex/CONTINUITY_POLICY.md`, `docs/TASK_QUEUE.md`, `docs/VALIDATION.md`.
3. Use a *separate* branch for each independent research task. Do not commit the research task directly on the G0 or CLINOS-004 branch. Use G0 as the base only if PR #1 is still unmerged; retarget to `main` after governance merges.
4. Confirm the current branch and worktree are clean; preserve existing local build evidence. Avoid rewriting or reverting unrelated work.
5. Issue and task IDs must remain stable.

## Wave A — CLINOS-001 standards and export-source audit (P0)
**Agent:** Research Director
**Review:** Clinical Informatics Lead and Terminology Steward

- Open issue #2 and `codex/orders/CLINOS-001-standards-ehi-audit.md`.
- Verify primary source/version/date and license/use terms for FHIR R4, SMART on FHIR, US Core where relevant, USCDI and EHI export requirements, and Epic's publicly accessible interoperability documentation.
- Separate standards-based capabilities, vendor-documented interfaces, authorization-dependent interfaces and unsupported assumptions.
- Inventory Patient, Encounter, Observation, ServiceRequest, DiagnosticReport, Provenance and other resources as *proposed* scope only; do not assert verified mapping until reviewed.
- Produce `research/standards_inventory.md` and update source rows in `research/literature_matrix.csv`.
- Record unsupported cases, version discrepancies, and ambiguity with `UNVERIFIED` or `UNRESOLVED`; do not fabricate version details.

**Acceptance:** Every reviewed claim includes authoritative source, exact version/date, access date, license/use constraints and an explicit limitation. Independent mapping/terminology review remains pending until performed.

## Wave B — CLINOS-002 OSS ecosystem and license audit (P0)
**Agent:** Research Director
**Review:** Independent QA and Terminology Steward

- Open issue #3 and `codex/orders/CLINOS-002-oss-competitive-audit.md`.
- Audit OpenEMR, OpenMRS, Medplum, HAPI FHIR, Inferno, Synthea, OHIF, and EHI-to-FHIR from actual maintained project sources.
- Capture license, maintenance evidence, commit or release version, supported features, tested vs claimed functionality and integration restrictions.
- Classify each candidate `REUSE`, `INTEGRATE`, `DIFFERENTIATE` or `DEFER`. State what cannot be confirmed.
- Produce `research/oss_feature_matrix.md`, update `research/literature_matrix.csv` and `research/gap_register.csv`.
- Do not treat an unavailable repository as proof that no alternative exists.

**Acceptance:** At least eight candidates individually assessed or marked blocked with reasons; evidence and version provenance visible; licensing review distinguished from legal signoff.

## Wave C — CI blocker handling (independent of Wave A/B)
**Agents:** Block Resolution (Tier 1), Resolution Decision (Tier 2 if needed), Codex Orchestrator

- Inspect CLINOS-004 PR #8 exact head, associated Actions runs, workflow files and available job logs; distinguish `startup_failure` before job allocation from application test failures.
- Preserve local evidence (19 reported passing tests) as **local**, not hosted-CI validation.
- Permit only bounded safe diagnostics/retry within the BRCA policy. Do not disable required checks, alter permissions/security policy, bypass reviewers or claim green CI without an actual successful run.
- If the failure cannot be resolved, produce a Tier 1 blocker record. Hand off to Tier 2 with evidence, classification, attempted remediation and alternative tasks.
- Tier 2 records `DEFER`, `SPLIT_SCOPE`, `RESEARCH`, `ESCALATE` or `STOP` according to `agents/resolution-decision.md` and `codex/RESOLUTION_DECISION_TEMPLATE.md`.
- Keep #5/PR #8 blocked on hosted CI and independent QA/privacy review; let Wave A/B continue in separate task branches.

## Wave D — conditional next contracts (do not implement early)
Only after required upstream source and review evidence:
- CLINOS-003: write a deterministic synthetic patient/encounter ground-truth contract with privacy/informatics review.
- CLINOS-005: design structured field-level reconciliation, provenance, and PASS/FAIL/UNRESOLVED/NOT_TESTED evidence schema.
- CLINOS-006: design negative/adversarial fixture assessment.
- Hold CLINOS-007 and later implementation until approvals and task dependencies are satisfied.

## Quality and evidence
Each task must link its exact branch/head SHA, source versions, commands executed, evidence status, unresolved claims, PR and next dependency. Create draft PRs; no autonomous merges, no production PHI, no unauthorized Epic access, no assertion of clinical safety or clinical equivalence from FHIR-shaped JSON.

## Final return format
TASKS ATTEMPTED:
PR / BRANCH / EXACT SHA:
SOURCE AUDIT RESULTS:
CHECKS ACTUALLY RUN:
BLOCKER ID + TIER 1 DECISION:
TIER 2 DISPOSITION (if invoked):
INDEPENDENT REVIEW STATUS:
READY NEXT TASKS:
BLOCKED NEXT TASKS:
SPECIFIC NEXT AUTHORIZED ACTION:

**Completion objective:** Separate reviewable research PRs for CLINOS-001 and CLINOS-002, correct blocker records for CI, and a clear evidence-based gate decision for the next engineering wave. If no execution access exists, mark work not tested rather than reporting completion.
