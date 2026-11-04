# CLINOS-003 — Deterministic synthetic clinical ground-truth contract

**Priority:** P0 | **Gate:** G1 | **Dependencies:** CLINOS-001 and initial terminology approval | **Primary:** Clinical Informatics Lead + Workflow Simulator | **Reviewers:** Security & Privacy + Independent Validator

## Deliverables
- `docs/SYNTHETIC_DATA_CONTRACT.md` with seed policy, patient/encounter IDs, time-zone conventions, normalization, relationship graph, provenance and amendment handling.
- `datasets/synthetic/README.md` describing permissible test data and generation strategy.
- Specification of fixtures: one ordinary encounter and adversarial cases for duplicate ID, missing encounter, order-result mismatch, lost amendment, changed unit and time shift.
- An explicit ground-truth manifest schema and deterministic hashing strategy.

## Acceptance criteria
- A second operator can recreate each specified fixture from seed and versioned inputs.
- No real names, dates of birth, MRNs or patient data in sample fixtures; dummy identifiers are obviously synthetic.
- Each corrupted fixture identifies exactly the intended defect and expected PASS/FAIL/UNRESOLVED outcome.
- Clinical mapping review and privacy review documented.

## Non-goals
Implementing an Epic parser, production ingestion or testing clinical patient care.

## Universal constraints
Use synthetic or lawfully public metadata only. No PHI, live Epic access, bypass of controls, proprietary code copying or clinical use. Capture source versions, fixtures, command output and limitations. Stop rather than infer undocumented clinical semantics. Independent QA must assess the result; code author cannot self-approve.
