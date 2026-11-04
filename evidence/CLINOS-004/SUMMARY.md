# CLINOS-004 build evidence

**Task:** CLINOS-004 / issue #5
**Branch:** `codex/clinos-004-rust-foundation`
**Base:** `codex/g0-agent-roadmap-literature-scaffold` (PR #1 pending merge)
**Execution status:** IN_PROGRESS — implementation committed, runtime evidence not yet established
**Source data:** wholly synthetic JSON fixtures only
**Clinical claims:** none

## Implementation artifacts
- Rust workspace with five crates and no Epic dependencies.
- JSON structural preflight with 4 MiB input limit and explicit failures for malformed structure.
- Deterministic type/count summary, excluding patient identifiers and clinical fields.
- `NOT_TESTED` and `UNRESOLVED` only for clinical equivalence.
- GitHub Actions format/lint/test/build and two synthetic CLI smoke runs.

## Evidence grid (pending external execution)
| Command or check | Expected | Observed | Status |
|---|---|---|---|
| `cargo fmt --all -- --check` | zero exit | Not run here | NOT_TESTED |
| `cargo clippy --workspace --all-targets -- -D warnings` | zero exit | Not run here | NOT_TESTED |
| `cargo test --workspace` | tests pass | Not run here | NOT_TESTED |
| `cargo build --workspace` | zero exit | Not run here | NOT_TESTED |
| synthetic bundle CLI | 3 entries; NOT_TESTED clinical | Not run here | NOT_TESTED |
| ambiguous bundle CLI | 1 unresolved; UNRESOLVED clinical | Not run here | NOT_TESTED |
| malformed input/no identifier echo | rejected without content | Unit tests authored, not run | NOT_TESTED |
| external clinical semantics review | scoped mappings approved | Not applicable to structural preflight | NOT_TESTED |
| independent QA review | reviewed evidence | Not done | NOT_TESTED |

## Limitations and blockers
The current execution environment has no Rust toolchain, so no Rust compile/test success is asserted. GitHub CI may provide evidence after the PR workflow triggers; record its exact run URL before changing test statuses. Cargo.lock has not been generated. G0 PR #1 is unmerged; this build is intentionally stacked. No standards/OSS literature matrix verification, Epic compatibility or clinical validation has occurred.

## Next execution
Run `codex/START_BUILD.md`, repair any compiler/lint errors, add command-level regression tests, generate Cargo.lock and record hosted CI evidence, then obtain independent review.
