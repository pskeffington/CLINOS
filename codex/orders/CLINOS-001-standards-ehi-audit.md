# CLINOS-001 — Standards and Epic EHI source audit

**Priority:** P0 | **Gate:** G0 | **Dependencies:** none | **Primary:** Research Director | **Reviewers:** Terminology Steward + Clinical Informatics Lead

## Deliverables
- Update standards and Epic public documentation rows in `research/literature_matrix.csv` with verified URL, publication/version date, access date, licensing/use constraints and precise claims.
- Add `research/standards_inventory.md` distinguishing FHIR R4 base spec, applicable US Core/SMART version, EHI export requirements, HL7 v2, terminology, and Epic public API/export documentation.
- Record gaps in `research/gap_register.csv`; do not copy protected vendor material.

## Procedure
1. Verify links from primary official sites, not secondary summaries.
2. Extract supported interfaces and limitations exactly; distinguish publicly documented vs contractual/authorized-only.
3. Specify the minimal Patient, Encounter, Observation, ServiceRequest, DiagnosticReport, Provenance and medication-related resources only where justified.
4. Note any code-set license restrictions before introducing fixtures.

## Acceptance criteria
- Every standards row has a verified/blocked status and evidence URL, version and date; no unverifiable row marked verified.
- At least one stated limitation per major interface family, with scope of claims explicit.
- Clinical Informatics and Terminology reviewer recorded separately.

## Stop criteria
Missing access, uncertain licensing, unpublished Epic internals or material spec conflicts -> BLOCKED, with exact gap and source.

## Universal constraints
Use synthetic or lawfully public metadata only. No PHI, live Epic access, bypass of controls, proprietary code copying or clinical use. Capture source versions, fixtures, command output and limitations. Stop rather than infer undocumented clinical semantics. Independent QA must assess the result; code author cannot self-approve.
