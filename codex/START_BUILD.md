# CODEX EXECUTION ORDER — CLINOS FIRST BUILD

**Project:** CLINOS — Clinical Integrity, Normalization & Open Systems
**Objective:** Deliver the first reproducible Rust prototype that produces privacy-minimized, deterministic evidence from wholly synthetic FHIR-shaped JSON.
**Task:** CLINOS-004 / GitHub issue #5
**Starting branch:** `codex/clinos-004-rust-foundation`; stacked on `codex/g0-agent-roadmap-literature-scaffold` while G0 PR #1 remains unmerged.
**Status:** Prototype code authored; runtime compilation and clinical/informatics review remain unverified.

## Assignment for Codex
You are CLINOS's Rust Systems Engineer. Read `AGENTS.md`, `agents/codex-orchestrator.md`, `agents/rust-systems.md`, `codex/CODEX_PROMPT.md`, `codex/ROADMAP.md`, `docs/VALIDATION.md`, `docs/TASK_QUEUE.md`, and `codex/orders/CLINOS-004-rust-workspace-ci.md`.

### First pass: establish build evidence
1. Inspect `Cargo.toml`, workspace crates, the CLI, CI, and synthetic fixtures; do not re-scaffold files that already exist.
2. Run `cargo fmt --all -- --check`, `cargo clippy --workspace --all-targets -- -D warnings`, `cargo test --workspace`, `cargo build --workspace`. Fix any actual compiler, lint, test or formatting defects.
3. Run `cargo run --bin clinos -- preflight tests/fixtures/synthetic-bundle.json`. Expect three entries, no unresolved entries, and `clinical_equivalence=NOT_TESTED`.
4. Run `cargo run --bin clinos -- preflight tests/fixtures/ambiguous-bundle.json`. Expect one unresolved entry and `clinical_equivalence=UNRESOLVED`.
5. Add command-level regression tests: `--help`, missing file, invalid JSON, excess-size file, malformed entry, non-UTF8, no patient identifier leakage.
6. Create and commit a Cargo.lock once dependencies resolve; assess dependency licenses and use pinned toolchain versions before production-oriented claims.
7. Verify GitHub Actions, record run IDs, and attach exact commands and evidence in `evidence/CLINOS-004/SUMMARY.md`.
8. Do not self-approve. Independent QA/security review remains required; keep PR in draft until accepted.

### Explicit non-goals
No Epic API calls, no PHI, no hidden integration, no clinical interpretation, no semantic migration equivalence and no authorization bypass. Structural inspection is not FHIR conformance testing.

### Stop conditions
Unexpected proprietary data, dependency/license conflicts, missing research approval for clinical logic, inability to reproduce results, or branch divergence. Document blockers and issue references; do not fabricate PASS.

### Next wave — only after review
CLINOS-001 and 002 verify standards/OSS sources. Then CLINOS-003 defines synthetic clinical ground truth; CLINOS-005 defines the semantic reconciliation contract; CLINOS-006 independently validates adversarial fixtures. CLINOS-007 may implement a true FHIR R4-aware parser only when these prerequisites are resolved.

### Deliverable
A draft PR with compiling Rust, passing tests, validated synthetic CLI behavior, Cargo.lock, corrected dependencies, exact CI logs, and a reviewer-ready evidence matrix. If any evidence is unavailable, mark NOT_TESTED.
