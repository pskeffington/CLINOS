# CLINOS-014 — GPT Consultation Agent Hardening

**Priority:** P0 engineering infrastructure
**Dependencies:** draft PR #11 reviewed as baseline; no clinical implementation dependency
**Owner:** Rust/Tooling Engineer with Security & Privacy reviewer and Independent QA reviewer
**Scope:** `tools/gpt_solution_consult.py`, its tests, consultation docs, and CI only
**Branch:** dedicate a small implementation branch after the instruction packet is reviewed

## Build objective
Turn the initial opt-in GPT Solution Mechanics Consultant into a robust, documented, offline-testable engineering support tool. It must ask an approved GPT model for candidate *solution mechanics*, not implement or execute them. The result must return to the Resolution Decision Agent as `PROPOSED_UNVERIFIED`.

## First action — inspect and reproduce
1. Read `AGENTS.md`, `agents/block-resolution.md`, `agents/resolution-decision.md`, `agents/gpt-solution-consultant.md`, `codex/GPT_CONSULTATION.md`, and this order.
2. Inspect current PRs #1, #8–#11 and their exact heads. Do not overwrite research branches or conflate stacked PRs.
3. Run `python3 -m unittest discover -s tools -p 'test_gpt_solution_consult.py' -v` and `python3 tools/gpt_solution_consult.py --input tools/fixtures/gpt-consult-ci.json`.
4. Report observed errors exactly. Do not report a pass when execution is unavailable.

## Hardening pass
1. Check failure behavior for nonexistent, oversized, malformed, non-UTF8 and non-object input files.
2. Ensure the payload contains only the declared allowlisted fields and is previewed before external transfer. Reject ambiguous or potentially sensitive content conservatively. Never claim automated redaction alone prevents all sensitive-data leakage.
3. Test calls without model, without API key, without `--send`, and with only one of the two authorization flags. No request should be transmitted in these cases.
4. Use fake transport for offline tests: HTTP error, timeout, incomplete Responses API result, malformed JSON, missing output text, excessive output, unexpected object structure, and provider output containing instruction-like text.
5. Inspect current official Responses API specification; verify request and response fields. Distinguish local protocol tests from a real provider acceptance test. Keep model identifiers configured, not hardcoded.
6. Verify `store:false` and document that API data handling depends on provider policies. Do not claim that a request is private merely because storage is disabled.
7. Make consultation output a *data-only artifact*. Never eval, execute shell commands, automatically create a PR from a GPT response, disable CI or bypass an approver.
8. Record metadata for consultation attempts: task ID, blocker ID, model identifier, timestamp, request schema version, response validation status, reviewing agent, and approved next action. Do not log raw source data, credentials or patient content.
9. Limit response size and consultations per unchanged blocker evidence. Use an explicit circuit breaker to avoid unbounded retries and cost escalation.
10. Keep all tests offline and deterministic. Any live smoke test requires separately approved provider access and curated public/synthetic content.

## Required evidence
- Exact Python version and test command output.
- Negative tests for all documented failure modes.
- Preview of synthetic CLINOS-004 startup_failure request.
- Security and privacy analysis of outbound data policy, logging and provider error handling.
- Scope/compatibility note for any Responses API changes.
- Independent QA and Security review status in `evidence/CLINOS-014/SUMMARY.md`.
- Draft PR with reproducible instructions and no unrelated core clinical changes.

## Gate
Do not mark CLINOS-014 PASS unless the test suite executes successfully and independent reviewers approve applicable evidence. Do not mark the GPT tool as approved for production PHI or automated code execution. CLINOS-004 hosted CI failure remains a separate unresolved gate.
