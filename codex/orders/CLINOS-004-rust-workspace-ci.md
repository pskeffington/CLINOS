# CLINOS-004 — Minimal Rust workspace and CI scaffold

**Priority:** P0 | **Gate:** G1/G2 substrate | **Dependencies:** G0 research/architecture baseline; CLINOS-003 contracts required before semantic implementation | **Primary:** Rust Systems Engineer | **Reviewers:** Security & Privacy + Independent Validator

## Deliverables
- Minimal root Cargo workspace and isolated `clinos-core`, `clinos-fhir`, `clinos-integrity`, `clinos-evidence` and `clinos-cli` crates (proposed names; verify architecture before implementation).
- CI running cargo fmt, clippy, test, build and dependency/security checks if supported by available tooling.
- Stable CLI skeleton with `--help` and nonzero exit codes on bad input; no live endpoint integrations.
- Architecture record for crate boundaries and dependency versions.

## Acceptance criteria
- Commands executed locally where available: `cargo fmt --all -- --check`, `cargo clippy --workspace --all-targets -- -D warnings`, `cargo test --workspace`, `cargo build --workspace`.
- Where not available, mark NOT_TESTED and provide reproducible instructions; do not report PASS.
- No unsafe Rust without documented exception and review; no network call or secret in test fixtures.
- A clean check against accidental real-data files and generated artifacts.

## Stop criteria
Contract mismatch or dependency license conflict -> stop before implementation and record decision.

## Universal constraints
Use synthetic or lawfully public metadata only. No PHI, live Epic access, bypass of controls, proprietary code copying or clinical use. Capture source versions, fixtures, command output and limitations. Stop rather than infer undocumented clinical semantics. Independent QA must assess the result; code author cannot self-approve.
