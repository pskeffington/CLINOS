# CLINOS-002 — Open-source EHR ecosystem and license audit

**Priority:** P0 | **Gate:** G0 | **Dependencies:** none | **Primary:** Research Director | **Reviewers:** Terminology Steward + Independent Validator

## Deliverables
- Update open-source repository entries in `research/literature_matrix.csv` and create `research/oss_feature_matrix.md`.
- Capture repository URL, project role, maintenance/activity date, supported interfaces, stable version/commit, license identifiers, dependencies, tested vs claimed features and known limitations.
- Map overlaps with OpenEMR, OpenMRS, Medplum, HAPI FHIR, Inferno, Synthea, OHIF and `jmandel/ehi-to-fhir`.

## Procedure
1. Inspect README, actual license and release/commit evidence for each candidate.
2. Distinguish project capability from marketing description; classify mature, partial, archived or unverified with evidence.
3. Identify reusable standards and algorithms without copying restricted implementation details.
4. Update six or more specific gap hypotheses in `research/gap_register.csv`, marking uncertain claims unverified.

## Acceptance criteria
- At least eight relevant repositories assessed with commit/release date and license status, or individually marked blocked with reasons.
- Each proposed CLINOS feature has a 'reuse / integrate / differentiate / defer' classification.
- No blanket statement that a function has no open-source implementation without supporting search evidence.

## Universal constraints
Use synthetic or lawfully public metadata only. No PHI, live Epic access, bypass of controls, proprietary code copying or clinical use. Capture source versions, fixtures, command output and limitations. Stop rather than infer undocumented clinical semantics. Independent QA must assess the result; code author cannot self-approve.
