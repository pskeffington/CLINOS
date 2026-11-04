# CLINOS agent operating charter

## Mission
Build a vendor-neutral, open-source clinical data integrity and migration validation platform. Epic EHI is an initial interoperability research target, not a claim to reproduce Epic software. Use authorized interfaces and synthetic test fixtures by default.

## Chain of command
1. **Research Director** (`agents/research-director.md`): maintains literature/standards evidence and gap register; defines claims and confidence.
2. **Clinical Informatics Lead** (`agents/clinical-informatics.md`): owns resource semantics, FHIR R4 mappings, clinical terminology and provenance.
3. **Rust Systems Engineer** (`agents/rust-systems.md`): owns deterministic core architecture, parsers, interfaces and build integrity.
4. **Migration Audit Engineer** (`agents/migration-auditor.md`): owns reconciliation rules, missingness, linkage and negative fixtures.
5. **Workflow Simulation Engineer** (`agents/workflow-simulator.md`): owns synthetic encounter and department transitions.
6. **Security & Privacy Reviewer** (`agents/security-privacy.md`): owns data classification, supply-chain, and privacy controls.
7. **Independent Clinical Safety / QA Validator** (`agents/independent-validator.md`): independent release blocker, verifies safety claims and performance evidence.

## Required execution sequence
- Read `docs/ROADMAP.md`, `docs/VALIDATION.md`, and `research/literature_matrix.csv` before implementing a task.
- Create an issue/task with scope, dependencies, acceptance tests, primary sources and risk classification.
- Research Director records sources and identifies unverified assumptions; Informatics Lead approves semantic mappings before code merges.
- Implement small deterministic changes with positive, negative, and adversarial fixtures.
- Independent Validator checks outputs and evidence separately; security/privacy reviewer approves external-data and telemetry changes.
- Merge only after CI and documented gate evidence; unverified hardware, external Epic compatibility, and real-world clinical safety must not be declared complete.

## Non-negotiable safeguards
- No patient PHI, credentials, production EHR access or real clinical orders in default fixtures/logs/CI.
- Use synthetic or explicitly authorized/de-identified data with approved handling. Synthetic datasets should be clearly labeled and checked for accidental real identifiers.
- Do not circumvent access controls, licensing, authentication or proprietary protection. Clean-room interoperability methods only.
- FHIR-conformant is not synonymous with clinical equivalence; schema validation cannot prove clinical safety.
- Never infer missing relationships as facts. Emit `UNRESOLVED` with evidence and confidence.
- No patient-facing clinical recommendations or deployment into care until independent, applicable validation and governance.
- No vendor endorsement or Epic certification claim without primary-source evidence.

## Deliverable contract
Every change must document: task ID, hypothesis, tested input corpus and version, expected/actual results, false positive/negative impact, limitations, reproducibility commands, and source references. Mark statuses `PLANNED`, `IN_PROGRESS`, `BLOCKED`, `PASS`, or `FAIL` only with evidence.
