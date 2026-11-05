# CLINOS-004 build evidence

**Task:** CLINOS-004 / issue #5
**Branch:** `codex/clinos-004-rust-foundation`
**Base:** `codex/g0-agent-roadmap-literature-scaffold` (PR #1 pending merge)
**Execution status:** IN_PROGRESS — local compilation/tests pass; hosted CI and independent review remain blocked/pending
**Source data:** wholly synthetic JSON fixtures only
**Clinical claims:** none

## Implementation artifacts
- Rust workspace with five crates and no Epic dependencies.
- JSON structural preflight with 4 MiB input limit and explicit failures for malformed structure.
- Deterministic type/count summary, excluding patient identifiers and clinical fields.
- `NOT_TESTED` and `UNRESOLVED` only for clinical equivalence.
- GitHub Actions format/lint/test/build and two synthetic CLI smoke runs.
- Command-level regression coverage for help, missing files, malformed JSON, excess-size input, invalid UTF-8, invalid Bundle entries, and privacy-sensitive output.
- Bounded CLI file reads (at most 4 MiB + 1 byte) and rejection of non-object Bundle entries.
- Resolved dependency lockfile and license metadata review.

## Local evidence

Environment: `rustc 1.99.1 (58cf8f9c3 2026-10-13)`, `cargo 1.99.1 (5f94df478 2026-08-27)`, rustfmt 1.10.0-stable. `rust-toolchain.toml` selects `stable`, not an exact toolchain release.

Commands run from repository root:

| Command | Result |
|---|---|
| `cargo fmt --all` | PASS (formatting applied) |
| `cargo fmt --all -- --check` | PASS |
| `cargo clippy --workspace --all-targets -- -D warnings` | PASS |
| `cargo test --workspace` | PASS — 19 passed, 0 failed |
| `cargo build --workspace` | PASS |
| `cargo run --quiet --bin clinos -- preflight tests/fixtures/synthetic-bundle.json` | PASS — 3 entries; Patient/Encounter/Observation counts 1/1/1; unresolved 0; clinical equivalence NOT_TESTED |
| `cargo run --quiet --bin clinos -- preflight tests/fixtures/ambiguous-bundle.json` | PASS — 2 entries; unresolved 1; clinical equivalence UNRESOLVED |
| `cargo tree --workspace --locked --format '{p} {l}'` | PASS — all resolved crates expose MIT/Apache-2.0/Unlicense metadata |

The CLI emits resource type names and counts only. Regression tests use synthetic marker strings and assert those strings do not appear in output/errors.

## Evidence grid
| Command or check | Expected | Observed | Status |
|---|---|---|---|
| Local fmt/clippy/test/build | zero exit; all tests pass | Commands and versions recorded above | PASS (local) |
| synthetic bundle CLI | 3 entries; NOT_TESTED clinical | 3 entries; unresolved 0 | PASS (synthetic structural behavior) |
| ambiguous bundle CLI | 1 unresolved entry; UNRESOLVED clinical | 2 total entries; 1 unresolved | PASS (synthetic ambiguity behavior) |
| command-level negative/privacy tests | failures are nonzero and content is not echoed | 7 CLI integration tests passed, plus malformed-entry library test | PASS (local synthetic fixtures) |
| dependency license metadata | review complete locked graph | serde/serde_core/serde_derive/serde_json/itoa/syn/quote/proc-macro2/unicode-ident MIT OR Apache-2.0; memchr Unlicense OR MIT; zmij MIT | PASS (Cargo metadata review only; no legal review) |
| GitHub Actions | hosted workflow passes | Runs 41937889310 and 41937866724 both `startup_failure`; logs unavailable (`log not found`) | BLOCKED (CI startup/infrastructure) |
| external clinical semantics review | scoped mappings approved | Not applicable to structural preflight | NOT_TESTED |
| independent QA/security review | reviewed evidence | Not done | NOT_TESTED |

## Limitations and blockers
Local checks are not independent verification. Hosted CI for prior head `b0308dc0e2c8f0861c3a53b50f881bc74ca9a4a4` is currently unavailable: the two latest runs ended `startup_failure`, and GitHub returned no logs. A Cargo.lock is generated locally and included in the proposed change; its resolved crate versions are reproducible, but `stable` itself is not exact-pinned. G0 PR #1 remains unmerged and this PR remains intentionally stacked/draft. No standards/OSS literature matrix verification, Epic compatibility, FHIR conformance, clinical validation or clinical equivalence has occurred.

## Next execution
Restore hosted CI startup, capture a successful exact-head workflow run, and obtain independent security/privacy and QA review. Continue to hold CLINOS-001/-002 source audits and CLINOS-003/-005 semantic contracts as gates for the next implementation wave.
