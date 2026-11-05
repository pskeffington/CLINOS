# CLINOS research and development roadmap

**Status:** G0 scaffolding in progress. No completed compatibility or clinical safety claims.

| Gate | Priority | Deliverable | Evidence required | Exit condition |
|---|---|---|---|---|
| G0 | P0 | Agent hierarchy, scope, standards and GitHub literature matrix | Linked sources, license audit, gap and risk register | Independently reviewed plan and constraints |
| G1 | P0 | Deterministic synthetic clinical corpus | Seeded patients, encounters, orders, results, amendments, negative cases | Fixtures reproduce byte-for-byte and have documented ground truth |
| G2 | P0 | FHIR R4 ingest, parse and normalize | Versioned resource schemas and referential validation | Schema checks plus semantic invariants across seeded fixtures |
| G3 | P0 | Migration integrity and semantic diff engine | Injected unit, omission, duplicate, timestamp, identity, provenance and linkage errors | All designated critical errors found in controlled fixtures; FP/FN explicitly measured |
| G4 | P1 | Documented Epic EHI export adapter | Authorized/public specs, parser coverage matrix, unsupported fields | Grounded record-level reconstruction on lawful synthetic samples |
| G5 | P1 | Hospital workflow simulation | Admission, lab, imaging, transfers, discharge and billing event graph | Repeatable failure and concurrency cases; no clinical equivalence claim |
| G6 | P1 | Oncology workflow research test suite | Synthetic regimens, versions, lab dependencies, deferrals | Cross-reviewed non-clinical validation scenarios |
| G7 | P1 | Evidence and reproducibility reports | JSON/HTML, provenance chain and test attestations | Auditable regenerated findings and clear unresolved status |
| G8 | P2 | Cross-platform EHR test harness | OpenEMR/OpenMRS/Medplum adapters as permitted | Documented comparison and interface constraints |
| G9 | P2 | Production security and governance planning | Threat model, privacy impact, SBOM, regulatory gap analysis | Independent governance approval before any real-data deployment |

## Immediate task sequence
1. **CLINOS-001** Inventory 2026-current EHI export and FHIR standards; verify Epic-specific public documentation independently.
2. **CLINOS-002** Build cited OSS literature matrix, compare maintained projects, validate licenses and latest commits.
3. **CLINOS-003** Define deterministic synthetic data generator and clinical invariants.
4. **CLINOS-004** Design minimal Rust crate interfaces without premature implementation.
5. **CLINOS-005** Specify semantic reconciliation output: PASS / FAIL / UNRESOLVED with provenance.
6. **CLINOS-006** Build adversarial test plan and independent QA decision records.

## Scope boundaries
In scope: synthetic testing, lawful export parsing, standards adapters, fidelity measurement, reproducible research. Out of scope until explicitly gated: extracting proprietary Epic binaries, bypassing authentication, operational care delivery, production patient records, clinical prescribing or autonomous safety decisions.

## Definition of done
A gate is not done solely because code compiles. Evidence includes versioned fixtures, command transcript, test coverage, independent review, limitations and reproducible results.

## Codex execution mapping
The executable research and implementation passes are specified in [Codex Roadmap](../codex/ROADMAP.md), with authoritative status in [Task Queue](TASK_QUEUE.md). Each pass uses an individual [work order](../codex/orders/) and requires independent review. G0 scaffold files are not evidence of completed validation.
