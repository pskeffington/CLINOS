# CLINOS Codex master execution prompt

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

## Block decision / continuation protocol
When a command, CI run, dependency, reviewer, source or permission blocks progress, do not end in a retry loop. Invoke the role documented in `agents/block-resolution.md`; classify the incident according to `codex/CONTINUITY_POLICY.md`, preserve original status and record a blocker decision using `codex/BLOCK_DECISION_TEMPLATE.md`. Attempt only permitted bounded remediation. If unresolved, dispatch the highest-priority independent READY task that passes all gates; otherwise stop with exact escalation and reopening conditions. No auto-approval, CI disabling, privilege escalation or clinical/privacy override. Include BLOCKER_ID and FALLBACK_TASK in the final report.

## Unresolved Tier 1 blocker escalation
After Block Resolution Agent reports unresolved, invoke the Resolution Decision Agent following `codex/ESCALATION_CHAIN.md`. Include the Tier 1 record, exact SHA, logs, attempts, blockers, alternative tasks and approval constraints. Obtain a documented Tier 2 disposition before splitting scope or selecting a different engineering approach. Respect all original safety and review gates. Report the resolution decision ID in the task summary.

## Next authorized development pass
Read `codex/NEXT_EXECUTION_ORDER.md` before selecting follow-up work. Prioritize independently reviewable CLINOS-001/002 source audits while CI startup and G0 approvals remain outstanding. Route unresolved blockers through Tier 1 and Tier 2. No clinical semantics implementation until approved contracts and evidence exist.

## GPT solution mechanics path
For an unresolved technical issue, Tier 2 may request an optional GPT consultation under `codex/GPT_CONSULTATION.md`. Create a curated allowlisted payload, preview locally, and obtain explicit operator approval before calling the provider. Treat the returned JSON as unverified engineering advice, validate mechanisms with primary evidence and tests, and continue standard review gates. No credentials/PHI/private logs may be transmitted. If network/configuration absent, continue offline with `NOT_QUERIED`.

## Active next-pass execution packet — CLINOS-014
Read `codex/NEXT_PASS_004.md` and `codex/orders/CLINOS-014-gpt-consult-hardening.md` before implementing the GPT consultation tooling. This packet directs offline client hardening, failure-path tests and guarded Tier 2 integration. It separately authorizes only research/specification preparation for CLINOS-003 until Informatics and Terminology signoffs exist. Preserve the draft PRs and record exact-head test evidence; do not call the external provider automatically.
