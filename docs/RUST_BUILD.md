# CLINOS Rust foundation — prototype operator guide

## Purpose
The first executable slice is `clinos preflight`, a bounded JSON shape inspector for synthetic FHIR-shaped files. It does not validate FHIR resource profiles, clinical terminology, complete patient histories, EHI exports, migration fidelity or patient safety.

## Local commands
Requires Rust toolchain with Cargo, rustfmt and clippy.

```sh
cargo fmt --all -- --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
cargo build --workspace
cargo run --bin clinos -- --help
cargo run --bin clinos -- preflight tests/fixtures/synthetic-bundle.json
cargo run --bin clinos -- preflight tests/fixtures/ambiguous-bundle.json
```

The first fixture contains three synthetic resource entries (Patient, Encounter, Observation). Structural preflight should count three entries, with zero unresolved. The second contains one resource entry and one ambiguous entry and must report `UNRESOLVED`. These outcomes are **expected**, not executed verification results until CI passes.

`preflight` limits input to 4 MiB and writes a machine-readable JSON summary. It reports only resource *type names and counts*, not IDs or patient contents. For malformed JSON, invalid root structure, missing root resourceType or invalid Bundle entry shape, the command exits nonzero without printing source data. The status field is exclusively a research assessment: `clinical_equivalence` is `NOT_TESTED` or `UNRESOLVED`, never `PASS`.

## Architecture
- `clinos-core`: evidence vocabulary.
- `clinos-fhir`: bounded JSON structural preflight (not FHIR validation).
- `clinos-integrity`: conservative untested/unresolved classification.
- `clinos-evidence`: privacy-minimized machine-readable report.
- `clinos-cli`: operator executable.

## Security and future changes
Do not run on production PHI or connect to a live EHR. Structural preflight cannot establish compliance, clinical completeness or EHI migration accuracy. This baseline intentionally avoids patient field logging. Any extension to semantic mappings requires clinical informatics and terminology review. Dependency `serde_json` requires source/license audit and a generated Cargo.lock before reproducible release claims.

## Acceptance
The PR may move from draft only after CI/lint/tests have run and a separate reviewer has checked negative behavior, privacy and claims. Source audit and approved synthetic contracts are separate roadmap gates.
