# CLINOS-005 — Clinical integrity diff and evidence schema

**Priority:** P0 | **Gate:** G3 design | **Dependencies:** CLINOS-001 and CLINOS-003 | **Primary:** Migration Audit Engineer | **Reviewers:** Informatics + Independent Validator

## Deliverables
- `docs/RECONCILIATION_SCHEMA.md` defining normalized identifiers, field comparisons, evidence pointers, severity, certainty, missing source data and versioned rules.
- JSON-schema or documented data contract for findings; statuses `PASS`, `FAIL`, `UNRESOLVED`, `NOT_TESTED`.
- Fault taxonomy and expected outcomes for record missingness, unit shifts, terminology collision, wrong patient, reference mismatch, clock changes and lost history.

## Acceptance criteria
- Every finding includes source/target references, rule ID, evidence path and uncertainty.
- UNRESOLVED cannot silently become PASS and cannot be omitted from denominators.
- Severity classifications are research categories, not clinical risk certifications.
- Sample synthetic fixtures demonstrate expected classifications, including ambiguous mappings.

## Universal constraints
Use synthetic or lawfully public metadata only. No PHI, live Epic access, bypass of controls, proprietary code copying or clinical use. Capture source versions, fixtures, command output and limitations. Stop rather than infer undocumented clinical semantics. Independent QA must assess the result; code author cannot self-approve.
