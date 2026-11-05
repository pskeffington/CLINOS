# CLINOS-006 — Independent QA and adversarial validation plan

**Priority:** P0 | **Gate:** G3 preparation | **Dependencies:** CLINOS-003, CLINOS-005 and runnable basic test harness | **Primary:** Independent Validator | **Reviewers:** Clinical Informatics + Security & Privacy

## Deliverables
- `docs/TEST_PLAN.md` with unit/property/mutation/end-to-end test levels and decision rules.
- `tests/fixtures/README.md` defining seeded positive, negative and ambiguous cases.
- `evidence/CLINOS-006/SUMMARY.md` template for commands, versions, confusion matrix, false-positive and false-negative counts.
- Independent assessment protocol, including a reproducibility attempt by someone other than implementer.

## Acceptance criteria
- At least 10 distinct proposed adversarial fixture categories; include wrong-patient link, shifted time zone, changed units, lost amendment, missing result and false duplicate.
- Classification expected for each fixture and explanation of expected failure mode.
- Report recall and precision where ground truth is known; report unknown/UNRESOLVED separately.
- No claims of full data fidelity or clinical safety from finite fixture coverage.

## Universal constraints
Use synthetic or lawfully public metadata only. No PHI, live Epic access, bypass of controls, proprietary code copying or clinical use. Capture source versions, fixtures, command output and limitations. Stop rather than infer undocumented clinical semantics. Independent QA must assess the result; code author cannot self-approve.
