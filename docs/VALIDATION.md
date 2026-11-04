# Validation and evidence policy

## Test levels
1. Parsing and schema: accepted/rejected input, FHIR version and profile claims.
2. Semantic invariants: identities, units, timestamps, encounter membership, encounter-to-order-result relationships, provenance and amendments.
3. Migration differential: source vs reconstructed target, with field-level comparison and reason codes.
4. Workflow correctness: state-machine invariants, concurrency, interruptions and compensating actions on synthetic traces.
5. Reproducibility: seeded fixture fingerprints, environment, dependency versions, report hashes.

## Mandatory negative fixtures
Missing patient, duplicate resource IDs, unresolved code, contradictory status, unit conversion mistake, time-zone shift, lost amendment, orphaned lab result, swapped patient identifier, and incorrect order-result association.

## Evidence statuses
- `PASS`: supported by successful test and independent review.
- `FAIL`: observed violation with reproducible fixture.
- `UNRESOLVED`: incomplete or ambiguous source semantics; must never be counted as pass.
- `NOT_TESTED`: no executed evidence.

Report confusion matrices and precision/recall for known injected defects. Never claim zero clinical data loss from a finite test corpus or equivalence from mere FHIR conformance.

## Governance
Security reviewer approves data ingress, logging, retention, and supply-chain changes. Clinical informatics reviewer approves semantics. Independent validator reviews claims before release. Use only synthetic test data in CI.
