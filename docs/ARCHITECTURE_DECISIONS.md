# Architecture decision log

## ADR-0001: Vendor-neutral interfaces first
Status: PROPOSED (2026-11-04). Core models must not require Epic internal schemas; adapter-specific behavior stays at the edge.

## ADR-0002: Synthetic-data-only baseline
Status: PROPOSED. CI fixtures are generated synthetic records with stable seeds and documented ground truth. Real patient data is outside the initial scope.

## ADR-0003: Preservation of uncertainty
Status: PROPOSED. Reconciliation emits PASS, FAIL, UNRESOLVED or NOT_TESTED with source pointers. No inferred linkage is represented as verified.

## ADR-0004: Rust deterministic core
Status: PROPOSED. Prefer a Rust workspace with isolated parse, normalization, integrity, and evidence components; Python/R are optional offline research and reporting tools. Exact crate interfaces are deferred to CLINOS-004.

## ADR-0005: Version-locked external standards
Status: PROPOSED. Record specification versions and implementation-guide contexts; never assume FHIR resources or EHI exports share the same semantic guarantees.

## ADR-0006: Independent validation
Status: PROPOSED. Developer and evaluator roles are separate; clinical mapping and privacy reviews may veto releases.

Each accepted ADR must identify the owner, tested alternatives, rationale, known failure modes and superseding decision.
