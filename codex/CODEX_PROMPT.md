# CLINOS Codex master execution prompt

## ACTIVE BUILD GOAL — CLINOS-004 / first executable Rust prototype

**Goal:** Build, compile, and independently verify the five-crate CLINOS foundation and a privacy-minimized `clinos preflight <synthetic-json-file>` command. It inspects JSON structure only; it must not assert FHIR profile conformance, Epic compatibility or clinical equivalence.

**Immediate action:** Read `codex/START_BUILD.md` and follow its command-by-command acceptance requirements. The branch `codex/clinos-004-rust-foundation` already contains initial implementation; inspect and fix that code rather than re-creating a competing scaffold. G0 governance is on an unmerged parent branch, so leave implementation in a **draft stacked PR** until upstream approval.

**Success evidence:** exact cargo fmt/clippy/test/build output, deterministic CLI results on both synthetic fixtures, expected failures, a committed Cargo.lock, CI run links, documented blockers and independent QA/security review. Mark unavailable checks `NOT_TESTED` and stop if clinical semantics or live records are requested.


You are operating in `pskeffington/CLINOS`, an independent clinical integrity research repository.

Read the following **in order** before changing anything:
1. `AGENTS.md` and `agents/codex-orchestrator.md`.
2. `docs/ROADMAP.md`, `codex/ROADMAP.md`, `docs/TASK_QUEUE.md` and `docs/VALIDATION.md`.
3. `research/literature_matrix.csv` and applicable `codex/orders/CLINOS-XXX-*.md`.
4. Existing branches, CI status and PRs to avoid duplication.

## Execute exactly one assigned order
- State the task ID and scope. Check dependencies and stop if they are unmet.
- Make a concise implementation plan: files affected, acceptance criteria, negative tests and risk classification.
- Use only synthetic data and explicitly documented standards. No PHI or production Epic integrations.
- Keep the change minimal, deterministic, and independently verifiable.
- Maintain source-linked evidence; mark preliminary literature rows unverified until checked.
- For Rust code: format, lint, test and build when tooling exists; record when tools are unavailable rather than inventing results.
- If a task changes clinical semantics, obtain independent informatics and terminology review.
- Treat security, privacy and QA review as independent gates. Do not sign off your own implementation.
- Open a draft PR and update `docs/TASK_QUEUE.md` and `evidence/<TASK-ID>/SUMMARY.md` with results.

## Final report template
TASK: CLINOS-XXX
BRANCH / PR: ...
FILES: ...
TESTS RUN (exact commands): ...
RESULTS: PASS / FAIL / NOT_TESTED per gate, including negative tests
SOURCES AND VERSION: ...
RISKS / OPEN QUESTIONS: ...
BLOCKERS: ...
INDEPENDENT REVIEW STATUS: ...
NEXT TASK: ...

If tool access prevents execution, create a reproducible plan and mark the affected check NOT_TESTED. Never write a fabricated benchmark or compatibility claim.
